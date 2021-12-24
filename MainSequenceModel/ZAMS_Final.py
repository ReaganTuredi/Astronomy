from routine import find_R, lum_error, plot_LT_over_mr, LT_plot, rhoT_plot
from structure import integrate, central_thermal
from eos import mean_molecular_weight, get_rho_and_T
from zams import Teff
from astro_const import *
import numpy as np
import time

start = time.time()
M = np.linspace(0.1,0.3, 10) 

Z = np.array([1,2,7]) 
A = np.array([1,4,14])
X = np.array([0.706, 0.275, 0.019])
mu = mean_molecular_weight(Z,A,X)

XH = 0.706
pp_factor = 1
delta_m = 0.01
eta = 1e-10
xi = 0.01
max_steps = 10000

output = np.zeros((len(M), 4))

for m in range(len(M)):
    final_R = find_R(M[m], delta_m, eta, xi, mu, XH, pp_factor, max_steps)
    mass, radius, pressure, luminosity = integrate(M[m], final_R, delta_m, eta, xi, mu, XH, pp_factor, max_steps)
    Pc, rhoc, Tc = central_thermal(M[m],final_R/Rsun,mu)
    output[m,0] = luminosity[-1]
    output[m,1] = Teff(M[m])    
    output[m,2] = Tc            
    output[m,3] = rhoc           

    if M[m] == 0.3:
        rho, temp = get_rho_and_T(pressure,Pc,rhoc,Tc)
        plot_LT_over_mr(mass, radius, temp, luminosity)

end = time.time()
print("This took",(end-start)/60, "minutes")

LT_plot(output[:,0], output[:,1])
rhoT_plot(output[:,3], output[:,2])
