from math import *

def dot(v1,v2):
	"""dot product"""
	m = 0
	for i in range(0,len(v1)):
		m += v1[i]*v2[i]
	return m

def dot3(u,v):
	"""3 dimensional dot product"""
	return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def cross(u,v):
	"""cross product"""
	return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])

def mag(a):
	"""magnitude of vector"""
	m = 0
	for k in a:
		m += k*k
	return sqrt(m)

def mag3(a):
	"""magnitude of vector (optomized for 3 dimensions)"""
	return sqrt(pow(a[0],2) + pow(a[1],2) + pow(a[2],2)) 

def proj(a,b):
	"""projection of a onto b"""
	k = mag(b)
	if(k == 0):
		return (0,0,0)
	return scale(b,dot(a,b)/pow(k,2))

def proj3(a,b):
	"""projection of a onto b (optomized for 3 dimensions)"""
	k = mag3(b)
	if(k == 0):
		return (0,0,0)
	return scale3(b,dot3(a,b)/pow(k,2))

def flatten3(x,n):
	"""flattens b component of a vector. (Solve[ Dot[a-lambda*b]==0,lambda]) """
	d = dot3(n,n)
	if d == 0:
		return (0,0,0) #cannot flatten (division by zero)
	return sum3(x,scale3(n,-1*(mag3(x)/d)))

def scale(v,a):
	"""scales vector v by scalar a"""
	k = []
	for n in v:
		k.append(n*a)
	return tuple(k)

def scale3(v,a):
	"""scales vector v by scalar a (optomized for 3 dimensions)"""
	return (v[0]*a, v[1]*a, v[2]*a)

def dist(a,b):
	"""find the distance between the two coords """
	t = 0
	for i in range(0,len(a)):
		t += pow((a[i]-b[i]),2)
	return sqrt(t)

def dist3(a,b):
	"""find the distance between the two coords (optomized for 3 dimensions)"""
	return sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2)+pow(a[2]-b[2],2))

def distn3(a,b):
	"""find the distance between the two coords (no root) (optomized for 3 dimensions)"""
	return pow(a[0]-b[0],2)+pow(a[1]-b[1],2)+pow(a[2]-b[2],2)

def sum3(a,b):
	"""add vector components (optomized for 3 dimensions)"""
	return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def dif3(a,b):
	"""subtract vector components (optomized for 3 dimensions)"""
	return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
