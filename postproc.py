#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:55 2017

@author: arnaud
"""

import matplotlib.pyplot as plt
import numpy as np
from analy import analy
from variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny

i = 99
Tf = np.genfromtxt('out/output_' + str(i) + '.csv')

Tf = Tf.transpose()

X = np.arange(Tf.shape[0]) / Nx * Lx
Y = np.arange(Tf.shape[1]) / Ny * Ly


fig, ax1 = plt.subplots(figsize=(12,10))

im = ax1.pcolormesh(X,Y,Tf)
fig.colorbar(im)
plt.title("Simulation")

#fig, ax2 = plt.subplots(figsize=(12,10))
#ax2.plot(X,Tf[2,:])

n = 100
err = 0.0001
Tanaly = analy(T1, Ta, h, lamb, Lx, Ly, Nx, Ny, n=n, err=err)
X = np.arange(Tanaly.shape[0]) / Nx * Lx
Y = np.arange(Tanaly.shape[1]) / Ny * Ly


fig, ax3 = plt.subplots(figsize=(12,10))

im = ax3.pcolormesh(X,Y,Tanaly)
fig.colorbar(im)
plt.title("Analytic")

