#! /usr/bin/env python3
from pylab import *
from netCDF4 import Dataset
#from matplotlib.gridspec import GridSpec
from scipy.interpolate import interp1d
from contribution_function import plot_contribution_function
import string

plt.rcParams['font.family'] = 'Serif'
plt.tick_params(axis='both', labelsize=12)

# frequencies
freq = [0.6, 1.25, 2.6, 5.2, 10., 22.]

#case = 'noNH4SH'
#case = 'test'
case = 'NH4SH'

# standard case
data = Dataset(f'outputs/uranus_mwr-{case}-main.nc', 'r')
pres = data['press'][0,:,0,0]/1.E5
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]

tb0_ad = tb[::4]
ld0_ad = (tb0_ad - tb45)/tb0_ad*100.
temp_ad = data['temp'][0,:,0,0]

h2o_ad = data['vapor1'][0,:,0,0]/data['vapor1'][0,0,0,0]*23000.
nh3_ad = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*200.
h2s_ad = data['vapor3'][0,:,0,0]/data['vapor3'][0,0,0,0]*300.
ch4_ad = data['vapor4'][0,:,0,0]/data['vapor4'][0,0,0,0]*23000.

print(tb0_ad)
print(ld0_ad)

fig, axs = subplots(1, 2, figsize = (10, 6), sharey = True)
subplots_adjust(wspace = 0)

ax = axs[0]
ax2 = ax.twiny()
plot_contribution_function(ax2, f"uranus_mwr-{case}", 0.)
ax2.set_xlabel('Contribution function', fontsize = 12)

ax.plot(temp_ad, pres, 'C3-', label = 'Temperature')

ax.set_yscale('log')
ax.set_xlabel('Temperature (K)', fontsize = 14)
ax.set_ylabel('Pressure (bar)', fontsize = 14)
ax.set_xlim([40., 800.])
ax.set_ylim([1000., 0.3])
#ax.set_xlim([170., 420.])
ax.legend(loc=0, fontsize = 14)

ax = axs[1]
ax.plot(ch4_ad, pres, 'C0-', label = 'CH$_4$')
ax.plot(h2s_ad, pres, 'C1-', label = 'H$_2$S')
ax.plot(nh3_ad, pres, 'C2-', label = 'NH$_3$')
ax.plot(h2o_ad, pres, 'C4-', label = 'H$_2$O')

ax.set_yscale('log')
ax.set_xlabel('Vapor mole fraction (ppmv)', fontsize = 14)
ax.set_xscale('log')
ax.set_xlim([1.E-5, 1.E5])
ax.legend(loc = 0, fontsize = 14)

#show()
savefig('wfunc_profile.png', bbox_inches='tight')
