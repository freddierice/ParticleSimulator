	def fillCollisionTree(self,frontier,explored,root):
		"""Fills in a collision tree, assuming that the
		   leaf is not in the frontier or the explored"""
		nextExplored = list(explored)
		for i in range(0,len(frontier)):
			if areColliding(frontier[i], root.value):
				if frontier[i] in explored:
					root.addChild(Tree(v=frontier[i],p=root,e=False))
				else:
					root.addChild(Tree(v=frontier[i],p=root,e=True))
					nextExplored.append(frontier[i])
		for child in root.children:
			if not child.value in explored:
				frontier.remove(child.value)
				self.fillCollisionTree(frontier, nextExplored, child)
				frontier.append(child.value)
		explored = nextExplored

	def collide(self,p1,parts):
		dv = (0,0,0)
		v0 = tuple(p1.velocity)
		for p2 in parts:
			p2 = p2.value
			norm = dif3(p2.pos,p1.pos)
			v1 = proj3(p1.velocity,norm)
			if dot3(v1,norm) < 0: #if the ball is moving away already, don't reverse it!
				continue
			v0 = flatten(v0,norm)
			v2 = proj3(p2.velocity,norm)
			v3 = ( (Cr*p2.mass*(v2[0]-v1[0])+p1.mass*v1[0])/(p1.mass+p2.mass),
                   (Cr*p2.mass*(v2[1]-v1[1])+p1.mass*v1[1])/(p1.mass+p2.mass),
                   (Cr*p2.mass*(v2[2]-v1[2])+p1.mass*v1[2])/(p1.mass+p2.mass) )
			dv = sum3(dv,v3)
		p1.velocity = sum3(v0, dv)

	def doCollisionTree(self,t):
		if not t.isLeaf():
			if t.isRoot():
				self.collide(t.value,t.children)
			else:
				temp = list(t.children)
				temp.append(t.parent)
				self.collide(t.value,temp)
			for i in range(0,len(t.children)):
				self.doCollisionTree(t.children[i])
		elif t.isExplorer():
			self.collide(t.value,[t.parent])

	def updateCollision(self,dt):
		f = list(self.particles)
		e = []
		collisions = []
		while len(f) > 0:
			#print "Delta T: " + str(dt)
			#print "Frontier: " + str(f)
			#print "Explored: " + str(e)
			e.append(f[0])
			t = Tree(v=f[0])
			f.remove(f[0])
			self.fillCollisionTree(f,e,t)
			collisions.append(t)
			#print "Collisions: " + str(collisions)
		for i in range(0, len(collisions)):
			self.doCollisionTree(collisions[i])