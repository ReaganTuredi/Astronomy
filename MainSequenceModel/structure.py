import numpy as np
from eos import get_rho_and_T, mean_molecular_weight
from ode import rk4
from astro_const import G, Msun, Rsun, Lsun, kB, m_u, fourpi
from reactions import pp_rate

def central_thermal(m,r,mu):

    Pc = 0.77*G*(m*Msun)**2/(r*Rsun)**4         
    rhoc = 5.99*3*m*Msun/(fourpi*(r*Rsun)**3)   
    Tc = 0.54*(mu*m_u/kB)*(G*m*Msun/(r*Rsun))   
    
    return Pc, rhoc, Tc

def stellar_derivatives(m, z, Mwant, Rguess, mu, XH, pp_factor):

    r = z[0]
    P = z[1]
    L = z[2]
    Pc, rhoc, Tc = central_thermal(Mwant,Rguess/Rsun,mu)
    rho, T  = get_rho_and_T(P,Pc, rhoc, Tc)

    dzdm = np.zeros_like(z)

    dzdm[0] =  1/(fourpi*r**2 *rho)          
    dzdm[1] =  -G*m/(fourpi*r**4)            
    dzdm[2] =  pp_rate(T, rho, XH, pp_factor) 

    return dzdm

def central_values(Mwant, R_guess, delta_m, mu, XH, pp_factor):

    z = np.zeros(3)
    Pc, rhoc, Tc = central_thermal(Mwant,R_guess/Rsun,mu)

    z[0] = (3*delta_m/(fourpi*rhoc))**(1/3)
    z[1] = Pc
    z[2] = pp_rate(Tc, rhoc, XH, pp_factor)*delta_m
    return z


def lengthscales(Mwant, Rguess, m, z, mu, XH, pp_factor):

    z_dzdm = np.zeros_like(z)
    r = z[0]
    P = z[1]
    L = z[2]

    Pc, rhoc, Tc = central_thermal(Mwant,Rguess/Rsun,mu)
    rho, T  = get_rho_and_T(P,Pc, rhoc, Tc)
    
    z_dzdm[0] = fourpi*r**3 *rho
    z_dzdm[1] = fourpi*r**4 *P / (G*m)
    z_dzdm[2] = L/pp_rate(T, rho, XH, pp_factor)

    return z_dzdm

def integrate(Mwant, R_guess, delta_m, eta, xi, mu, XH, pp_factor, max_steps=10000):

    m_step = np.zeros(max_steps)
    r_step = np.zeros(max_steps)
    p_step = np.zeros(max_steps)
    L_step = np.zeros(max_steps)
     
    z = central_values(Mwant, R_guess, delta_m, mu, XH, pp_factor)
    m_step[0] = delta_m
    Pc, rhoc, Tc = central_thermal(Mwant,R_guess/Rsun,mu)

    Nsteps = 0
    for step in range(max_steps-1):
        radius = z[0]
        pressure = z[1]
        luminosity = z[2]
        if pressure < eta*Pc:
            break
        r_step[step] = radius
        p_step[step] = pressure
        L_step[step] = luminosity
        h = xi*min(lengthscales(Mwant, R_guess, m_step[step], z, mu, XH, pp_factor))

        znew = rk4(stellar_derivatives,m_step[step],z,h,args=(Mwant, R_guess, mu, XH, pp_factor))

        Nsteps += 1
        m_step[step+1] = m_step[step] + h
        z = np.copy(znew) 

    if Nsteps < max_steps:
        pass
    else:
        raise Exception('too many iterations')

    return m_step[0:Nsteps],r_step[0:Nsteps],p_step[0:Nsteps],L_step[0:Nsteps]
