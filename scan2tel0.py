import numpy as np
from path import path
from is_it_here import is_it_here
import matplotlib.pyplot as plt

#from scopes100 import labels
from updateN import updateN
from kmeans import kmeans
from closest_point import closest_point
from labelmax_solo import labelmax_solo
from plant_event import plant_event
from prob_in_blob import prob_in_blob

def scan2tel0( phiI, thetaI, pointsra, pointsdec, tele,t_update, minra, mindec, ramax, decmax,  ii, timearr, theta, phi, tottime, j,event_ipix,hpx,nside,kks,phis,thetas,timearrs,r,passedra,passeddec,scanned_ra,scanned_dec,scanned_pix,scanned_time,kk,pointslabels,labelmax,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulk, bulkra, bulkdec,scanned_pix_s,z,t0):
    print('scan2tel0')
    wewewe=False
    is_here = False
    rachange = []
    decchange = []
    tchange = []
    uflag=0
    merge=False
    tempdis=10000
    minrap1=0
    mindecp1=0
    minrap = 0
    mindecp = 0
    pointsra1=pointsra
    pointsdec1=pointsdec
    #print('minra',pointslabels,labelmax,minra,mindec)
    print('kk1',kk,len(pointsra))
    for i in range(len(pointsra)):
        if abs(minra - pointsra[i]) + abs(mindec - pointsdec[i]) < tempdis and pointslabels[i]==labelmax:
            tempdis = abs(minra - pointsra[i]) + abs(mindec - pointsdec[i])
            minrap = pointsra[i]
            mindecp = pointsdec[i]

    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(phiI, thetaI, minrap, mindecp)
    ra,dec=minrap, mindecp
    raI, decI=phiI, thetaI
    if not merge:
        if t_update!=[]:
            while (time >= t_update[uflag] ):
                raI, decI = tele.place(t_update[uflag], raI, decI, flag, flago, flag2, flago2, ra,dec, timetheta, timephi, sign, time2)
                tempdis = 10000
                rachange.append(1000000)
                decchange.append(1000000)
                tchange.append(1000000)

                hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels, kk1, kk2,labels, labelsc, nkmeans = updateN(nside, pointsra, pointsdec, r2, kk1, kk2, kks, pointslabels, area_update[uflag], hpx)
                labelmax,bulkramax,bulkdecmax,minra,mindec=labelmax_solo(bulkra, bulkdec, bulk, labels, nkmeans, tele,raI, decI)

                for i in range(len(pointsra)):
                    if abs(minrap - pointsra[i]) + abs(mindecp - pointsdec[i]) < tempdis :
                        print(uflag,rachange)
                        tempdis = abs(minrap - pointsra[i]) + abs(mindecp - pointsdec[i])
                        #minrap1 = pointsra[i]
                        #mindecp1 = pointsdec[i]
                        #ra, dec = minrap1, mindecp1
                        rachange[uflag] = pointsra[i]
                        decchange[uflag] = pointsdec[i]
                        tchange[uflag] = t_update[uflag]
                        kk = i
                    # print('re', aa,pointsra[kk1], pointsdec[kk1], pointsra[kk2], pointsdec[kk2])
                uflag = uflag + 1
                if uflag == len(t_update) :
                    merge = True
                    if  event_ipix == 0 and met==0 and z==0:
                        #print('plant_event01',r)
                        event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)
                    break
        else:
            merge=True
            if  event_ipix == 0 and met==0 and z==0 :

                event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)

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
    if timearrs[-1]>t0 and timearrs[-1]!=100000:
        merge= True
        if met == 0 and event_ipix == 0 and z == 0:
            event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)
    else:
        merge= False
    if merge:
        print('kk',kk,len(pointsra))
        passedra.append(pointsra[kk])
        passeddec.append(pointsdec[kk])
        kks.append(kk)
        is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(hpx, pointsra[kk], pointsdec[kk], r, nside, event_ipix)
        #print('s01', is_here, scanned_ra1, scanned_dec1,ipix_disc)
        #plt.plot(2, 2)
        #plt.show()
        #scanned_pix.append(ipix_disc)
        #if not (tele.name == 'BIG' and met == 1):
        scanned_time.append(timearrs[-1])
        scanned_ra.append(scanned_ra1)
        scanned_dec.append(scanned_dec1)
        if (tele.name == 'BIG' or tele.name == 'ULTARASAT') and is_here:
            scanned_pix_s = ipix_disc
            #print('ipix_disc0', scanned_pix_s)
            #plt.plot(2, 2)
            #plt.show()
        else:
            scanned_pix.extend(ipix_disc)

    if minrap1!=0 and mindecp1!=0:
        print('y')

        minrap=minrap1
        mindecp=mindecp1
    kkf=0
    print('kk',len(pointsra1),kk)
    for i in range(len(pointsra1)):
        if pointsra[kk]==pointsra1[i] and pointsdec[kk]==pointsdec1[i]:
            kkf=i
            print('yy')

    print('1',kkf,pointsra1[kkf],pointsdec1[kkf],minrap,mindecp,r,len(pointsra1))
    #plt.plot(2,2)
    #plt.show()
    if rachange!=[]:
        minrap=rachange[-1]
        mindecp=decchange[-1]
    return phis, thetas, timearrs,  scanned_ra, scanned_dec,scanned_pix, scanned_time,passedra, passeddec,is_here,kkf,minrap,mindecp,event_ipix,pointsra1,pointsdec1,turn_points_ra,turn_points_dec,scanned_pix_s
