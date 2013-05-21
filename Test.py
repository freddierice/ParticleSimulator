from Tree import *

class dummy():
	def __init__(self,a):
		self.a = a

f = [dummy(1), dummy(3), dummy(2), dummy(6), dummy(4), dummy(4), dummy(5)]
e = []
r = Tree(v=f[5])
e.append(f[5])
f.remove(f[5])

fillCollisionTree(f,e,r)

print r.children