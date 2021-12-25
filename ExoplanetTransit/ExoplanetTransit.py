import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

in_array = np.genfromtxt('keplerD_lc.dat', skip_header=18)
print(in_array)

#plot of the star's lightcurve
plt.figure(figsize=(10,5))
plt.plot(HJD,DNF)
plt.xlabel("Heliocentric Julian Date")
plt.ylabel("detrended normalized flux")
plt.title("detrended normalized flux as a function of time")

#determining first transit
plt.figure(figsize=(10,5))
plt.plot(HJD,DNF)
plt.xlabel("Heliocentric Julian Date")
plt.ylabel("detrended normalized flux")
plt.title("detrended normalized flux as a function of time")
plt.xlim([2454957.077874,2454957.727433])
plt.ylim([0.99,1.000222]) 
plt.vlines(2454957.380,0.9,1.1)
plt.vlines(2454957.625,0.9,1.1)

#determining transit period 
plt.figure(figsize=(10,5))
foo = np.arange(2454957.077874,2454996.736769,4.88382899994)
plt.plot(HJD,DNF)
plt.xlabel("Heliocentric Julian Date")
plt.ylabel("detrended normalized flux")
plt.title("detrended normalized flux as a function of time")
plt.vlines(foo,0.99,1.0)

#folded lightcurve 
plt.figure(figsize=(10,5))
t_fold = np.remainder(HJD,4.88382899994)
print(t_fold)
plt.scatter(t_fold,DNF,s=3)
plt.xlabel("Adjusted HJD")
plt.ylabel("detrended normalized flux")

# transit depth
plt.figure(figsize=(10,5))
t_fold = np.remainder(HJD,4.88382899994)
print(t_fold)
plt.scatter(t_fold,DNF,s=3)
plt.xlabel("Transit Period")
plt.ylabel("detrended normalized flux")
plt.hlines(0.9924,0,5,color='black')
plt.hlines(1.0,0,5,color='black')

#transit duration
plt.figure(figsize=(10,5))
t_fold = np.remainder(HJD,4.88382899994)
print(t_fold)
plt.scatter(t_fold,DNF,s=3)
plt.xlabel("Transit Period")
plt.ylabel("detrended normalized flux")
plt.vlines(3.1,0.992,1,color='black')
plt.vlines(3.31,0.992,1,color='black')

