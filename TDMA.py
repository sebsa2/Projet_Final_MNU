# -*- coding: utf-8 -*-
"""
TDMA Algortihm
"""

import numpy as np
Tmax = 500
Tmin = 280

def TDMA(a,b,c,d):
    """
    Returns output of TDMA algorithm
    
    Parameters
        a,b,c,d : arrays-like size N
    
    Returns
        1D-array
    """
    
    N = len(a)
    
    # Vérifier que q,b,c,d ont tous la même taille
    if len(b)!=N or len(c)!=N or len(d)!=N:
        raise Exception("TDMA algorithm must receive four same-length arrays.")
    
    P = np.empty_like(a)
    Q = np.empty_like(a)
    f = np.empty_like(a)
    
    P[0] = b[0] / a[0]
    Q[0] = d[0] / a[0]
    
    for i in range(1, N):
        P[i] = b[i] / (a[i] - c[i]*P[i-1])
        Q[i] = (d[i] + c[i]*Q[i-1]) / (a[i] - c[i]*P[i-1])
        
    f[N-1] = Q[N-1] # Problem usually occurs right here, Q[N-1] is below Tmin
    
    for i in range(N-2, -1, -1):
        f[i] = P[i]*f[i+1] + Q[i]
        if f[i]>Tmax or f[i]<Tmin:
            print("i:",i)
            print("f[i]:",f[i], " P[i]:",P[i], " f[i+1]:",f[i+1], " Q[i]:",Q[i])
            print("a[i]:", a[i], " b[i]:", b[i], " c[i]:", c[i], " d[i]:", d[i])
            
            print("")
            print("Comparison with previous i:")
            i+=1
            
            print("i:",i)
            print("f[i]:",f[i], " P[i]:",P[i], " Q[i]:",Q[i])
            print("a[i]:", a[i], " b[i]:", b[i], " c[i]:", c[i], " d[i]:", d[i])
            
            print("")
            print(a)
            print(b)
            print(c)
            print(d)
            raise Exception("Temperature out of range.")
        
    return f
