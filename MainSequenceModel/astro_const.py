import astropy.constants as _ac
import astropy.units as _au

from numpy import pi
fourpi = 4.0*pi

Msun = _ac.M_sun.value
Rsun = _ac.R_sun.value
Lsun = _ac.L_sun.value

pc = _ac.pc.value
au = _ac.au.value
year = _au.year.to(_au.second)

G = _ac.G.value
h = _ac.h.value
hbar = _ac.hbar.value
m_e = _ac.m_e.value
m_p = _ac.m_p.value
m_n = _ac.m_n.value
m_u = _ac.u.value
c = _ac.c.value
kB = _ac.k_B.value
sigmaSB = _ac.sigma_sb.value
gamma = 5/3

def print_constants():
    constants = [
        ("solar mass",Msun,"kg"),
        ("solar radius",Rsun,"m"),
        ("solar luminosity",Lsun,"W"),
        ("parsec",pc,"m"),
        ("astronomical unit",au,"m"),
        ("year",year,"s"),
        ("gravitational constant",G,"m**3 s**-2 kg**-1"),
        ("Planck constant",h,"J s"),
        ("Planck constant, reduced",hbar,"J s"),
        ("electron mass",m_e,"kg"),
        ("proton mass",m_p,"kg"),
        ("neutron mass",m_n,"kg"),
        ("atomic mass unit",m_u,"kg"),
        ("speed of light",c,"m s**-1"),
        ("Boltzmann constant",kB,"J K**-1"),
        ("Stefan-Boltzmann constant",sigmaSB,"W m**-2 K**-4"),
        ("Adiabatic Index for an Ideal Monatomic Gas", gamma, "unite-less")
    ]
    for const in constants:
        print('{0[0]:28} = {0[1]:23.16e} {0[2]}'.format(const))
