import numpy as np
from eos import *
from structure import *
import astro_const as ac
import matplotlib.pyplot as plt
from routine import *
from IPython.display import HTML
import time

start = time.time()

M = ac.Msun*np.arange(.1,1.1,.1)
mue = ac.WD_mue

delta_m = 0.01 
xi = 0.01
eta = 1e-10
max_steps = 10000

output = np.zeros((len(M),6))

for m in range(len(M)):
    Pc_final = find_Pc(M[m], delta_m, eta, xi, mue, max_steps)
    mass,radius,pressure = integrate(Pc_final,delta_m,eta,xi,mue, max_steps)
    #Save Information in Output array
    output[m,0] = mass[-1]/ac.Msun
    output[m,1] = radius[-1]/ac.Rsun
    output[m,2] = pressure[0]
    output[m,3] = pressure[0]/(ac.G*mass[-1]**2 * radius[-1]**(-4))
    output[m,4] = density(pressure[0],mue)
    output[m,5] = density(pressure[0],mue)/ (3*mass[-1]/(4*np.pi*radius[-1]**3))

print("Saved Mass Radius Ration Graph as mass_radius_ratio.png")
plot_observations(output)
print("Output Table in HTML format")
print(create_html_table(output))

end = time.time()
print("This took", (end-start)/60, "minutes to run")
