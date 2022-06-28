#Python3 version
#to run   exec(open("plotonestar.py").read())
# or command line python3 plotonestar.py
import matplotlib.pyplot as plt
import pynbody
import numpy as np

tdir = "./"
tfile = tdir+"agora_gasoline.000100"

# UNITS:  dMsolUnit: 1e+09 dKpcUnit: 1 dErgPerGmUnit: 4.30158e+13 dGmPerCcUnit (z=0): 6.77331e-23 dSecUnit: 4.70475e+14 (14.9084 Myr) dKmPerSecUnit (z=0): 65.5865
s = pynbody.load(tfile)

#Extra files
#s.properties
#s.g.loadable_keys()
#>>> s.g.keys()
#['phi', 'temp', 'pos', 'metals', 'eps', 'rxy', 'vx', 'r', 'mass', 'rho', 'vy', 'y', 'x', 'vel', 'z', 'vz']

Hcc=6.77331e-23/1.67e-24
kms = 65.5865

if (True):
    #plt.scatter(s.s['x'],s.s['y'],s=1e-1,c='r')
    #plt.scatter(s.g['x'],s.g['y'],s=1e-1,c=np.log10(s.g['temp']),cmap="rainbow")
    # mustplot 'Tinc' to get average of Hot/Cold phase  'Temp' is cold phase
    plt.scatter(s.g['x'],s.g['y'],s=1e-1,c=np.log10(s.g['Tinc']),cmap="rainbow") 
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(' Gas temperature '+r'$log_{10} T (K)$')
    plt.xlim([-20,20])
    plt.ylim([-20,20])
    plt.colorbar()
    plt.show()

if (True):
    sfr, tsfr = np.histogram((s.s['tform']-6740.4)*14.9084, bins=100, range=[0,500], weights=s.s['mass'],density=False)
    sfr=sfr*1e9/4e6 # 5 Myr per bin
    #plt.scatter(s.s['x'],s.s['y'],s=1e-1,c='r')
    plt.plot(tsfr[:-1],sfr)
    plt.xlabel('time (Myr)')
    plt.ylabel('SFR (Msun/yr)')
    plt.xlim([0,100])
    plt.show()

