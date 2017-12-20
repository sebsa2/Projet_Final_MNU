# -*- coding: utf-8 -*-
"""
Projet MNU main
"""

import numpy as np
from TDMA import TDMA

# Conditions exterieures
T0 = 300
Ta = 280
T1 = 500
h = 5

# Materiau
lamb = 1
cp = 1
rho = 1
a = lamb / (rho*cp)

# Géométrie
Lx = 1
Ly = 1
Nx = 100
Ny = 100
dx = Lx/Nx
dy = Ly/Ny

# Temps
Timetot = 1
N = 100
dt = Timetot/N

# Nombres de Fourier
Fx = a*dt/dx**2
Fy = a*dt/dy**2

# Temperature
T = np.empty((N,Nx,Ny))

T[0,:,:] = T0
T[:,:,0] = T1

for n in range(1,N):
    
    for j in range(1,Ny):   
        a = np.ones(Nx)*(1+Fx)
        b = np.empty(Nx)
        c = np.empty(Nx)
        d = np.empty(Nx)
        
        b[0] = -Fx
        b[1:Nx-2] = -Fx/2
        b[Nx-1] = 0
        
        c[0] = 0
        c[1:Nx-2] = -Fx/2
        c[Nx-1] = -Fx/2 * (1 + 1/(2*dx*h+lamb))
        
        if j!=Ny-1:
            d[:] = T[n-1,:,j] + Fy/2 * (T[n-1,:,j+1]-2*T[n-1,:,j]+T[n-1,:,j-1])   
        else:    
            d[:] = T[n-1,:,j] + Fy/2 * 2*(-T[n-1,:,j]+T[n-1,:,j-1])  
        d[Nx-1] += Fx * dx*h*Ta / (2*dx*h+lamb)
        
        Tinter = np.empty_like(T[0,:,:])
        Tinter[:,j] = TDMA(a,b,c,d)
        
    for i in range(0,Nx):
        
            
        
        
        
        
        
        
        
        