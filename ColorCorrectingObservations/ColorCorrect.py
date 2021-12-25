import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline
from astropy.io import fits
from scipy.optimize import curve_fit
from scipy.ndimage import shift

Bias = fits.open('Bias.fits')
bias1 = np.array(Bias[0].data,dtype=np.float64)
Bias.close()

Dark = fits.open('Dark.fits')
Dark1 = np.array(Dark[0].data,dtype=np.float64)
Dark.close()

FlatB = fits.open('FlatB.fits')
FlatB1 = np.array(FlatB[0].data,dtype=np.float64)
FlatB.close()

FlatV = fits.open('FlatV.fits')
FlatV1 = np.array(FlatV[0].data,dtype=np.float64)
FlatV.close()

FlatR = fits.open('FlatR.fits')
FlatR1 = np.array(FlatR[0].data,dtype=np.float64)
FlatR.close()

MessierB = fits.open('MessierB.fits')
MessierB1 = np.array(MessierB[0].data,dtype=np.float64)
MessierB.close()

MessierR = fits.open('MessierR.fits')
MessierR1 = np.array(MessierR[0].data,dtype=np.float64)
MessierR.close()

MessierV = fits.open('MessierV.fits')
MessierV1 = np.array(MessierV[0].data,dtype=np.float64)
MessierV.close()


# Correcting for CCD Bias Level 
NewB= (MessierB1-bias1)
NewV= (MessierV1-bias1)
NewR= (MessierR1-bias1)

# Correcting for Dark Current
DarkV= (NewV-Dark1)
DarkB= (NewB-Dark1)
DarkR= (NewR-Dark1)

# Correcting for Flat Field
NormB= (FlatB1/27714.421875)
NormV= (FlatV1/25777.199652777777)
NormR= (FlatR1/30249.842633928572)

DivR= (DarkR/NormR)
DivB= (DarkB/NormB)
DivV= (DarkV/NormV)

# Overwrite fits file with corrections
fits.writeto('<newR>.fits', DivR, overwrite=True)
fits.writeto('<newB>.fits', DivB, overwrite=True)
fits.writeto('<newV>.fits', DivV, overwrite=True)
