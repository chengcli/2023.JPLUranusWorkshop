#! /usr/bin/env python3
from pylab import *
from netCDF4 import Dataset
from matplotlib.gridspec import GridSpec
from scipy.interpolate import interp1d
from contribution_function import plot_contribution_function
import string
#import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Serif'
plt.tick_params(axis='both', labelsize=12)

# frequencies
freq = [0.6, 1.25, 2.6, 5.2, 10., 22.]

# adiabatic
data = Dataset('outputs/uranus_mwr-ad-main.nc', 'r')
pres = data['press'][0,:,0,0]/1.E5
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]

tb0_ad = tb[::4]
ld0_ad = (tb0_ad - tb45)/tb0_ad*100.
temp_ad = data['temp'][0,:,0,0]

h2o_ad = data['vapor1'][0,:,0,0]/data['vapor1'][0,0,0,0]*23000.
nh3_ad = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*200.
h2s_ad = data['vapor3'][0,:,0,0]/data['vapor3'][0,0,0,0]*300.

fig, axs = subplots(1, 3, figsize = (12, 8),
  gridspec_kw = {'width_ratios': [4,1,1]})
subplots_adjust(wspace = 0.08)

################################
# NH3
# super
data = Dataset('outputs/uranus_mwr-10.xNH3-main.nc', 'r')
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]
tb0_sup = tb[::4]
ld0_sup = (tb0_sup - tb45)/tb0_sup*100.
nh3_sup = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*2000.

# sub
data = Dataset('outputs/uranus_mwr-0.1xNH3-main.nc', 'r')
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]

tb0_sub = tb[::4]
ld0_sub = (tb0_sub - tb45)/tb0_sub*100.
nh3_sub = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*20.

ax = axs[0]
ax2 = ax.twiny()
plot_contribution_function(ax2, "uranus_mwr-NH4SH", 0.)
ax2.set_yscale('log')
ax2.set_ylim([1000., 10.])

ax.plot(nh3_ad, pres, 'C2-', label = 'NH$_3$', linewidth = 2)
ax.plot(nh3_sup, pres, 'C2--', label = 'NH$_3$ x 10')
ax.plot(nh3_sub, pres, 'C2:', label = 'NH$_3$ x 0.1')

ax.set_yscale('log')
ax.set_xlabel('Vapor mole fraction (ppmv)', fontsize = 14)
ax.set_ylabel('Pressure (bar)', fontsize = 14)
ax.set_ylim([1000., 10.])
ax.set_xlim([1.E-5, 1.E5])
ax.set_xscale('log')
ax.legend(loc=0, fontsize = 14)

ax = axs[1]
ax.plot([0., 0.], [0.6, 22.], 'k--')
print(tb0_sup - tb0_sub)
ax.errorbar(tb0_sup - tb0_ad, freq, xerr = 0.02*tb0_sup, 
            label='$\\Theta_{1bar} = 169 K$', capsize = 5, color = 'C2', ls = '--')
ax.errorbar(tb0_sub - tb0_ad, freq, xerr = 0.02*tb0_sup, 
            label='$\\Theta_{1bar} = 163 K', capsize = 5, color = 'C2')
ax.set_ylim([0.59, 22.1])
#ax.set_xlim([-20., 20.])
ax.set_yscale('log')
ax.set_xlabel('Tb anomaly (K)', fontsize = 14)
ax.set_yticklabels([])

ax = axs[2]
ax.plot([0., 0.], [0.6, 22.], 'k--')
print(ld0_sup - ld0_sub)
ax.errorbar(ld0_sup - ld0_ad, freq, xerr = 0.1,
            label='\\Theta_{1bar} = 169 K', capsize = 5, color = 'C2', ls = '--')
ax.errorbar(ld0_sub - ld0_ad, freq, xerr = 0.1, 
            label='\\Theta_{1bar} = 163 K', capsize = 5, color = 'C2')
ax.set_ylim([0.59, 22.1])
#ax.set_xlim([-0.8, 0.8])
ax.yaxis.set_ticks([])
ax.set_xlabel('R45 anomaly (%)', fontsize = 14)
ax.set_yscale('log')
ax.set_yticklabels([])


################################
# H2S
# super
data = Dataset('outputs/uranus_mwr-10.xH2S-main.nc', 'r')
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]
tb0_sup = tb[::4]
ld0_sup = (tb0_sup - tb45)/tb0_sup*100.
h2s_sup = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*3000.

# sub
data = Dataset('outputs/uranus_mwr-0.1xH2S-main.nc', 'r')
tb = data['radiance'][0,:,0,0]
tb45 = tb[3::4]

tb0_sub = tb[::4]
ld0_sub = (tb0_sub - tb45)/tb0_sub*100.
h2s_sub = data['vapor2'][0,:,0,0]/data['vapor2'][0,0,0,0]*30.

ax = axs[0]
ax2 = ax.twiny()
plot_contribution_function(ax2, "uranus_mwr-NH4SH", 0.)
ax2.set_yscale('log')
ax2.set_ylim([1000., 10.])

ax.plot(h2s_ad, pres, 'C1-', label = 'H$_2$S', linewidth = 2)
ax.plot(h2s_sup, pres, 'C1--', label = 'H$_2$S x 10')
ax.plot(h2s_sub, pres, 'C1:', label = 'H$_2$S x 0.1')

ax.set_yscale('log')
ax.set_xlabel('Vapor mole fraction (ppmv)', fontsize = 14)
ax.set_ylabel('Pressure (bar)', fontsize = 14)
ax.set_ylim([1000., 10.])
ax.set_xlim([1.E-5, 1.E5])
ax.set_xscale('log')
ax.legend(loc=0, fontsize = 14)

ax = axs[1]
ax.plot([0., 0.], [0.6, 22.], 'k--')
print(tb0_sup - tb0_sub)
ax.errorbar(tb0_sup - tb0_ad, freq, xerr = 0.02*tb0_sup, 
            label='$\\Theta_{1bar} = 169 K$', capsize = 5, color = 'C1', ls = '--')
ax.errorbar(tb0_sub - tb0_ad, freq, xerr = 0.02*tb0_sup, 
            label='$\\Theta_{1bar} = 163 K', capsize = 5, color = 'C1')
ax.set_ylim([0.59, 22.1])
#ax.set_xlim([-20., 20.])
ax.set_yscale('log')
ax.set_xlabel('Tb anomaly (K)', fontsize = 14)
ax.set_yticklabels([])

ax = axs[2]
ax.plot([0., 0.], [0.6, 22.], 'k--')
print(ld0_sup - ld0_sub)
ax.errorbar(ld0_sup - ld0_ad, freq, xerr = 0.1,
            label='\\Theta_{1bar} = 169 K', capsize = 5, color = 'C1', ls = '--')
ax.errorbar(ld0_sub - ld0_ad, freq, xerr = 0.1, 
            label='\\Theta_{1bar} = 163 K', capsize = 5, color = 'C1')
ax.set_ylim([0.59, 22.1])
#ax.set_xlim([-0.8, 0.8])
ax.yaxis.set_ticks([])
ax.set_xlabel('R45 anomaly (%)', fontsize = 14)
ax.set_yscale('log')
ax.set_yticklabels([])

labels = iter(string.ascii_uppercase)  # Generates the labels A, B, C, ...
for ax in axs:
    ax.annotate(f"({next(labels)})", xy=(0.05, 0.05), xycoords="axes fraction", fontsize=12, fontweight="bold")

#show()
savefig('three_cases_composition.png', bbox_inches='tight')
