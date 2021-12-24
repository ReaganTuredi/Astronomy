import astro_const as ac
import numpy as np

def pressure(rho, mue):
    p = ac.Ke * (rho/ mue)**(5/3)
    return p

def density(p, mue):
    rho = (p*mue**(5/3) /ac.Ke)**(3/5)
    return rho
