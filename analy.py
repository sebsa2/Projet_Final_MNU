#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:10:31 2018

@author: arnaud
"""

#import matplotlib.pyplot as plt
from math import tan, pi, cos, cosh
import numpy as np
from variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny
import matplotlib.pyplot as plt
from tqdm import tqdm

def analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=10, err=0.001, test=False, test2=False):
    beta = h/lamb
    
    alpha = np.empty(n)
    
    mysum = np.zeros((Nx, Ny))
    termek = np.zeros((Nx, Ny))
    x = np.arange(Nx)
    y = np.arange(Ny)
    T = np.empty((Nx, Ny))
    
    for k in tqdm(range(n)):
        mini = k*pi / Lx
        maxi = (k+1/2)*pi / Lx # maxi = mini + alpha[k-1]
        
        alpha[k] = dicho(mini, maxi, beta, err, Lx)
        if test:
            print("Interval : [" + str(mini/pi*Lx) + "pi;" + str(maxi/pi*Lx) + "pi]")
            print("Interval : [" + str(mini) + ";" + str(maxi) + "]")
            print("alpha:" + str(alpha[k]))
            print("")
        denom = ((alpha[k]*alpha[k]+beta*beta)*Lx + beta) * cos(alpha[k]*Lx) * cosh(alpha[k]*Ly)
        
        for i in x:
            for j in y:
                termek[i,j] = (cos(alpha[k]*(i*Lx/Nx)) * cosh(alpha[k]*(Ly-(j*Ly/Ny)))) / denom
        mysum += termek
                
        # Comparaison deux termes d'affilée 
        if np.max(np.abs(termek)) < err:
#            print("Terminé avec k=",k)
            break
    
    T[:,:] = Ta + 2*beta * (T1 - Ta) * mysum[:,:]
    T = T.transpose()
    if test or test2:
        return T, mysum, alpha
    else:
        return T
    
#def dicho(mini, maxi, beta, err, Lx):
#    if mini >= maxi:
#        raise Exception("To use dichotomy, min value must be lower than max.")
#    var = (maxi+mini)/2
#    
#    test = var * tan(Lx * var) - beta
#    
#    if abs(test) < err:
#        return var
#    
#    if test > 0:
#        return dicho(mini, var, beta, err, Lx)
#    else:
#        return dicho(var, maxi, beta, err, Lx)
    
def dicho(mini, maxi, beta, err, Lx):
    if mini >= maxi:
        raise Exception("To use dichotomy, min value must be lower than max.")
        
    var = (maxi+mini)/2
    
    count = 0
        
    while (maxi - mini > err):
        count += 1
        var = (maxi+mini)/2
        
        test = var * tan(Lx * var) - beta
        
        if test > 0:
            maxi = var
        else:
            mini = var
        if count >= 10000000:
            break
    return var

if __name__ == "__main__":
    n=35
    err=0.0001
    beta = h/lamb
    test = False
    test2 = False
    disp = True
    if test or test2:
        Tanaly, mysum, alpha = analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=n, err=err, test=test, test2=test2)
    if test:
        f = np.tan(alpha * Lx)
        
        X = np.arange((n/Lx)*pi*1000) / 1000
        #Y = np.arange(2000)/1000 - 1
        
        fig = plt.plot(X, np.tan(X*Lx), X, beta/X)
        plt.plot(alpha, f, "ro")
        
        x1 = np.arange(n/Lx) * pi
        y1 = x1 * 0
        plt.plot(x1, y1, "g+")
        
        axes = plt.gca()
        axes.set_ylim([-1,1])
        plt.show()
        
        print(alpha)
        print(np.arange(len(alpha))*pi/2)
        print(alpha * np.tan(Lx * alpha) - beta)
        print(np.arange(n)*pi/2)
        
    if disp:
        Tanaly = analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=n, err=err)
        X = np.arange(Tanaly.shape[0]) / Nx * Lx
        Y = np.arange(Tanaly.shape[1]) / Ny * Ly
        
        
        fig, ax3 = plt.subplots(figsize=(8,6))
        
        im = ax3.pcolormesh(Y,X,Tanaly)
        im2 = ax3.contour(Y,X,Tanaly, colors="k")
        plt.clabel(im2, inline=1, fontsize=10)
        zou = fig.colorbar(im)
        zou.ax.set_ylabel('Température en Kelvin')
        plt.title("Analytic")
        ax3.set_xlabel('x(m)')
        ax3.set_ylabel('y(m)')

