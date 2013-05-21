#Tree class file
class Tree():
	"""A generic Tree class"""
	def __init__(self, v=None, p=None, c=None, e=None):
		"""Initialize the tree with a particle"""
		self.value = v or None
		self.children = c or []
		self.parent = p or None
		self.explorer = e or False
	
	def addChild(self,t):
		"""Add a child to the tree"""
		self.children.append(t)
	
	def isLeaf(self):
		"""Returns true if the tree is a leaf node"""
		return len(self.children) == 0
	
	def isRoot(self):
		"""Returns true if the tree is a root"""
		return self.parent == None

	def isExplorer(self):
		return self.explorer
	
	def setExplorer(self,e):
		self.explorer = e
