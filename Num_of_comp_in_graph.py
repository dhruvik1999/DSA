from Graph import Graph
from BFS import BFS

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
			ans+=1
			bfs.bfs(i)

	print("Number of Comp : ",ans);

if __name__ == "__main__":
	main()

