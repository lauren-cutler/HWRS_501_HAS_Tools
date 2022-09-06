#code to calculate air pressure at a given height

import numpy as np

p0 = 101325 ###Reference Pressure in Pa
g = 9.81 ###gravity m/s2
T0 = 288.16 ####Sea level temperature in K
m = 0.02896968 ###molar mass of air in kg/mol
R0 = 8.3144 ###universal gas constant in J/(mol*K)
z = np.array(0,2000,100)

p =  np.zeros((len(z)))  ### height in meters
for i in range(len(z)):
    p[i] = p0*np.exp((-g*z[i]*m)/(T0*R0))

print(p)