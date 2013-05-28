from visual import *
import time
import threading
from Tree import *
from Vector import *
from Particle import *

class ParticleGroup():
	"""Runs the Particles"""
	
	def __init__(self,n=None,s=None):
		"""Initializes the runner"""
		self.particleCount = n or 2
		self.connectionStrengths = s or []
		self.bounds = b or [(-150,150),(-150,150),(-150,150)]
	
	def updateParticles(self):
		for p in self.particles:
			