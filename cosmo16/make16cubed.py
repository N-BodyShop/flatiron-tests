import numpy as np
from pytipsy import *

#Omegam=0.3086 OmegaLambda=0.6914,ns=0.9611,sigma8=0.8288  (Planck 2014)
#Omegab=0.048
#h=0.6666667
#Box 100 Mpc = 66.6667/h
#a=0.037 T ~ 23-37 K so 30 K start seems ok
#Z start = 0
#density = 0.0481 in code units

omegam=0.3086 
omegab=0.048
n1d=16
catg=makecatg(n1d**3)
a=(np.arange(0,n1d)+.5)/n1d-0.5
(z,y,x) = np.meshgrid(a,a,a)
catg['x']=np.reshape(x,(n1d**3))
catg['y']=np.reshape(y,(n1d**3))
catg['z']=np.reshape(z,(n1d**3))
catg['mass']=catg['mass']*0.+omegab/n1d**3  #total mass = Omegab
catg['h']=catg['h']*0.+0.333/n1d
catg['tempg']=catg['tempg']*0.+30. #30 K
catg['dens']=catg['dens']*0.+omegab

catd=makecatd(n1d**3)
catd['mass']=catd['mass']*0.+(omegam-omegab)/n1d**3  #total mass = Omegab
catd['eps']=catd['eps']*0.+0.333/n1d
catd['x']=catg['x']
catd['y']=catg['y']
catd['z']=catg['z']

header=makeheader(1/100.,2*n1d**3,3,n1d**3,n1d**3,0)

wtipsy("cosmo16cubed.std", header, catg, catd, 0)

