from visual import *
import time
import threading
from Tree import *
from Vector import *
from Particle import *

#bounds are (equilibrium position, k)

class ParticleGroup():
	"""Runs the Particles"""
	
	def __init__(self,n=None,c=None,r=None,p=None,pos=None,rot=None,d=None):
		"""Initializes the runner"""
		self.particleCount = n or 2
		self.radius = r or 20
		self.dampening = d or 1
		if self.particleCount < 2:
			self.particleCount = 2
		self.connections = c or [(3,1),(3,1)]
		self.particles = p or [Particle(r=5),Particle(r=5)]
		self.pos = pos or (0,0,0)
		div = 2*3.1415926535/self.particleCount
		for i in range(0,self.particleCount):
			self.particles[i].pos = scale3(roty((1,0,0),div*i),self.radius)
		if rot:
			for part in self.particles:
				part.pos = rotx(part.pos,rot[0])
				part.pos = roty(part.pos,rot[1])
				part.pos = rotz(part.pos,rot[2])
		
	
	def updateParticles(self):
		for i in range(1,self.particleCount+1):
			p1=self.particles[(i-1)%self.particleCount]
			p2=self.particles[i%self.particleCount]
			r = dif3(p2.pos,p1.pos)
			c=self.connections[i-1]
			e=c[0]
			k=c[1]
			rs = mag3(r)
			x = e-rs
			if x == 0:
				continue
			a1 = -1*self.dampening*x/(rs*p1.mass)
			a2 = self.dampening*x/(rs*p2.mass)
			p1.acceleration = sum3(p1.acceleration,scale3(r,a1))
			p2.acceleration = sum3(p2.acceleration,scale3(r,a2))
		
