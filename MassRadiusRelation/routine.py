import numpy as np
import astro_const as ac
from eos import *
from structure import *
from scipy.optimize import bisect
from IPython.display import HTML
import matplotlib.pyplot as plt
from observations import MassRadiusObservations


def error_function(Pc, M_want, delta_m, eta, xi, mue, max_steps=10000):

    mass,radius,pressure = integrate(Pc,delta_m,eta,xi,mue, max_steps)
    error = mass[-1] - M_want
    return error

def find_Pc(M_want, delta_m, eta, xi, mue, max_steps):
    Pc_low = 1e-3*pressure_guess(M_want, mue)
    Pc_high = pressure_guess(M_want, mue)
    final_Pc = bisect(error_function, Pc_low, Pc_high, args = (M_want,delta_m,eta,xi,mue, max_steps))
    return final_Pc


def create_html_table(output):

    table = """<table><tr><th>M / M<sub>&#9737</sub> </th><th>R / R<sub>&#9737</sub> </th><th>P<sub>c</sub> (N/m<sup>2</sup>)</th><th>P<sub>c</sub> / (GM<sup>2</sup>R<sup>-4</sup>) </th><th> &#961 <sub>c</sub> (kg/m<sup>3</sup>)</th><th> &#961 <sub>c</sub> / [ 3M / (4 &#960 R<sup>3</sup>) ] </th></tr>"""
    for i in range(output.shape[0]):
        table += "<tr>"
        for j in range(output.shape[1]):
            table += "<td> {:.3e} </td>".format(output[i,j])
        table += "</tr>"

    return table

def plot_observations(output):
    obs = MassRadiusObservations()
    plt.figure()
    plt.errorbar(obs.masses, 0.01*obs.radii, yerr = 0.01*obs.radius_errors, fmt = "bo", label = "Observations")
    plt.plot(output[:,0], output[:,1], "r", label = "Mass-Radius Ratio")
    plt.xlabel(r"M/M$_\odot$")
    plt.ylabel(r"R/R$_\odot$")
    plt.title("Mass to Radius Relation")
    plt.legend()
    plt.savefig("mass_ratio_ratio")
