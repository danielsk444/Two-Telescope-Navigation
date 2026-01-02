import matplotlib.pyplot as plt
import numpy as np


def path(tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,turn_points_ra,turn_points_dec):
    #print('1,',tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j)
    #plt.plot(2, 2)
    #plt.show()
    j = j + 1
    #if isinstance(tele, tele_deg):
        #time, flag = tele.time(ra, dec, raI, decI)
        #print('ttttttt1', time)
    #if isinstance(tele, tele_acc):
    #print('ti4', ra, dec, tchange, rachange, decchange)

    #plt.plot(2, 2)
    #plt.show()
    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(ra, dec, raI, decI)
       # print('ttttttt2', time)
    #print('ti4', ra, dec, tchange, rachange, decchange)

   # plt.plot(2, 2)
    #plt.show()
    n = 20
    br = 0
    # print('ttttttt', tottime, time)
    for i in range(ii, n + ii):
        timearr[i] = ((i - ii) / n) * time
        # for j in range (0,len(tchange)):
        if j < len(tchange):
           # print('w', tchange[j], tottime + ((i - ii) / n) * time, i, j)
           # print('2,', tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j)
            #plt.plot(2, 2)
            #plt.show()
            if 0.95 * tchange[j] < tottime + ((i - ii) / n) * time < 1.05 * tchange[j]:
                #print('3,', tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j)
                #plt.plot(2, 2)
                #plt.show()
                # print('j', j)
                # print('ssss', rachange[j], decchange[j])
                o = len(phi) - 1
                while (phi[o] == 0):
                    o = o - 1
                #print('ti4', ra, dec, tchange, rachange, decchange)

                #print('time', timearr, phi, theta,timearr[o],phi[o],theta[o],o)
                #plt.plot(2, 2)
                #plt.show()
                turn_points_ra.append(phi[o])
                turn_points_dec.append(theta[o])
                tottime = tottime + timearr[i]
                ii = i
                timearr = np.append(timearr, np.zeros(i))
                theta = np.append(theta, np.zeros(i))
                phi = np.append(phi, np.zeros(i))
              #  if isinstance(tele, tele_deg):
                 #   raI, decI = tele.place(timearr[i], raI, decI, flag, ra, dec)
               # if isinstance(tele, tele_acc):
                #print('1', timearr[i])
                #print('time', time, time2)
                #plt.plot(2, 2)
                #plt.show()
                raI, decI = tele.place(timearr[i], raI, decI, flag, flago,flag2,flago2,  ra, dec, timetheta, timephi,sign,time2)
                phi, theta, timearr, i,turn_points_ra,turn_points_dec = path(tele, raI, decI, rachange[j], decchange[j], tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,turn_points_ra,turn_points_dec)
                br = 1
                # break
        if br == 1:
            break
        #if isinstance(tele,tele_deg):
        #phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, ra, dec)
       #if isinstance(tele, tele_acc):
        #print('1', timearr[i])
        #print('time', time, time2)
        #plt.plot(2, 2)
        #plt.show()
        phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, flago,flag2,flago2,  ra, dec, timetheta, timephi,sign,time2)
        timearr[i] = tottime + ((i - ii) / n) * time
        # print('arrrrrrr', timearr[i])
    #print('arrrrrrr', timearr,phi,theta )
    #plt.plot(2,2)
    #plt.show()


    return phi, theta, timearr, i,turn_points_ra,turn_points_dec
