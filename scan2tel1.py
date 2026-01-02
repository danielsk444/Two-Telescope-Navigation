import numpy as np
from path import path
from is_it_here import is_it_here
import matplotlib.pyplot as plt

#from scopes100 import labels
from kmeans import kmeans
from closest_point import closest_point
from labelmax_solo import labelmax_solo
from plant_event import plant_event
from prob_in_blob import prob_in_blob
def scan2tel1(phiI, thetaI, pointsras, pointsdecs, tele,t_update, minrap, mindecp, ramax, decmax,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis,thetas,timearrs,r,passedra,passeddec,scanned_ra,scanned_dec,scanned_pix,scanned_time,kk,pointslabelss,labelss,labelmax,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0):
    print('scan2tel1')
    is_here = False
    rachange = []
    decchange = []
    tchange = []
    uflag=0
    merge=False

    hpx = hpxs[0]
    pointslabels = pointslabelss[0]
    bulk = bulks[0]
    bulkra = bulkras[0]
    bulkdec = bulkdecs[0]
    pointsra1=pointsras[0]
    pointsdec1=pointsdecs[0]
    pointsra=pointsra1
    pointsdec=pointsdec1

    #print('minra',pointslabels,labelmax,minra,mindec)
    print('kk1', pointsra1[0])
    print('kk2', pointsdec1[0])
    print('kk3', pointslabelss[0][0])

    '''
    for i in range(len(pointsra1)):
        if abs(minra - pointsra1[i]) + abs(mindec - pointsdec1[i]) < tempdis and pointslabelss[0][i]==labelmax:
            tempdis = abs(minra - pointsra1[i]) + abs(mindec - pointsdec1[i])
            minrap = pointsra1[i]
            mindecp = pointsdec1[i]
    '''
    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(minrap, mindecp,phiI, thetaI)

    if t_update!=[]:
        while (time >= t_update[uflag] ):

            uflag = uflag + 1
            hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels,labels= hpxs[uflag],bulks[uflag],bulkras[uflag],bulkdecs[uflag],pointsras[uflag],pointsdecs[uflag],pointslabelss[uflag],labelss[uflag]
            print('bulks', bulks)
            print('bulks[0]', bulks[0])

            #plt.plot(2, 2)
            #plt.show()
            ra, dec = tele.place(t_update[uflag-1]-timearrs[-1],phiI, thetaI, flag, flago, flag2, flago2,minrap, mindecp, timetheta, timephi, sign, time2)
            turn_points_ra=np.append(turn_points_ra,ra)
            turn_points_dec=np.append(turn_points_dec,dec)
            phi, theta, timearr,i, turn_points_ra, turn_points_dec = path(tele, phiI, thetaI,ra, dec , tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j, turn_points_ra, turn_points_dec)
            phis = np.append(phis, phi)
            thetas = np.append(thetas, theta)
            timearr = np.add(timearr, timearrs[-1])
            timearrs = np.append(timearrs, timearr)
            tempdis = 10000
            print('bulk',bulk)
            #plt.plot(2,2)
            #plt.show()
            labelmax, bulkramax, bulkdecmax, minrap, mindecp=labelmax_solo(bulk,labels,tele, ra, dec,pointsra,pointsdec, pointslabels)
            print('minrap1',minrap,mindecp,phiI,thetaI,r)
            '''
            for i in range(len(pointsra)):
                if abs(minra - pointsra[i]) + abs(mindec - pointsdec[i]) < tempdis and pointslabels[i]==labelmax :
                    tempdis = abs(ra - pointsra[i]) + abs(dec - pointsdec[i])
                    minrap = pointsra[i]
                    mindecp = pointsdec[i]
            '''
            print('minrap2',minrap,mindecp,phiI,thetaI,r)
            #plt.plot(2,2)
            #plt.show()
            time, flag, flago, flago2, flag2, timetheta, timephi, sign, time2 = tele.time( minrap, mindecp,ra, dec)
            phiI,thetaI=ra, dec
            if uflag == len(t_update):
                break

    if tchange==[]:
        tchange=[10000]
    if not merge:
        delay=0

    phi, theta, timearr, i,turn_points_ra,turn_points_dec = path(tele, phiI, thetaI, minrap, mindecp, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,turn_points_ra,turn_points_dec)
    phis = np.append(phis, phi)
    thetas = np.append(thetas, theta)
    timearr = np.add(timearr, timearrs[-1])
    timearr[-1]=timearr[-1]+delay
    timearrs = np.append(timearrs, timearr)
    #if wewewe:
    #    print('turn_points_ra',timearrs,phis,thetas,turn_points_ra,turn_points_dec)
    #    plt.plot(phis,thetas)
    #    plt.show()
    print('s0', r,phis,thetas,timearrs,merge,timearr, event_ipix, phiI, thetaI, minrap, mindecp)
    #plt.plot(2,2)
    #plt.show()
    if timearrs[-1]>=t0 and timearrs[-1]!=100000:
        merge= True

        if met == 0 and event_ipix == 0 and z == 0:
            event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)

    else:
        merge= False
    if merge:
        passedra.append(minrap)
        passeddec.append(mindecp)
        is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(minrap, mindecp, r, nside, event_ipix)
        print('s0', is_here,ipix_disc)
        print('fffffff',tele.name)
        #plt.plot(2, 2)
        #plt.show()
        #scanned_pix.append(ipix_disc)
        #if not (tele.name == 'BIG' and met == 1):
        scanned_time.append(timearrs[-1])
        scanned_ra.append(scanned_ra1)
        scanned_dec.append(scanned_dec1)
        if (tele.name == 'BIG' or tele.name == 'ULTRASAT') and is_here:
            scanned_pix_s = ipix_disc
            #print('ipix_disc0', scanned_pix_s)
            #plt.plot(2, 2)
            #plt.show()
            print('s1', is_here, ipix_disc)

            print('fffffff', tele.name)
            #plt.plot(2, 2)
            #plt.show()
        else:
            scanned_pix.extend(ipix_disc)
            print('s2', is_here, ipix_disc)
            print('fffffff2131', tele.name)
            #plt.plot(2, 2)
            #plt.show()



    return phis, thetas, timearrs,  scanned_ra, scanned_dec,scanned_pix, scanned_time,passedra, passeddec,is_here,minrap,mindecp,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,labelmax
