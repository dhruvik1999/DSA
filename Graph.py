class Graph:
	def __init__(self,node,tp="al"):
		self.node=node
		self.g=[]
		self.type=tp
		self.num_edge=0

		if self.type=="al":
			for i in range(0,node):
				self.g.append([])
		else:
			for i in range(0,node):
				req=[]
				for j in range(0,node):
					req.append(0)
				self.g.append(req)


	def insert(self,p1,p2):
		if self.num_edge <= self.node*(self.node-1)/2:
			if self.type=="al":
				if not p1 in self.g[p2]:
					self.g[p1].append(p2);
					self.g[p2].append(p1);
					return
			else:
				self.g[p1][p2]=1
				self.g[p2][p1]=1
			self.num_edge+=1
			return True
		else:
			return False

	def show(self):
		if self.type=="al":
			for i in range(0,self.node):
				print("Ver ",i," ",self.g[i])
		else:
			for i in range(0,self.node):
				print(self.g[i])

def main():

	n = int(input("Enter the number of node"))
	e = int(input("Enter the number of edge"))
	g1=Graph(n,"al")
	g2=Graph(n,"am")

	for i in range(e):
		a,b=input().split()
		a=int(a)
		b=int(b)
		g1.insert(a,b)
		g2.insert(a,b)

	g1.show()
	print("")
	g2.show()


if __name__ == "__main__":
	main()