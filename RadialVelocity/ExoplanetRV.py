import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

in_array = np.genfromtxt('keplerD_rv.dat', skip_header=17, usecols=(0,1,2,3,4))
print(in_array)
BJD = in_array[:,0]
RV = in_array[:,1]
RVU = in_array[:,2]
BIS = in_array[:,3]
BU = in_array[:,4]
CBJD=BJD-BJD[0]

plt.figure(figsize=(10,5))
t_fold = np.remainder(CBJD,4.886)
t1fold=t_fold/4.886
plt.scatter(t1fold,RV)
time        = np.arange(0, 1, 0.1);
amplitude   = 40*np.sin((2*np.pi)*time+1)
plot.plot(time, amplitude)
plot.title('Fitted Sinusoid')
plot.xlabel('Radial Velocity')
plot.ylabel(r"$phase{\phi}$")
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
plt.savefig('fitted_sinusoid.png')

Radial_Velocity=(max(RV)-min(RV))/2
