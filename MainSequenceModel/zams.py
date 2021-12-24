import numpy as np
from astro_const import fourpi, sigmaSB

def Teff(Mwant):
    masses = np.array([0.1,0.15,0.2,0.3]) 
    Teffs = np.array([2800.0,3150.0,3300.0,3400.0]) 
    Teff_want = np.interp(Mwant, masses, Teffs)
    return Teff_want

def surface_luminosity(Teff,radius):
    luminosity = fourpi*radius**2 *sigmaSB*Teff**4
    return luminosity
