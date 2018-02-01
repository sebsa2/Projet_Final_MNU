#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:40:46 2018

@author: arnaud
"""

# Error function of mesh size
# Results are stored in Chalpha folder
# We need to compute each error for these results, then plot the error function of mesh size

import os
import numpy as np
import re
import math
import matplotlib.pyplot as plt
from analy import analy
from variables import T1, Ta, h, lamb, Lx, Ly, Nx, Ny

folder = "Chalpha"
listfile = os.listdir(folder)

sz = []
temperatures = []
sims = []
errs = []

for file in listfile:
    # Get mesh size
    m = re.search("Nx([0-9]+)\.csv", file)
    if m:
        size = int(m.group(1))
    else:
        raise Exception("Wrong filename for : ", file)
    sz.append(size)
    
    # Compute analytic solution
    T = analy(T1, Ta, h, lamb, Lx, Ly, size, size)
    sims.append(T)
    
    # Get computed result from file
    temp = np.genfromtxt(folder + "/" + file)
    temperatures.append(temp)
    
    # Compute error (L2)
    err = math.sqrt(np.sum(np.square(temp - T))/size**2)
    errs.append(err)

# Plot error function of mesh
plt.plot(sz, errs, "ob")


