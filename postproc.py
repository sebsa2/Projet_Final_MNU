#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:55 2017

@author: arnaud
"""

import matplotlib.pyplot as plt
import numpy as np

i = 99
Tf = np.genfromtxt('out/output_' + str(i) + '.csv')
Tf = Tf.transpose()

X = np.arange(Tf.shape[0])
Y = np.arange(Tf.shape[1])


fig, ax1 = plt.subplots(figsize=(12,10))

im = ax1.pcolormesh(X,Y,Tf)
fig.colorbar(im)

fig, ax2 = plt.subplots(figsize=(12,10))
ax2.plot(X,Tf[10,:])