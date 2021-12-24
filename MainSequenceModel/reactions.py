import numpy as np

def pp_rate(T,rho,XH,pp_factor=1.0):
   
    T9 = T/10**9 
    rate = (2.4*10**(-3)*rho*XH**2)/(T9**(2/3))*np.exp(-3.380/(T9**(1/3))) 
    return rate*pp_factor
