"""
Created on Mon Aug 18 12:40:22 2025

@author: Marco Viezzer
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

'''
Open data file and save columns in numpy arrays, skipping the header
Masses measured in 10^10 solar masses / h, positions in ckpc/h
'''

dataFile = 'file2_Groups_AGN-wWU_500Mpc_Data.txt'
massTot, massGas, massDM, massStars, massBH, xPos, yPos, zPos = np.loadtxt(dataFile, skiprows=1, unpack=True)

# DM mass vs baryonic mass
barMass = massStars+massGas # Useful to save baryonic mass in separate variable

# First plot in loglog scale to better appreciate distribution of data points
plt.loglog(barMass, massDM, c='r', marker='o', linestyle='', label='Data points')

plt.grid()
plt.xlabel(r'Baryonic mass $[10^{10} \, M_\odot/h]$')
plt.ylabel(r'Dark Matter mass $[10^{10} \, M_\odot/h]$')
plt.title('DM mass vs baryonic mass')
plt.legend()

plt.savefig('DM_baryonic_mass_loglog.png')
plt.show()

# Plot in linear scale with linear fit
plt.plot(barMass, massDM, c='r', marker='o', linestyle='', label='Data points')
opt = stats.linregress(barMass, massDM)
massVals = np.linspace(0.01,np.max(barMass),1000)
plt.plot(massVals, opt.intercept + opt.slope*massVals, label=r'$y = {:.2f} \, x {:.2f}$'.format(opt.slope, opt.intercept))

plt.grid()
plt.xlabel(r'Baryonic mass $[10^{10} \, M_\odot/h]$')
plt.ylabel(r'Dark Matter mass $[10^{10} \, M_\odot/h]$')
plt.title('DM mass vs baryonic mass with linear fit')

plt.legend()

plt.savefig('DM_baryonic_mass_fit.png')
plt.show()

'''
Find most massive halo and compute distances from it
'''

biggest = np.max(massTot)
idx = np.where(massTot==biggest)[0]

# Compute distances
dist = np.sqrt((xPos-xPos[idx])**2 + (yPos-yPos[idx])**2 + (zPos-zPos[idx])**2)
newIndex = np.delete(np.arange(len(massTot)), idx) # Get new index list without most massive halo for plots
# Plot in log-log scale scale
plt.scatter([dist[i] for i in newIndex], [massTot[i] for i in newIndex], color='violet', edgecolors='black', marker='o', linestyle='', label='Data points')

plt.grid()
plt.title('Mass vs distance from most massive halo')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Distance [ckpc/h]')
plt.ylabel(r'Mass $[10^{10} \, M_\odot/h]$')
plt.legend()

plt.savefig('Mass_distance_scatter.png')
plt.show()

'''
Produce histogram of DM mass distribution with mean and median
'''

# Histogram of the logarithm of Dark Matter mass
dmHist = plt.hist(np.log10(massDM), bins=100, color='darkblue', edgecolor='black')
plt.title('Dark Matter mass distribution')
plt.xlabel(r'$log_{10}(M \, [10^{10} \, M_\odot/h])$')
plt.ylabel('Counts')

meanDM = np.mean(massDM)
medianDM = np.median(massDM)

ylim = plt.ylim()
plt.axvline(x=np.log10(meanDM), c='red', linestyle='--')
plt.axvline(x=np.log10(medianDM), c='green', linestyle='--')
plt.text(0.5, ylim[1]*0.9,
         r'Mean={:.2f} $\cdot 10^{{10}} M_\odot/h$'.format(meanDM),
         color='red', ha='center', va='bottom')
plt.text(0.25, ylim[1]*0.9, r'Median={:.2f} $\cdot 10^{{10}} M_\odot/h$'.format(medianDM), color='green', va='top', ha='right')

plt.savefig('DM_mass_distribution.png')
plt.show()

'''
4x4 panel of halos' spatial distribution in 3 projections.
'''
fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))

# Hide the 4th unused panel
axes[1,1].axis("off")

# For optimal visibility, size scales with square root of the stellar mass
# and color scales with the log of the gas mass.
axes[0,0].set_title('x-y distribution')
axes[0,0].scatter(xPos, yPos, s=np.sqrt(massStars*10**6), c=np.log(massGas), cmap='plasma')
axes[0,0].set_ylabel('Distance [ckpc/h]')
axes[0,1].set_title('z-y distribution')
axes[0,1].scatter(yPos, zPos, s=np.sqrt(massStars*10**6), c=np.log(massGas), cmap='plasma')
axes[1,0].set_title('x-z distribution')
axes[1,0].scatter(xPos, zPos, s=np.sqrt(massStars*10**6), c=np.log(massGas), cmap='plasma')
axes[1,0].set_xlabel('Distance [ckpc/h]')
axes[1,0].set_ylabel('Distance [ckpc/h]')

plt.savefig('Spatial_distribution_panel.png')
plt.show()

'''
BH mass vs stellar mass with threshold on BH mass
'''

# Find haloes above threshold
BHthreshold = 8*10**-5
BHidx = np.where(massBH >= BHthreshold)

# Linear fit
optBH = stats.linregress(massStars, massBH)
xVals = np.linspace(-0.5,4.5,100)

plt.scatter([massStars[i] for i in BHidx[0]], [massBH[i] for i in BHidx[0]], color='darkgreen', label='Data points')
plt.plot(xVals, optBH.intercept + optBH.slope*xVals, label=r'$y = {:.2f} \, x {:.2f}$'.format(optBH.slope, optBH.intercept))

plt.grid()
plt.title('BH mass vs stellar mass')
plt.xlabel(r'Stellar mass $[10^{10} \, M_\odot/h]$')
plt.ylabel(r'Black hole mass $[10^{10} \, M_\odot/h]$')
plt.legend()

plt.savefig('BH_stellar_mass_fit.png')
plt.show()

plt.scatter([massStars[i] for i in BHidx[0]], [massBH[i] for i in BHidx[0]], color='darkgreen', label='Data points')
plt.plot(xVals, optBH.intercept + optBH.slope*xVals, label=r'$y = {:.2f} \, x {:.2f}$'.format(optBH.slope, optBH.intercept))

plt.grid()
plt.yscale('log')
plt.title('BH mass vs Stellar mass')
plt.xlabel(r'Stellar mass $[10^{10} \, M_\odot/h]$')
plt.ylabel(r'Black hole mass $[10^{10} \, M_\odot/h]$')
plt.legend()

plt.savefig('BH_stellar_mass_log.png')
plt.show()


'''
2d cumulative histogram
'''

massIdx = np.where(massTot >= 0.307)[0]

# Bins for the 2d histograms, with logarithmic scale for the masses
nBins = 10
xBins = np.logspace(np.log10(0.3), np.log10(np.max(massTot)),nBins)
yBins = np.linspace(0,2400, nBins)
cumHist = np.zeros((nBins-1, nBins-1))

for i in massIdx:
    # Bin all masses different from the chosen one
    xaxis = [massTot[j] for j in massIdx if j!=i]
    # Compute distance of each halo from the chosen one
    yaxis = np.sqrt([(xPos[j]-xPos[i])**2 + (yPos[j]-yPos[i])**2 + (zPos[j]-zPos[i])**2 for j in massIdx if j!=i])
    tempHist= np.histogram2d(xaxis, yaxis, bins=(xBins,yBins))[0]
    # Sum each contribution for the final cumulative histogram
    cumHist += tempHist

X,Y = np.meshgrid(xBins,yBins)
plt.pcolormesh(X, Y, cumHist.T, cmap='viridis', shading='auto')
plt.xscale('log')
plt.title('2d cumulative histogram')
plt.xlabel('Total mass $[10^{10} \, M_\odot/h]$')
plt.ylabel('Distance [ckpc/h]')
plt.colorbar(label='Number of haloes')

plt.savefig('Cumulative_2dhistogram')
plt.show()

    