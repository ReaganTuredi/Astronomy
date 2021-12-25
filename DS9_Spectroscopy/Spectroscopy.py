import numpy as np
%matplotlib inline
from astropy.io import fits
import matplotlib.pyplot as plt

#Reading in arrays

print('reading spec1.fits...')
spec1_raw = fits.open('spec1.fits',ignore_missing_end=True)
spec1 = np.array(spec1_raw[0].data[0],dtype=np.float64)
print('got an array of dimension ',spec1.shape)

print('reading spec1.fits...')
spec2_raw = fits.open('spec2.fits',ignore_missing_end=True)
spec2 = np.array(spec2_raw[0].data[0],dtype=np.float64)
print('got an array of dimension ',spec2.shape)

print('reading spec1.fits...')
spec3_raw = fits.open('spec3.fits',ignore_missing_end=True)
spec3 = np.array(spec3_raw[0].data[0],dtype=np.float64)
print('got an array of dimension ',spec3.shape)


#Taking a slice of each image array that extends along the entire length of the spectrum, centered on the bright source spectrum.
spec1[871:892,:]
spec2[875:890,:]
spec3[933:970,:]

# At the necessary wavelengths, summing all the light from that source
Spec1sum = np.sum(spec1,axis=0)
print(Spec1sum.shape)
Spec2sum = np.sum(spec2,axis=0)
print(Spec1sum.shape)
Spec3sum = np.sum(spec3,axis=0)
print(Spec1sum.shape)

# Plot the specs
plt.plot(Spec1sum/np.max(Spec1sum))
plt.plot(Spec2sum/np.max(Spec2sum))
plt.plot(Spec3sum/np.max(Spec3sum))

#Constructing the wavelength scales for each of the three spectra
dx = 1
Narr = 4142
delta1 = 5577.3 - 2669*dx
sp1scale = np.arange(delta1,delta1+Narr*dx,dx)
print("sp1scale = ",sp1scale)

dx = 1
Narr = 4142
delta2 = 5577.3 - 2669*dx
sp2scale = np.arange(delta2,delta2+Narr*dx,dx)
print("sp2scale = ",sp2scale)

dx = 1
Narr = 4142
delta3 = 5577.3 - 2680*dx
sp3scale = np.arange(delta3,delta3+Narr*dx,dx)
print("sp3scale = ",sp3scale)

#Plotting the profile of the  5577.3 Å  Oi line
plt.figure(figsize=(10,5))
plt.plot(sp3scale,Spec3sum/np.max(Spec3sum))
plt.ylim([.9,1])
plt.xlim([5570,5590])
plt.xlabel('Wavelength in Angstroms')
plt.ylabel('Intensity')

#Restricting x axis to 4810–4910 A to adjust for n=4 -> n=2 hydrogen emission
plt.figure(figsize=(10,5))
plt.plot(sp3scale,Spec3sum/np.max(Spec3sum))
plt.ylim([.915,.924])
plt.xlim([4810,4910])
plt.xlabel('Wavelength in Angstroms')
plt.ylabel('Intensity')
plt.vlines(4861.3,-100,100)
plt.vlines(4874.3,-100,100,linestyle='--')

# spec1 and spec 2 can be interchanged in the previous section, but spec 3 is the only spectrum with an appreciable maximum. 
