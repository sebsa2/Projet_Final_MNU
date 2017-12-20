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

# Materiau : cuivre pur par exemple
lamb = 386 # W.m^-1.K^-1
cp = 385 # J.kg^-1.K^-1
rho = 8960 # kg.m^-3
diff = lamb / (rho*cp) # m^2.s^-1 # Variable a déjà prise plus loin

# Géométrie
Lx = 1
Ly = 1
Nx = 15
Ny = Nx
dx = Lx/Nx
dy = Ly/Ny

# Temps
Timetot = 1
N = 4
dt = Timetot/N

# Nombres de Fourier
Fx = diff*dt/dx**2
Fy = diff*dt/dy**2

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
    print("")
    print("Time:",n)
    
    for j in range(1,Ny):
        print("Selon Y:",j)
        a = np.ones(Nx)*(1+Fx)
        b = np.empty(Nx)
        c = np.empty(Nx)
        d = np.empty(Nx)
        
        b[0] = -Fx
        b[1:Nx-1] = -Fx/2
        b[Nx-1] = 0
        
        c[0] = 0
        c[1:Nx-1] = -Fx/2
        c[Nx-1] = -Fx/2 * (1 + 1/(2*dx*h+lamb))
        
        if j!=Ny-1:
            d[:] = Ti[:,j]*(1-Fy) + Fy/2 * (Ti[:,j+1]+Ti[:,j-1])   
        else:    
            d[:] = Ti[:,j]*(1-Fy) + Fy*Ti[:,j-1]
        d[Nx-1] += Fx * dx*h*Ta / (2*dx*h+lamb)
        
        Tinter[:,j] = TDMA(a,b,c,d)
        
    np.savetxt('out/inter_'+str(n)+'.csv', Tinter)

    for i in range(Nx):
        print("Selon X:",i)
        a = np.ones(Ny)*(1+Fy)
        b = np.empty(Ny)
        c = np.empty(Ny)
        d = np.empty(Ny)
        
        a[0] = 1
        
        b[0] = 0
        b[1:Ny-1] = -Fy/2
        b[Ny-1] = 0
        
        c[0] = 0
        c[1:Ny-1] = -Fy/2
        c[Ny-1] = -Fy
        
        # TODO: Il me semble que l'erreur soit située dans le d
        if i==0:
            d[:] = Tinter[i,:]*(1-Fx) + Fx*Tinter[i+1,:]
        elif i==Nx-1:
#            d[:] = Tinter[i,:]*(1-Fx) + Fx/2*( (1+lamb/(2*dx*h+lamb))*Tinter[i-1,:]) + Fx*dx*h*Ta/(2*dx*h+lamb)
            d[:] = Tinter[i,:]*(1-Fx+Fx*dx*h/lamb) + Tinter[i-1,:]*Fx - Fx*dx*h*Ta/lamb
        else:
            d[:] = Tinter[i,:]*(1-Fx) + Fx/2*(Tinter[i+1,:]+Tinter[i-1,:])
        d[0] = T1
        
        Tf[i,:] = TDMA(a,b,c,d)
        
    Ti = Tf
    
    np.savetxt('out/output_'+str(n)+'.csv', Ti)
        
        
        
        
        
        
        
        
        