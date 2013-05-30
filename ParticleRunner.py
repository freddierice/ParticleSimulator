from visual import *
import time
import threading
from Tree import *
from Vector import *
from Particle import *
from ParticleGroup import *

class ParticleRunner(threading.Thread):
	"""Runs the Particles"""
	
	def __init__(self,b=None,p=None,g=None):
		"""Initializes the runner"""
		threading.Thread.__init__(self)
		self.particles = p or []
		self.bounds = b or [(-100,100),(-100,100),(-100,100)]
		self.groups = g or []
	
	def add(self,p):
		"""Add a particle to the system"""
		self.particles.append(p)
	
	def addGroup(self,g):
		self.groups.append(g)
		for p in g.particles:
			self.add(p)
	
	def stop(self):
		"""Stops the particle runner thread"""
		return
	
	def run(self):
		"""Thread runner"""
		oldTime = time.time()
		while True:
			dt = time.time()-oldTime
			if( dt == 0 or len(self.particles) == 0 ): #many algorithms depend on dt != 0
				continue
			oldTime = time.time()
			
			self.updateGravity()
			self.updateCharge()
			self.basicCollide()
			self.wallCollide()
			self.doGroup()
			
			for p in self.particles:
				p.velocity = sum3(p.velocity, scale3(p.acceleration,dt))
				p.pos = sum3(p.pos, scale3(p.velocity, dt))
			time.sleep(0.00001)
	
	def doGroup(self):
		for g in self.groups:
			g.updateParticles()
	
	def basicDoCollision(self,collisions):
		p1 = collisions[0]
		ps = collisions[1:]
		dv = (0,0,0)
		v0 = tuple(p1.velocity)
		for p2 in ps:
			norm = dif3(p2.pos,p1.pos)
			v1 = proj3(p1.velocity,norm)
			v2 = proj3(p2.velocity,norm)
			dot1_2 = dot3(v1,v2)
			dot1_n = dot3(v1,norm)
			dot2_n = dot3(v2,norm)
			mag1 = mag3(v1)
			mag2 = mag3(v2)
			if(dot1_2 < 0): 
				"""if velocities are going different directions"""
				if(dot1_n < 0):
					"""and the first particle is going away from the other"""
					continue
			else:
				"""if the velocities are in the same direction"""
				if abs(dot1_n) < abs(dot2_n):
					"""p1 is going too slow"""
					if(dot1_n > 0):
						"""p1 is going towards p2"""
						continue
				if abs(dot1_n) > abs(dot2_n):
					"""p2 is going to slow"""
					if(dot1_n < 0):
						"""p1 is going away from p2"""
						continue
			v0 = flatten3(v0,norm)
			v3 = ( (Cr*p2.mass*(v2[0]-v1[0])+p1.mass*v1[0]+p2.mass*v2[0])/(p1.mass+p2.mass),
                   (Cr*p2.mass*(v2[1]-v1[1])+p1.mass*v1[1]+p2.mass*v2[1])/(p1.mass+p2.mass),
                   (Cr*p2.mass*(v2[2]-v1[2])+p1.mass*v1[2]+p2.mass*v2[2])/(p1.mass+p2.mass) )
			dv = sum3(dv,v3)
		return sum3(v0, dv)

	def basicCollide(self):
		collisions = []
		for p1 in self.particles:
			col = []
			for p2 in self.particles:
				if not p1 == p2:
					if areColliding(p1,p2):
						col.append(p2)
			if not len(col) == 0:
				col.insert(0,p1)
				collisions.append(col)
		if not len(collisions) == 0:
			velos = []
			for c in collisions:
				velos.append((c[0],self.basicDoCollision(c)))
			for v in velos:
				v[0].velocity = v[1]
	
	def wallCollide(self):
		for p in self.particles:
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

	def updateCharge(self):
		accel = (0,0,0)
		for i in range(0,len(self.particles)):
			p1 = self.particles[i]
			for j in range(i+1,len(self.particles)):
				p2 = self.particles[j]
				if p1.charge != 0 or p2.charge != 0:
					norm = dif3(p2.pos, p1.pos)
					normMag = mag3(norm)
					f = ke * p2.charge * p1.charge / distn3(p1.pos,p2.pos)
					p1.acceleration = sum3(p1.acceleration, scale3(norm, -1*f/(p1.mass*normMag)))
					p2.acceleration = sum3(p2.acceleration, scale3(norm, f/(p2.mass*normMag)))

	def updateGravity(self):
		for p in self.particles:
			p.acceleration = sum3(g,p.aStart)