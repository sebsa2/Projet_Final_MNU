#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:55 2017

@author: arnaud
"""

import matplotlib.pyplot as plt
import numpy as np
from analy import analy
from err_tempo_0.variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny, dt, Timetot
import math

folder_path = 'err_tempo_0'

i = 55500
Tf = np.genfromtxt(folder_path+'/output_' + str(i) + '.csv')

Tf = Tf.transpose()

X = np.arange(Tf.shape[0]) / Nx * Lx
Y = np.arange(Tf.shape[1]) / Ny * Ly


fig, ax1 = plt.subplots(figsize=(8,6))

im = ax1.pcolormesh(X,Y,Tf)
im2 = ax1.contour(X,Y,Tf, colors="k")
zou = fig.colorbar(im)
zou.ax.set_ylabel('Température en Kelvin')
plt.title("Simulation")
ax1.set_xlabel('x(m)')
ax1.set_ylabel('y(m)')

#fig, ax2 = plt.subplots(figsize=(12,10))
#ax2.plot(X,Tf[2,:])

n = 100
err = 0.0001
Tanaly = analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=n, err=err)
X = np.arange(Tanaly.shape[0]) / Nx * Lx
Y = np.arange(Tanaly.shape[1]) / Ny * Ly


fig, ax3 = plt.subplots(figsize=(8,6))

im = ax3.pcolormesh(X,Y,Tanaly)
im2 = ax3.contour(X,Y,Tanaly, colors="k")
zou = fig.colorbar(im)
zou.ax.set_ylabel('Température en Kelvin')
plt.title("Analytic")
ax3.set_xlabel('x(m)')
ax3.set_ylabel('y(m)')

# Erreur finale
Erreursim = Tf - Tanaly
fig, ax4 = plt.subplots(figsize=(8,6))
im = ax4.pcolormesh(X,Y,Erreursim)
im2 = ax4.contour(X,Y,Erreursim, colors="k")
zou = fig.colorbar(im)
zou.ax.set_ylabel('Température en Kelvin')
plt.title("Erreur")
ax4.set_xlabel('x(m)')
ax4.set_ylabel('y(m)')

# Erreur en fonction des itérations
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

