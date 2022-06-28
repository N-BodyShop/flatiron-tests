#Python3 version, uses pynbody
import matplotlib.pyplot as plt
import pynbody
import numpy as np
import os

tdir = "./"
tbase = "cosmo16out"

zp = []
Tp = []
HIp = []
HeIp = []
HeIIp = []

for iout in range(1025):
    tfile = tdir+tbase+"."+str(iout).zfill(6)
    if (os.path.isfile(tfile)):
        s = pynbody.load(tfile)
        
        #Extra files
        #s.properties
        #s.g.loadable_keys()
        #s.g.keys()
        #['phi', 'temp', 'pos', 'metals', 'eps', 'rxy', 'vx', 'r', 'mass', 'rho', 'vy', 'y', 'x', 'vel', 'z', 'vz']
        z = s.properties['z']
        
        zp.append( z )
        Tp.append( s.g['temp'][0] )
        HIp.append ( s.g['HI'][0] )
        HeIp.append ( s.g['HeI'][0] )
        HeIIp.append ( s.g['HeII'][0] )

# zero metallicity Y_H = 1-0.236,  Y_He = 0.236/4.0
 
plt.title("Cosmo16 evolution")
plt.plot(zp,Tp,label="T")
plt.plot(zp,HIp,label="HI")
plt.plot(zp,(1-0.236)-np.array(HIp),label="HII")
plt.plot(zp,HeIp,label="HeI")
plt.plot(zp,HeIIp,label="HeII")
plt.plot(zp,0.236/4.0-np.array(HeIp)-np.array(HeIIp),label="HeIII")
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel("Redshift, z")
plt.ylabel("T (K), species per Baryon")
plt.show()

