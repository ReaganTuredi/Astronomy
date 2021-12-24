from structure import integrate
from zams import Teff, surface_luminosity
from scipy.optimize import brentq
from astro_const import *
import matplotlib.pyplot as plt
import numpy as np

def lum_error(Rguess, Mwant, delta_m, eta, xi, mu, XH, pp_factor, max_steps = 10000):
   
    mass,radius,pressure,Luminosity = integrate(Mwant, Rguess, delta_m, eta, xi, mu, XH, pp_factor, max_steps=10000)
    L_nuc = Luminosity[-1]
    
    Teff_want = Teff(Mwant)
    L_calc = surface_luminosity(Teff_want, Rguess)
    error = L_nuc - L_calc

    return error

def find_R(Mwant, delta_m, eta, xi, mu, XH, pp_factor, max_steps = 10000):
   
    R_low = Mwant*Rsun/2
    R_high = Mwant*Rsun*2
    final_R = brentq(lum_error, R_low, R_high, args = (Mwant, delta_m, eta, xi, mu, XH, pp_factor, max_steps))
    return final_R

def LT_plot(Luminosity, Temp):
    plt.figure()
    plt.plot(Temp,Luminosity/Lsun)
    plt.yscale("log")
    plt.xscale("log")
    plt.xlim([3.5*10**3,2.7*10**3])
    plt.yticks(np.arange(1,11,1)*10**(-3))
    plt.xticks(np.arange(2.7,3.6,0.1)*10**3, rotation=20)
    plt.title("Luminosity as a function of Effective Temperature")
    plt.xlabel(r"log(T$_{eff}$/K)")
    plt.ylabel(r"log(L/L$_\odot$)")
    plt.savefig("lum_teff_plot")

def rhoT_plot(density, Temp):

    rho = density*0.001 
    plt.figure()
    plt.plot(rho, Temp)
    plt.yscale("log")
    plt.xscale("log")
    plt.title("Central Temperature as a function of Central Density")
    plt.ylabel(r"log(T$_{c}$/K)")
    plt.xlabel(r"log($\rho/gcm^{-3}$)")
    plt.savefig("tc_rhoc_plot")


def plot_LT_over_mr(Mass, Radius, Temperature, Luminosity):
    fig, ax = plt.subplots(2,2)
    ax[0,0].plot(Mass/Mass[-1], Temperature/np.max(Temperature))
    ax[0,0].set_title("Temperature as a \n funtion of Mass")
    ax[0,0].set_xlabel("Fraction of Mass")
    ax[0,0].set_ylabel("Fraction of Temperature")

    ax[1,0].plot(Mass/Mass[-1], Luminosity/Luminosity[-1])
    ax[1,0].set_title("Luminosity as a \n funtion of Mass")
    ax[1,0].set_xlabel("Fraction of Mass")
    ax[1,0].set_ylabel("Fraction of Luminosity")

    ax[0,1].plot(Radius/Radius[-1], Temperature/np.max(Temperature))
    ax[0,1].set_title("Temperature as a \n funtion of Radius")
    ax[0,1].set_xlabel("Fraction of Radius")
    ax[0,1].set_ylabel("Fraction of Temperature")

    ax[1,1].plot(Radius/Radius[-1], Luminosity/Luminosity[-1])
    ax[1,1].set_title("Luminosity as a \n funtion of Radius")
    ax[1,1].set_xlabel("Fraction of Radius")
    ax[1,1].set_ylabel("Fraction of Luminosity")

    plt.tight_layout()
    plt.savefig("LT_MR_plot")
