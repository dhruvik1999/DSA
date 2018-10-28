from queue import Queue

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

class BFS:
	def __init__(self,node,graph):
		self.src=0
		self.visited=[]
		self.node=node
		self.graph=graph
		self.queue = Queue()
		self.dis=Queue()
		self.cycle=0
		for i in range(node):
			self.visited.append(0)

	def bfs(self,node):
		self.src=node
		self.queue.enqueue(node)
		self.dis.enqueue(0)
		#self.visit(node)
		while not self.queue.isEmpty():
			temp = self.queue.Back()
			if temp > node:
				if self.visited[temp]==0:
					self.visit(temp)
					for i in self.graph.g[temp]:
						self.queue.enqueue(i)
						self.dis.enqueue(self.dis.Back()+1)
				else:
					self.cycle+=1

			self.queue.dequeue()
			self.dis.dequeue()

	def visit(self,node):
		#print("node : ",node," dis from ",self.src," is : ",self.dis.Back())
		self.visited[node]=1

def main():
	n = int(input("Enter the number of node"))
	e = int(input("Enter the number of edge"))
	#src=int(input("Enter Soource"))
	g1=Graph(n,"al")

	for i in range(e):
		a,b=input().split()
		a=int(a)
		b=int(b)
		g1.insert(a,b)
	bfs=BFS(n,g1)
	visited=bfs.visited
	ans=0
	for i in range(n):
		if visited[i]==0:
			bfs.bfs(i)

	if bfs.cycle==0:
		print("Cycle Not Found!!!")
	else:
		print("Cycle Found!!!  ")

if __name__ == "__main__":
	main()



