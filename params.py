import numpy as np
import os

par =   {}

#===============================================================================
""" particle parameters """
#===============================================================================

par['N']    =   100    # number of particles
par['m']    =   1       # particle masses

#===============================================================================
""" cloud parameters """
#===============================================================================

par['r0']       =   1                                       # initial radius
par['tau0']     =   .1                                       # initial rotational period
par['disp0']    =   1e-3                                    # initial velocity dispersion
par['omega0']   =   np.array([ 0,0,(2*np.pi)/par['tau0'] ]) # initial rotational axis

#===============================================================================
""" physical parameters """
#===============================================================================

par['rho0']     =   10
# par['rho0']     =   1e-14   # [g cm^-3] rho << rho0 ~ isothermal; rho >> rho0 ~ adiabatic
par['gamma']    =   1.41    # ratio of specific heats for hydrogen
# par['Gamma']    =   1       # radiative heating rate
# par['Lambda']   =   1       # radiative cooling rate
par['alpha']    =   1       # tunable shock parameter
par['beta']     =   1       # tunable shock parameter

#===============================================================================
""" physical constants """
#===============================================================================

par['k']    =   1.3807e-16  # [cm^2 g s^-2 K-1] Boltzmann's constant
par['mu']   =   2           # mean molecular weight (H2 in this case)
par['G']    =   10          # [natural unity] gravitational constant
