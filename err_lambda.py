# -*- coding: utf-8 -*-
from math import sqrt, asin, sin, pi

h = 6.62606896 * 10**-34 # Planck constant
c = 2.9979248  * 10**8   # Speed of light in vacuum
m = 9.10938215 * 10**-31 # Mass of an electron
eV = 1.602176487 * 10**-19 # electron-volt
r2d = 180/pi        # rads to degrees ratio

deltaL = lambda V, deltaV: (h/(sqrt(2*m) * (eV*V)**(3/2)))*deltaV 


distances = [3.3756, 2.1386, 2.0390, 1.6811, 1.2340, 1.1603]
dist_factor = 10**-10

voltages = [8000, 7000, 6000, 5000, 4000]
deltaV = [60, 60, 50, 40, 30]

tubelen = 127 # tube length (in mm)
n = 2

for i in xrange(len(voltages)):
    print("{0:.4f},{1:.10f}".format( 
        voltages[i], 
        deltaL(voltages[i], deltaV[i]))
    )

