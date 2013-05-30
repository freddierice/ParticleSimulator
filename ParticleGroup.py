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
		self.connections = c or []
		self.particles = p or [Particle(r=5),Particle(r=5)]
		self.pos = pos or (0,0,0)
		div = 2*3.1415926535/self.particleCount
		for i in range(0,self.particleCount):
			self.particles[i].pos = scale3(rotx((1,0,0),div),self.radius)
		if rot:
			for part in self.particles:
				rotx(part,rot[0])
				roty(part,rot[1])
				rotz(part,rot[2])
		
	
	def updateParticles(self):
		for i in range(1,self.particleCount+1):
			p1=self.particles[(i-1)%self.particleCount]
			p2=self.particles[i%self.particleCount]
			r = sub3(p2.pos,p1.pos)
			c=self.connections[i]
			e=c[0]
			k=c[1]
			rs = mag3(r)
			x = e-rs
			a1 = -1*self.dampening*x/(rs*p1.mass)
			a2 = self.dampening*x/(rs*p2.mass)
			p1.acceleration = sum3(p1.acceleration,scale3(a1,p1.acceleration)
			p2.acceleration = sum3(p2.acceleration,scale3(a2,p2.acceleration)
		
