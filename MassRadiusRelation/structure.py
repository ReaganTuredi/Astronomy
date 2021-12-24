import numpy as np
from numpy.linalg import norm
from eos import *
from ode import rk4
from astro_const import *

def stellar_derivatives(m,z,mue):
    r = z[0]
    P = z[1]
    rho = density(P,mue)

    dzdm = np.zeros_like(z)
    dzdm[0] = 1/(4*np.pi*r**2 *rho)
    dzdm[1] = -ac.G*m/(4*np.pi*r**4)
    
    return dzdm

def central_values(Pc,delta_m,mue):
    z = np.zeros(2)
    rho_c = density(Pc,mue)
    r  = (3*delta_m/ (4*np.pi*rho_c))**(1/3) 
    
    z[0] = r
    z[1] = Pc
    return z
    
def lengthscales(m,z,mue):
    r = z[0]
    P = z[1]
    rho = density(P,mue)
    
    z_dzdm = np.zeros_like(z)
    
    Hr = 4*np.pi*r**3 *rho                     
    Hp = 4*np.pi*r**4 * P / (ac.G*m)    

    z_dzdm[0] = Hr
    z_dzdm[1] = Hp

    return z_dzdm
    
def integrate(Pc,delta_m,eta,xi,mue,max_steps=10000):
        
    m_step = np.zeros(max_steps)
    r_step = np.zeros(max_steps)
    p_step = np.zeros(max_steps)
    
    z = central_values(Pc,delta_m,mue)
    m_step[0] = delta_m

    Nsteps = 0
    for step in range(max_steps-1):
        radius = z[0]
        pressure = z[1]
        if (pressure < eta*Pc):
            break
        r_step[step] = radius
        p_step[step] = pressure

        h = xi*min(lengthscales(m_step[step],z,mue))

        znew = rk4(stellar_derivatives,m_step[step],z,h,args=(mue))
        
        Nsteps += 1
        m_step[step+1] = m_step[step] + h
        z = np.copy(znew) 


    if Nsteps < max_steps:
        pass
    else:
        raise Exception('too many iterations')
        
    return m_step[0:Nsteps],r_step[0:Nsteps],p_step[0:Nsteps]

def pressure_guess(m,mue):
    Pguess = ac.G**5/ac.Ke**4  * (m*mue**2)**(10/3)

    return Pguess
