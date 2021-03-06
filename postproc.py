#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:55 2017

@author: arnaud
"""

import matplotlib.pyplot as plt
import numpy as np
from analy import analy
from variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny, Timetot
import math

print("")

folder_path = 'out_3'
disp_analytic = True
disp_simulation = True
disp_error = True
disp_evolution = False

if disp_simulation:
    i = 9999
    Tf = np.genfromtxt(folder_path+'/output_' + str(i) + '.csv')
    
    Tf = Tf.transpose()
    
    X = np.arange(Tf.shape[0]) / Nx * Lx
    Y = np.arange(Tf.shape[1]) / Ny * Ly
    
    
    fig, ax1 = plt.subplots(figsize=(8,6))
    
    im = ax1.pcolormesh(Y,X,Tf)
    im2 = ax1.contour(Y,X,Tf, colors="k")
    plt.clabel(im2, inline=1, fontsize=10)
    zou = fig.colorbar(im)
    zou.ax.set_ylabel('Température en Kelvin')
    plt.title("Simulation")
    ax1.set_xlabel('x(m)')
    ax1.set_ylabel('y(m)')

#fig, ax2 = plt.subplots(figsize=(12,10))
#ax2.plot(X,Tf[2,:])

if disp_analytic:
    n = 100
    err = 0.0001
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

# Erreur finale
if disp_error:
    Erreursim = Tf - Tanaly
    fig, ax4 = plt.subplots(figsize=(8,6))
    im = ax4.pcolormesh(Y,X,Erreursim)
    im2 = ax4.contour(Y,X,Erreursim, colors="k")
    plt.clabel(im2, inline=1, fontsize=10)
    zou = fig.colorbar(im)
    zou.ax.set_ylabel('Température en Kelvin')
    plt.title("Erreur")
    ax4.set_xlabel('x(m)')
    ax4.set_ylabel('y(m)')

# Erreur en fonction des itérations
if disp_evolution:
    sz = 55001
    modulo = 500
    yerr = np.zeros(int(sz/modulo))
    count = 0
    for k in range(1,sz): # norme l2
        if k%modulo != 0 and k != sz-1:
            continue
        Temp = np.genfromtxt(folder_path+"/output_" + str(k) + ".csv").transpose()
        errtemp = Temp - Tanaly
        yerr[count] = math.sqrt(np.sum(np.square(errtemp)))
        count += 1
    
    xerr = np.arange(len(yerr)) / (len(yerr) -1) * Timetot
    fig, ax5 = plt.subplots(figsize=(8,6))
    ax5.plot(xerr,yerr)

