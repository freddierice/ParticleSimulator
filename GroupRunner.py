from visual import *
import time
import threading
from ParticleGroup import *
from Vector import *
from Particle import *

class GroupRunner(threading.Thread):
	"""Runs the groups"""
	
	def __init__(self,b=None):
		"""Initializes the runner"""
		threading.Thread.__init__(self)
		self.groups = []
		self.bounds = b or [(-150,150),(-150,150),(-150,150)]
	
	def add(self,g):
		"""Add a group to the system"""
		self.particles.append(g)
	
	def stop(self):
		"""Stops the group runner thread"""
		return
	
	def run(self):
		"""Thread runner"""
		oldTime = time.time()
		while True:
			dt = time.time()-oldTime
			if( dt == 0 or len(self.particles) == 0 ): #many algorithms depend on dt != 0
				continue
			oldTime = time.time()
			
			self.wallCollide()
			self.interGroupInteraction()
			
			for p in self.particles:
				p.velocity = sum3(p.velocity, scale3(p.acceleration,dt))
				p.pos = sum3(p.pos, scale3(p.velocity, dt))
			time.sleep(0.00001)

	def interGroupInteraction(self):
		for g in self.groups:
			g.updateParticles()
	
	def wallCollide(self):
		for g in self.groups:
			for p in g.particles:
				for i in range(0,3):
					if p.pos[i] + p.radius > self.bounds[i][1]:
						if p.velocity[i] < 0:
							continue
						temp = list(p.velocity)
						temp[i] = -1*wallCr*temp[i]
						p.velocity = tuple(temp)
					elif p.pos[i] - p.radius < self.bounds[i][0]:
						if p.velocity[i] > 0:
							continue
						temp = list(p.velocity)
						temp[i] = -1*wallCr*temp[i]
						p.velocity = tuple(temp)

