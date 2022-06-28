#!/usr/bin/python
import pynbody as pyn
import numpy as np
import matplotlib.pyplot as plt

xp=[]
rhop=[]
pp=[]
vp=[]
xmin=-8
xmax=8

for infile in ["shocktube.000400"]:
        sim = pyn.load(infile)
        # Plot raw particle data 
        plt.plot(sim.g['x'], sim.g['rho'], 'r.',markersize=0.1)
        plt.plot(sim.g['x'], sim.g['rho']*sim.g['temp']*.4, 'g.',markersize=0.1)
        plt.plot(sim.g['x'], sim.g['vx'], 'b.',markersize=0.1)

        # Bin the particle properties at the local resolution dx ~ (m/rho)^(1/3)
        isort=np.argsort(sim.g['x'])
        i=0
        xs=min(sim.g['x'])
        while (xs < xmax):
            dx=(sim.g['mass'][isort[i]]/sim.g['rho'][isort[i]])**.3333333
            xnext = xs+dx
            ns=0
            xsum=0.
            rhosum=0.
            psum=0.
            vsum=0.
            while (sim.g['x'][isort[i]]<xnext):
                ns += 1
                xsum += sim.g['x'][isort[i]]
                rhosum += sim.g['rho'][isort[i]]
                psum += sim.g['rho'][isort[i]]*sim.g['temp'][isort[i]]*.4
                vsum += sim.g['vx'][isort[i]]
                i += 1
            xs = xnext
            xp.append(xsum/ns)
            rhop.append(rhosum/ns)
            pp.append(psum/ns)
            vp.append(vsum/ns)
        plt.plot(xp, rhop, 'r.')
        plt.plot(xp, pp, 'g.')
        plt.plot(xp, vp, 'b.')
        
        plt.xlabel('position')
        plt.ylabel(r'$\rho$, P, v')
        plt.xlim([xmin,xmax])
        plt.ylim([-.1,1.1])
        plt.title(infile)
        plt.show()

