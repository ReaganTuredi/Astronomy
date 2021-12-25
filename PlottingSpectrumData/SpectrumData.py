from astropy.table import Table
import matplotlib.pyplot as plt

t=Table.read('spec-3875-55364-0308.fits')

flux=t["FLUX"]
OR=t["MODEL"]

wavelength=t["LOGLAM"]
wavelength=10**wavelength

plt.plot(wavelength,flux, color='black')

plt.axvline(5619,0 , 10, color='red')
plt.text(5619, 10,'H', rotation=90, verticalalignment='bottom',fontsize=50)

plt.axvline(5570,0 , 10, color='red')
plt.text(5570, 10,'K', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(3964,0 , 10, color='blue')
plt.text(3964, 10,'Mg II', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(5279,0 , 10, color='blue')
plt.text(5279, 10,'O II', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(5275,0 , 10, color='blue')
plt.text(5275, 10,'O II', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(9323,0 , 10, color='blue')
plt.text(9323, 10,'N II', rotation=90, verticalalignment='bottom',fontsize=50)

plt.axvline(9293,0 , 10, color='red')
plt.text(9293, 10,'Hα', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(7328,0 , 10, color='red')
plt.text(7328, 10,'Mg I', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(7022,0 , 10, color='blue')
plt.text(7022, 10,'O III', rotation=90, verticalalignment='top',fontsize=50)

plt.axvline(7090,0 , 10, color='blue')
plt.text(7090, 10,'O III', rotation=90, verticalalignment='top',fontsize=50)

plt.xlim(3500, 10000)
plt.ylim(-8, 12)
plt.xlabel("Wavelength [Angstroms]", fontsize=50)
plt.ylabel("Flux[10e-17 erg/cm^2/s/Å]",fontsize=50)
plt.title("Spectrum Plot [SDSS J145610.86+302106.2]", fontsize=50)
plt.rcParams['figure.figsize'] = [70, 35]
plt.tick_params(labelsize=50)
plt.savefig('spectrumplot.png')
plt.show()
