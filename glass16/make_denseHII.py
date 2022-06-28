#dense HII region IC
import matplotlib.pyplot as plt
import numpy as np
from pytipsy import *

# Stretch an existing 16^3 glass (and make copies)
# to create grid of desired size and density

Lunit = 0.001 #kpc
munit = 1.0 #msun

h16,g16,d16,s16 = rtipsy('glass16.std')

ngasmax=10000000 # 
g0=makecatg(ngasmax)
g0['y']=g0['y']+1e20  

mgas=0.01 #msun 
rscale = 0.03435*16 #spacing 1e4 H/cc 0.01 Msun particles(pre HII density?)
Lbox = 1.0
fileout="denseHII_1e4.std"

nrep=4
npart=0
for irep in range(-nrep,nrep+1):
    for jrep in range(-nrep,nrep+1):
        for krep in range(-nrep,nrep+1):
            x = (irep+g16['x'])*rscale
            y = (jrep+g16['y'])*rscale 
            z = (krep+g16['z'])*rscale
            i=np.where((x>-Lbox*0.5)&(x<Lbox*0.5)&(y>-Lbox*0.5)&(y<Lbox*0.5)&(z>-Lbox*0.5)&(z<Lbox*0.5))
            nnew=len(i[0])
            if (True):
                g0['x'][npart:npart+nnew] = x[i]
                g0['y'][npart:npart+nnew] = y[i]
                g0['z'][npart:npart+nnew] = z[i]
                npart=npart+nnew


print("npart = ",npart, "Lbox = ",Lbox)

if (False):                
    i=np.where(np.fabs(g0['y'])<0.1)
    plt.scatter(g0['vz'][i],g0['z'][i])
    plt.title('vz vs z')
    plt.show()

if (True):                
    i=np.where(np.fabs(g0['y'])<0.1)
    plt.scatter(g0['z'][i],g0['x'][i], s=1e-2)
    plt.title('z vs x')
    plt.show()
           
eps = 0.015
                
#new list
g=makecatg(npart)
g['mass']=g['mass']*0+mgas/munit
g['x']=g0['x'][0:npart]
g['y']=g0['y'][0:npart]
g['z']=g0['z'][0:npart]
g['h']=g['h']*0+eps
g['vz']=g['vz']*0
g['tempg'][:] = 30 #Kelvin 
g['zmetal'][:] = 0 #0.014 solar
#gas metals identically zero, could make a metal version if wanted

s=makecats(1)
mstar=100. #msun trapezium
s['x'][0]=0
s['y'][0]=0
s['z'][0]= 0 
s['mass'][0]=mstar/munit
s['eps'][0]=eps
s['tform'][0]=0. 
s['metals'][0]=0.014 # standard solar

if (True):
    header = h16
    header['time']=0
    header['ngas']=npart
    header['nstar']=1
    header['n']=header['ndark']+header['ngas']+header['nstar']
    d=makecatd(0)
    wtipsy(fileout, header, g, d, s)

