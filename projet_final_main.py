# -*- coding: utf-8 -*-
"""
Projet MNU main
"""

import os
import numpy as np
from TDMA import TDMA
from variables import T0,Ta,T1,h, lamb, Nx,Ny,dx, N, Fx,Fy


for i in range(15):
    folder_path = 'err_tempo_{0}'.format(i)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        break

# Temperature
Ti = np.empty((Nx,Ny))
Tf = np.empty((Nx,Ny))
Tinter = np.empty_like(Ti)

# Condition intiale
Ti[:,:] = T0

# Condition aux limites y=0
Ti[:,0] = T1
Tinter[:,0] = T1

# Skip unnecessary write of files
skip_write_inter = True
skip_modulo = 500


print('Fx=',Fx)
print('Fy=',Fy)

for n in range(1,N):
#    print("")
#    print("Time:",n)
    
    for j in range(1,Ny):
#        print("Selon Y:",j)
        a = np.empty(Nx)
        b = np.empty(Nx)
        c = np.empty(Nx)
        d = np.empty(Nx)
        
        if j==0:
            a[:] = 1
            b[:] = 0
            c[:] = 0
            d[:] = T1
            
        elif j==Ny-1:
            a[0:Nx-1] = 1+Fx
            a[Nx-1] = 1+Fx+Fx*dx*h/lamb
            b[0] = Fx
            b[1:Nx-1] = Fx/2
            b[Nx-1] = 0
            c[0] = 0
            c[1:Nx-1] = Fx/2
            c[Nx-1] = Fx
            d[0:Nx-1] = Ti[0:Nx-1,j]*(1-Fy) + Fy*(Ti[0:Nx-1,j-1])
            d[Nx-1] = Ti[Nx-1,j]*(1-Fy) + Fy*(Ti[Nx-1,j-1]) + Fx*Ta*dx*h/lamb
            
        else:
            a[0:Nx-1] = 1+Fx
            a[Nx-1] = 1+Fx+Fx*dx*h/lamb
            b[0] = Fx
            b[1:Nx-1] = Fx/2
            b[Nx-1] = 0
            c[0] = 0
            c[1:Nx-1] = Fx/2
            c[Nx-1] = Fx
            d[0:Nx-1] = Ti[0:Nx-1,j]*(1-Fy) + Fy/2*(Ti[0:Nx-1,j+1]+Ti[0:Nx-1,j-1])
            d[Nx-1] = Ti[Nx-1,j]*(1-Fy) + Fy/2*(Ti[Nx-1,j+1]+Ti[Nx-1,j-1]) + Fx*Ta*dx*h/lamb
        
        Tinter[:,j] = TDMA(a,b,c,d)
        
    if not skip_write_inter:
        np.savetxt(folder_path+'/inter_'+str(n)+'.csv', Tinter)

    for i in range(Nx):
#        print("Selon X:",i)
        a = np.empty(Ny)
        b = np.empty(Ny)
        c = np.empty(Ny)
        d = np.empty(Ny)
        
        if i==0:
            a[0] = 1
            a[1:Ny] = 1+Fy
            b[0] = 0
            b[1:Ny-1] = Fy/2
            b[Ny-1] = 0
            c[0] = 0
            c[1:Ny-1] = Fy/2
            c[Ny-1] = Fy
            d[0] = T1
            d[1:Ny] = Tinter[i,1:Ny]*(1-Fx) + Fx*Tinter[i+1,1:Ny]
            
        elif i==Nx-1:
            a[0] = 1
            a[1:Ny] = 1+Fy
            b[0] = 0
            b[1:Ny-1] = Fy/2
            b[Ny-1] = 0
            c[0] = 0
            c[1:Ny-1] = Fy/2
            c[Ny-1] = Fy
            d[0] = T1
            d[1:Ny] = Tinter[i,1:Ny]*(1-Fx-Fx*dx*h/lamb) + Fx*dx*h*Ta/lamb + Fx*Tinter[i-1,1:Ny]
            
        else:
            a[0] = 1
            a[1:Ny] = 1+Fy
            b[0] = 0
            b[1:Ny-1] = Fy/2
            b[Ny-1] = 0
            c[0] = 0
            c[1:Ny-1] = Fy/2
            c[Ny-1] = Fy
            d[0] = T1
            d[1:Ny] = Tinter[i,1:Ny]*(1-Fx) + Fx/2*(Tinter[i+1,1:Ny]+Tinter[i-1,1:Ny])
        
        Tf[i,:] = TDMA(a,b,c,d)
        
    Ti = Tf
    
    if n%skip_modulo == 0:
        np.savetxt(folder_path+'/output_'+str(n)+'.csv', Ti)
        
# Save the last occurence anyway
if n%skip_modulo != 0:
    np.savetxt(folder_path+"/output_" + str(n) +  ".csv", Ti)
    
print("Computation terminated.")
        
        
        
        
        
        
        
        