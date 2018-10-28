from Graph import Graph
from queue import Queue

class BFS:
	def __init__(self,node,graph):
		self.src=0
		self.visited=[]
		self.node=node
		self.graph=graph
		self.queue = Queue()
		self.dis=Queue()
		for i in range(node):
			self.visited.append(0)

	def bfs(self,node):
		self.src=node
		self.queue.enqueue(node)
		self.dis.enqueue(0)
		#self.visit(node)
		while not self.queue.isEmpty():
			temp = self.queue.Back()
			if self.visited[temp]==0:
				self.visit(temp)
				for i in self.graph.g[temp]:
					self.queue.enqueue(i)
					self.dis.enqueue(self.dis.Back()+1)
			self.queue.dequeue()
			self.dis.dequeue()

	def visit(self,node):
		print("node : ",node," dis from ",self.src," is : ",self.dis.Back())
		self.visited[node]=1




def main():
	n = int(input("Enter the number of node"))
	e = int(input("Enter the number of edge"))
	src=int(input("Enter Soource"))
	g1=Graph(n,"al")

	for i in range(e):
		a,b=input().split()
		a=int(a)
		b=int(b)
		g1.insert(a,b)
	bfs=BFS(n,g1)
	bfs.bfs(src)

if __name__ == "__main__":
	main()