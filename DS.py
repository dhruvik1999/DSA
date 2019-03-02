class Node:
	def  __init__(self,data):
		self.data = data
		self.parent=self
		self.rank=0

class DisjointS:
	def __init__(self,n):
		self.vert=[]
		
		for i in range(n):
			self.vert.append(Node(i))

	def makeSet(self,a):
		a=self.vert[a]
		self.vert[a] = Node(a);
		return True


	def findSet(self,a):
		a = self.vert[a]
		if a!=a.parent:
			a = self.findSet(a.parent.data)
		return a

	def union(self,a,b):
		a=self.findSet(a)
		b=self.findSet(b)
		if a != b:
			if b.rank > a.rank:
				a.parent=b
			elif b.rank < a.rank:
				b.parent=a
			else:
				b.parent=a
				a.rank+=1
		else:
			return False

		return True

def main():
	n=6
	ds = DisjointS(6)
	ds.union(0,1)
	ds.union(0,2)
	ds.union(2,3)
	ds.union(4,5)

	print(0,ds.findSet(0).data)
	print(1,ds.findSet(1).data)
	print(2,ds.findSet(2).data)
	print(3,ds.findSet(3).data)
	print(4,ds.findSet(4).data)
	print(5,ds.findSet(5).data)

	ds.union(3,5)

	print(0,ds.findSet(0).data)
	print(1,ds.findSet(1).data)
	print(2,ds.findSet(2).data)
	print(3,ds.findSet(3).data)
	print(4,ds.findSet(4).data)
	print(5,ds.findSet(5).data)



if __name__ == "__main__":
	main();




