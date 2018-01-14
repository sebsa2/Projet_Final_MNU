#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:10:31 2018

@author: arnaud
"""

#import matplotlib.pyplot as plt
from math import tan, pi, cos, cosh
import numpy as np
#from variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny

def analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=10, err=0.001):
    beta = h/lamb
    
    alpha = np.empty(n)
    
    mysum = np.zeros((Ny, Nx))
    x = np.arange(Nx)
    y = np.arange(Ny)
    T = np.empty((Ny, Nx))
    
    for k in range(n):
        mini = 2*k*pi / Lx
        maxi = (2*k+1)*pi / Lx # maxi = mini + alpha[k-1]
        
        alpha[k] = dicho(mini, maxi, beta, err, Lx)
        denom = ((alpha[k]*alpha[k]+beta*beta)*Lx + beta) * cos(alpha[k]*Lx) * cosh(alpha[k]*Ly)
        
        for i in x:
            for j in y:
                mysum[j,i] += (cos(alpha[k]*(i*Lx/Nx)) * cosh(alpha[k]*(Ly-(j*Ly/Ny)))) / denom
    
    T[:,:] = Ta + 2*beta * (T1 - Ta) * mysum[:,:]
    
    return T, mysum
    
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
        if count >= 100:
            break
    return var
