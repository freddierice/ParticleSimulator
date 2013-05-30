#!/usr/bin/env python
import time
from visual import *
from Particle import *
from ParticleRunner import *
from ParticleGroup import *
from random import *

if __name__ == "__main__":
	"""Contains the main function of the program"""
	
	scene = display(title='Particles Colliding', width=1200, height=700,
                     center=(0,0,0), background=(0,0,0))
	scene.autoscale = False
	scene.range = (300,300,300)
	
	runner = ParticleRunner()
	
	"""
	parts = []
	for i in range(0,40):
		parts.append(Particle(r=15,m=1))
		parts[i].velocity = (uniform(-100,100),uniform(-100,100),uniform(-100,100))
		parts[i].velocity = (0,0,0)
		runner.add(parts[i])
	
	
	
	c1 = Particle(p=(10,10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c2 = Particle(p=(-10,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c3 = Particle(p=(-10,10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	c4 = Particle(p=(10,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	
	runner.add(c1)
	runner.add(c2)
	runner.add(c3)
	runner.add(c4)
	
	"""
	"""
	p1 = Particle(p=(0,5,0),v=(0,2,0),m=20,r=1,a=(0,-2,0))
	p2 = Particle(p=(0,0,0),v=(0,4,0),m=10,r=1,a=(0,0,0))
	#p3 = Particle(p=(0,-10,0),v=(0,0,0),m=10,r=1,a=(0,0,0))
	
	runner.add(p1)
	runner.add(p2)
	#runner.add(p3)
	
	
	"""
	p1 = Particle(r=1,m=1)
	p2 = Particle(r=1,m=1)
	p3 = Particle(r=1,m=1)
	p4 = Particle(r=1,m=1)
	
	q1 = Particle(r=1,m=1)
	q2 = Particle(r=1,m=1)
	q3 = Particle(r=1,m=1)
	q4 = Particle(r=1,m=1)
	q5 = Particle(r=1,m=1)
	q6 = Particle(r=1,m=1)
	
	g1 = ParticleGroup(r=5,p=[p1,p2,p3,p4],c=[(5.5,10),(5.5,10),(5.5,10),(5.5,10)],n=4,rot=(1,1,1))
	g2 = ParticleGroup(r=10,p=[q1,q2,q3,q4,q5,q6],c=[(11.5,10),(11.5,10),(11.5,10),(11.5,10),(11.5,10),(11.5,10)],n=6,rot=(0,0,0))
	
	
	runner.addGroup(g1)
	runner.addGroup(g2)
	
	
	
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

	