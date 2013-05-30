from visual import *
from random import *
from Vector import *

"""Globals"""
spaceStart = (-50, -50, -50)
spaceEnd   = ( 50,  50,  50)
minRadius  = 0.1
maxRadius  = 10
minMass = 5
maxMass = 30
Cr = 1 	#coefficient of restitution
wallCr = .5
ke = 8987551787
g = (0,-9.81,0)

class Particle(vis.primitives.sphere):
	"""Particle class derived from VPython Sphere"""
	def __init__(self, p=None, m=None, r=None, v=None, a=None, q=None):
		super(vis.primitives.sphere, self).__init__()
		self.pos = p or (uniform(spaceStart[0],spaceEnd[0]),uniform(spaceStart[1],spaceEnd[1]),uniform(spaceStart[2],spaceEnd[2]))
		self.mass = m or uniform(minMass, maxMass)
		self.radius = r or uniform(minRadius,maxRadius)
		self.velocity = v or (0,0,0)
		self.acceleration = a or (0,0,0)
		self.aStart = a or (0,0,0)
		self.color = (uniform(0,1),uniform(0,1),uniform(0,1))
		self.charge = q or 0

def areColliding(p1,p2):
	return dist3(p1.pos,p2.pos) < p1.radius + p2.radius

