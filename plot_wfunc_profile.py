#! /usr/bin/env python3
from pylab import *
from netCDF4 import Dataset
from matplotlib.gridspec import GridSpec
from scipy.interpolate import interp1d
#from contribution_function import plot_contribution_function
import string

plt.rcParams['font.family'] = 'Serif'
plt.tick_params(axis='both', labelsize=12)

# frequencies
freq = [0.6, 1.25, 2.6, 5.2, 10., 22.]

# standard case
data = Dataset('outputs/uranus_mwr-noNH4SH-main.nc', 'r')
pres = data['press'][0,:,0,0]/1.E5
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]

tb0_ad = tb[::4]
ld0_ad = (tb0_ad - tb45)/tb0_ad*100.
temp_ad = data['temp'][0,:,0,0]
nh3_ad = data['vapor2'][0,:,0,0]/2.7e-3*370.

print(tb0_ad)
print(ld0_ad)

fig, axs = subplots(1, 2, figsize = (12, 10), sharey = True)
subplots_adjust(wspace = 0.08)

ax = axs[0]
ax2 = ax.twiny()
#plot_contribution_function(ax2, "juno_mwr-tau", 0.)

ax.plot(temp_ad, pres, 'k-', label='Adiabatic')

ax.set_yscale('log')
ax.set_xlabel('Temperature (K)', fontsize = 14)
ax.set_ylabel('Pressure (K)', fontsize = 14)
ax.set_ylim([100., 1.])
#ax.set_xlim([170., 420.])
ax.legend(loc=0, fontsize = 14)

ax = axs[1]
ax.plot(nh3_ad, pres, 'k-', label='$NH_3 = 310 ppm$')
ax.set_yscale('log')
ax.set_xlabel('NH$_3$ concentration (ppmv)', fontsize = 14)
ax.set_xscale('log')

show()
#savefig('three_cases_dTdz.png', bbox_inches='tight')
