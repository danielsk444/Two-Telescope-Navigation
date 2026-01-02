import numpy as np
from path import path
from is_it_here import is_it_here
from calc_ipix import calc_ipix
import matplotlib.pyplot as plt
from is_in_nested_list import is_in_nested_list

def scan2tel2(pointsra, pointsdec, tele,tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,  event_ipix,hpx,nside,minrap,mindecp,kks,phis,thetas,timearrs,F,r,passedra,passeddec,scanned_ra,scanned_dec,scanned_pix,scanned_time,countwhile,kk,tempdis,c,labels,y,flag,pointslabels,labelmax,delay,merge,t_update,met, changepix,change_is_here):
    print('yes 3')
    is_here=False
    turn_points_ra=[]
    turn_points_dec = []
    candidx = []
    canddis = []
    countwhile = countwhile + 1
    print('countwhile',countwhile)
    #plt.plot(2,2)
    #plt.show()
    if not merge:
        delay=0
    for i in range(len(pointsra)):
        print(len(pointsra),kk)
        if abs(pointsra[kk] - pointsra[i]) > 180:
            radis = 360 - max(pointsra[kk], pointsra[i]) + min(pointsra[kk], pointsra[i])
        else:
            radis = abs(pointsra[kk] - pointsra[i])
        if abs(rachange - pointsra[i]) > 180:
            radis1 = 360 - max(rachange, pointsra[i]) + min(rachange, pointsra[i])
        else:
            radis1 = abs(rachange - pointsra[i])
        print('tempdis',tempdis)
        #plt.plot(2,2)
        #plt.show()
        print('e1', radis + abs(pointsdec[kk] - pointsdec[i]) , c, r , radis1 + abs(decchange - pointsdec[i]), tempdis , pointslabels[i],labelmax , i , kks,countwhile)

        print('e', is_in_nested_list(scanned_pix, event_ipix) ,(not is_in_nested_list(scanned_pix, calc_ipix(pointsra[i], pointsdec[i],nside)))  , radis + abs(pointsdec[kk] - pointsdec[i]) < c* r , radis1 + abs(decchange - pointsdec[i]) < tempdis , pointslabels[i]==labelmax ,(not is_in_nested_list(scanned_pix, calc_ipix(pointsra[i], pointsdec[i],nside)))  and radis + abs(pointsdec[kk] - pointsdec[i]) < c* r and radis1 + abs(decchange - pointsdec[i]) < tempdis and pointslabels[i]==labelmax)

        if (not is_in_nested_list(scanned_pix, calc_ipix(pointsra[i], pointsdec[i],nside)))  and radis + abs(pointsdec[kk] - pointsdec[i]) < c* r and radis1 + abs(decchange - pointsdec[i]) < tempdis and pointslabels[i]==labelmax and i not in kks :
            candidx.append(i)
            canddis.append(radis + abs(pointsdec[kk] - pointsdec[i]))
    if canddis != []:
        #countwhile = 0
        print('yes')
        c = 1.5
        jj = candidx[canddis.index(min(canddis))]
        if abs(rachange - pointsra[i]) > 180:

            radis1 = 360 - max(rachange, pointsra[jj]) + min(rachange, pointsra[jj])
        else:
            radis1 = abs(rachange - pointsra[jj])
        tempdis =  radis1 + abs(decchange - pointsdec[jj])
        phi1, theta1, timearr1, i,turn_points_ra,turn_points_dec = path(tele, pointsra[kk], pointsdec[kk], pointsra[jj], pointsdec[jj], tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,turn_points_ra,turn_points_dec)
        phis = np.append(phis, phi1)
        thetas = np.append(thetas, theta1)
        timearr1 = np.add(timearr1, timearrs[-1])
        timearr1[-1] = timearr1[-1] + delay
        timearrs = np.append(timearrs, timearr1)
        print('s2', r,phis, thetas, timearrs,merge,timearr1, event_ipix, timearrs[-1],t_update, pointsra[kk], pointsdec[kk], pointsra[jj], pointsdec[jj])
        #plt.plot(2, 2)
        #plt.show()
        kk = jj
        if t_update==[]:
            t_update=[0]
        if timearrs[-1] >= t_update[-1]:
            print('222',merge,timearrs[-1] , t_update[-1] ,not (tele.name=='BIG' and met==1))
            #plt.plot(2,2)
            #plt.show()
        change_is_here, scanned_ra1, scanned_dec1, ipix_disc = is_it_here(hpx, pointsra[kk], pointsdec[kk], r, nside, changepix)

        if merge and timearrs[-1] >= t_update[-1]:
            kks.append(kk)
            is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(hpx, pointsra[kk], pointsdec[kk], r, nside, event_ipix)
            print('s21', is_here, scanned_ra1, scanned_dec1, ipix_disc)

            #scanned_pix.append(ipix_disc)
            #if not (tele.name=='BIG' and met==1):
            scanned_time.append(timearrs[-1])
            scanned_pix.append(ipix_disc)
            scanned_ra.append(scanned_ra1)
            scanned_dec.append(scanned_dec1)
            passedra.append(pointsra[kk])
            passeddec.append(pointsdec[kk])

    #if countwhile % 2 == 0 and countwhile != 0:
    if countwhile>5:
        c=c+2
    elif countwhile>10:
        c=c+5
    else:
        c = c + 0.5

    print('nono 1')
    return phis, thetas, timearrs, kks, scanned_ra, scanned_dec,scanned_pix,scanned_time, passedra, passeddec,is_here,countwhile,kk,tempdis, c,labels,y,flag,change_is_here

