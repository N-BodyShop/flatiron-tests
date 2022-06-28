#!/usr/bin/python
import pynbody as pyn
import numpy as np
import matplotlib.pyplot as plt

rp=[]
rhop=[]
pp=[]
vp=[]

for infile in ["evrardcollapse.000030"]:
        sim = pyn.load(infile)
        # Plot raw particle data 
        plt.plot(sim.g['r'], sim.g['rho'], 'r.',markersize=0.05)
        plt.plot(sim.g['r'], sim.g['rho']*sim.g['temp']*.2, 'g.',markersize=0.05)
        plt.plot(sim.g['r'], -sim.g['vr'], 'b.',markersize=0.05)

        # Bin the particle properties at the local resolution dr ~ (m/rho)^(1/3)
        isort=np.argsort(sim.g['r'])
        i=0
        rmin=3e-3
        rmax=max(sim.g['r'])

        r0=min(sim.g['r'])
        dr=(sim.g['mass'][isort[i]]/sim.g['rho'][isort[i]])**.3333333
        while (r0+dr < rmax):
            rnext = r0+dr
            ns=1e-10
            rsum=0.
            rhosum=0.
            psum=0.
            vsum=0.
            while (sim.g['r'][isort[i]]<rnext):
                ns += 1
                rsum += sim.g['r'][isort[i]]
                rhosum += sim.g['rho'][isort[i]]
                psum += sim.g['rho'][isort[i]]*sim.g['temp'][isort[i]]*.2
                vsum += -sim.g['vr'][isort[i]]
                i += 1
            dr=(sim.g['mass'][isort[i]]/sim.g['rho'][isort[i]])**.3333333
            r0 = rnext
            rp.append(rsum/ns)
            rhop.append(rhosum/ns)
            pp.append(psum/ns)
            vp.append(vsum/ns)
        plt.plot(rp, rhop, 'k.')
        plt.plot(rp, pp, 'k.')
        plt.plot(rp, vp, 'k.')
        
        plt.xlabel('position')
        plt.ylabel(r'$\rho$, P, v')
        plt.xlim([rmin,rmax])
        plt.xscale('log')
        plt.yscale('log')
        plt.ylim([1e-2,500])
        plt.title("Evrard (1988) Collapse")
        plt.show()

