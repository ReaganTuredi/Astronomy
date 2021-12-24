import numpy as np
import astro_const as ac

def mean_molecular_weight(Z,A,X):
    Zs = np.array(Z)
    As = np.array(A)
    Xs = np.array(X)
    
    mu = np.sum(Xs*(Zs+1)/As)**(-1) 
    return mu
    
def get_rho_and_T(P,P_c,rho_c,T_c):
    
    rho = rho_c*(P/P_c)**(1/ac.gamma)
    T = T_c*(P/P_c)**(1-1/ac.gamma)

    return rho, T
