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
Nx = 10
Ny = 10
dx = Lx/Nx
dy = Ly/Ny

# Temps
Timetot = 1
N = 10
dt = Timetot/N

# Nombres de Fourier
Fx = a*dt/dx**2
Fy = a*dt/dy**2

# Temperature
Ti = np.empty((Nx,Ny))
Tf = np.empty((Nx,Ny))
Tinter = np.empty_like(Ti)

# Condition intiale
Ti[:,:] = T0

# Condition aux limites y=0
Ti[:,0] = T1
Tinter[:,0] = T1

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
            d[:] = Ti[:,j] + Fy/2 * (Ti[:,j+1]-2*Ti[:,j]+Ti[:,j-1])   
        else:    
            d[:] = Ti[:,j] + Fy/2 * 2*(-Ti[:,j]+Ti[:,j-1])  
        d[Nx-1] += Fx * dx*h*Ta / (2*dx*h+lamb)
        
        Tinter[:,j] = TDMA(a,b,c,d)
        
    for i in range(Nx):
        a = np.ones(Ny)*(1+Fy)
        b = np.empty(Ny)
        c = np.empty(Ny)
        d = np.empty(Ny)
        
        a[0] = 1
        
        b[0] = 0
        b[1:Ny-2] = -Fy/2
        b[Ny-1] = 0
        
        c[0] = 0
        c[1:Ny-2] = -Fy/2
        c[Ny-1] = -Fy
        
        if i==0:
            d[:] = Tinter[i,:] + Fx*(Tinter[i+1,:]-Tinter[i,:])
        elif i==Nx-1:
            d[:] = Tinter[i,:] + Fx/2*( (1+lamb/(2*dx*h+lamb))*Tinter[i-1,:] - 2*Tinter[i,:]) + Fx*dx*h*Ta/(2*dx*h+lamb)
        else:
            d[:] = Tinter[i,:] + Fx/2*(Tinter[i+1,:]-2*Tinter[i,:]+Tinter[i-1,:])
        d[0] = T1
        
        Tf[i,:] = TDMA(a,b,c,d)
        
    Ti = Tf
    
    np.savetxt('out/output_'+str(n)+'.csv', Ti)
        
        
        
        
        
        
        
        
        