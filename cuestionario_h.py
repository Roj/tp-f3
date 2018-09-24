#!/usr/bin/python3
from math import sqrt, asin, sin, pi as π

h = 6.62 * 10**-34 # Planck constant
c = 300  * 10**6   # Speed of light in vacuum
m = 9.11 * 10**-31 # Mass of an electron
eV = 1.6 * 10**-19 # electron-volt
r2d = 180/π        # rads to degrees ratio

λ = lambda Ec: (h*c)/sqrt(Ec**2 + Ec*(2*m*c**2))
θ = lambda λ, n, d: asin(n*λ/(2*d))

distances = [3.3756, 2.1386, 2.0390, 1.6811, 1.2340, 1.1603]
dist_factor = 10**-10

voltages = [9000, 8000, 7000, 6000, 5000, 4000]

tubelen = 127 # tube length (in mm)
n = 2

for d in distances:
    for v in voltages:
        print("{0:.4f},{1:d},{2:.4f},{3:.4f}".format(
            d, 
            v, 
            θ(λ(v*eV), n, d * dist_factor) * r2d,
            tubelen * sin(4*θ(λ(v*eV), n, d * dist_factor))
        ))

