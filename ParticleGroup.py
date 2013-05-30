from visual import *
import time
import threading
from Tree import *
from Vector import *
from Particle import *

#bounds are (equilibrium position, k)

class ParticleGroup():
	"""Runs the Particles"""
	
	def __init__(self,n=None,c=None,r=None,p=None,pos=None):
		"""Initializes the runner"""
		self.particleCount = n or 2
		self.radius = r or 20
		if self.particleCount < 2:
			self.particleCount = 2
		self.connections = c or []
		self.particles = p or []
		self.pos = pos or (0,0,0)
		circ = 2*radius*3.1415926535
		div = circ / self.particleCount
		
	
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
			a1 = -1*x/(rs*p1.mass)
			a2 = x/(rs*p2.mass)
			p1.acceleration = sum3(p1.acceleration,scale3(a1,p1.acceleration)
			p2.acceleration = sum3(p2.acceleration,scale3(a2,p2.acceleration)