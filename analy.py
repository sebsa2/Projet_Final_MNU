#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:10:31 2018

@author: arnaud
"""

from math import tan, pi, cos, cosh
import numpy as np

def analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=10, err=0.001):
    beta = h/lamb
    
    alpha = np.empty(n)
    
    mysum = np.zeros((Nx, Ny))
    x = np.arange(Nx)
    y = np.arange(Ny)
    T = np.empty((Nx, Ny))
    
    for k in range(n):
        mini = 2*k*pi
        maxi = (2*k+1)*pi # maxi = mini + alpha[k-1]
        
        alpha[k] = dicho(mini, maxi, beta, err, Lx)
        denom = ((alpha[k]*alpha[k]+beta*beta)*Lx + beta) * cos(alpha[k]*Lx) * cosh(alpha[k]*Ly)
        print(denom)
        
        for i in x:
            for j in y:
                mysum[i,j] += (cos(alpha[k]*(i*Lx/Nx)) * cosh(alpha[k]*(Ly-(j*Ly/Ny)))) / denom
    
    T[:,:] = Ta + 2*beta * (T1 - Ta) * mysum[:,:]
    
    return T, mysum
    
def dicho(mini, maxi, beta, err, Lx):
    var = (maxi+mini)/2
    
    test = var * tan(Lx * var) - beta
    
    if test < err:
        return var
    
    if test < 0:
        return dicho(mini, var, beta, err, Lx)
    else:
        return dicho(var, maxi, beta, err, Lx)
    
Tanaly, mysum = analy(400, 200, 100, 386, 1, 1, 10, 10, n=3)
