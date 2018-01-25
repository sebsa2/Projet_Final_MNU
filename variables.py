#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:11:27 2018

@author: arnaud
"""

# Conditions exterieures
T0 = 300
Ta = 250
T1 = 400
h = 1000

# Materiau : cuivre pur par exemple
lamb = 386 # W.m^-1.K^-1
cp = 385 # J.kg^-1.K^-1
rho = 8960 # kg.m^-3
diff = lamb / (rho*cp) # m^2.s^-1 # Variable a déjà prise plus loin

# Géométrie
Lx = 1
Ly = 1
Nx = 50
Ny = 50
dx = Lx/Nx
dy = Ly/Ny

# Temps
Timetot = 10000
N = 5000
dt = Timetot/N

# Nombres de Fourier
Fx = diff*dt/dx**2
Fy = diff*dt/dy**2
