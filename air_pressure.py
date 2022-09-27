#code to calculate air pressure at a given height
#%%

import numpy as np
import math
#%%
def air_pressure(z):
    p0 = 101325 ###Reference Pressure in Pa
    g = 9.81 ###gravity m/s2
    T0 = 288.16 ####Sea level temperature in K
    m = 0.02896968 ###molar mass of air in kg/mol
    R0 = 8.3144 ###universal gas constant in J/(mol*K)
    p = p0*np.exp((-g*z*m)/(T0*R0))
    print(p)
    return p
#%%
air_pressure(10)
# %%
