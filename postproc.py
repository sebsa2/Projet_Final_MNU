#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:55 2017

@author: arnaud
"""

import matplotlib.pyplot as plt
import numpy as np

Tf = np.genfromtxt('out/output_1.csv')

X = np.arange(Tf.shape[0])
Y = np.arange(Tf.shape[1])


fig, ax = plt.subplots()

im = ax.pcolormesh(X,Y,Tf)
fig.colorbar(im)
