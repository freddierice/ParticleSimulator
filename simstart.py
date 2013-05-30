#!/usr/bin/env python
import time
from visual import *
from Particle import *
from ParticleRunner import *
from random import *

if __name__ == "__main__":
	"""Contains the main function of the program"""
	
	scene = display(title='Particles Colliding', width=1200, height=700,
                     center=(0,0,0), background=(0,0,0))
	#scene.autoscale = False
	#scene.range = (25,25,25)
	
	runner = ParticleRunner()
	
	parts = []
	for i in range(0,40):
		parts.append(Particle(r=15,m=1,q=0.01))
		parts[i].velocity = (uniform(-100,100),uniform(-100,100),uniform(-100,100))
		#parts[i].velocity = (0,0,0)
		runner.add(parts[i])
	
	"""
	
	c1 = Particle(p=(10,10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c2 = Particle(p=(-10,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c3 = Particle(p=(-10,10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c4 = Particle(p=(10,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	
	runner.add(c1)
	runner.add(c2)
	runner.add(c3)
	runner.add(c4)
	
	
	
	p1 = Particle(p=(0,10,0),v=(0,0,0),m=10,r=1,a=(0,0,0), q=-0.0001)
	p2 = Particle(p=(0,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0),q=0.0001)
	#p3 = Particle(p=(0,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	
	runner.add(p1)
	runner.add(p2)
	#runner.add(p3)
	"""
	runner.start()
	
	"""
	a = (1,1,1)
	b = (-1,0,-1)
	c = proj3(a,b)
	print c
	"""
	
	a = raw_input()
	
	scene = display(title='Particles Colliding2', width=1200, height=700,
                     center=(0,0,0), background=(0,0,0))

	