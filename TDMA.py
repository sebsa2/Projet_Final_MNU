# -*- coding: utf-8 -*-
"""
TDMA Algortihm
"""

import numpy as np

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
    
    P = np.empty_like(a)
    Q = np.empty_like(a)
    f = np.empty_like(a)
    
    P[0] = b[0] / a[0]
    Q[0] = d[0] / a[0]
    
    for i in range(1, N):
        P[i] = b[i] / (a[i] - c[i]*P[i-1])
        Q[i] = (d[i] + c[i]*Q[i-1]) / (a[i] - c[i]*P[i-1])
        
    f[N-1] = Q[N-1]
    
    for i in range(N-2, -1, -1):
        f[i] = P[i]*f[i+1] + Q[i]
        
    return f