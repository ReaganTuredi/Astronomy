def fEuler(f,t,z,h,args=()):
    if not isinstance(args,tuple):
        args = (args,)
    return z + h*f(t,z,*args)


def rk2(f,t,z,h,args=()):

    if not isinstance(args,tuple):
        args = (args,)
    z_mp = z + (h/2)*f(t,z, *args)
    znew = z + h*f(t+h/2, z_mp, *args)


    return znew

def rk4(f,t,z,h,args=()):
   
    if not isinstance(args,tuple):
        args = (args,)
    
    k1 = f(t,z,*args)
    k2 = f(t+h/2, z+((h/2)*k1), *args)
    k3 = f(t+h/2,z+((h/2)*k2), *args)
    k4 = f(t+h, z + h*k3, *args)

    znew = z + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

    return znew
