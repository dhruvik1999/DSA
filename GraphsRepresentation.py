










def main():
    n=int(input("Enter number of vertices: "))
    m=int(input("Enter number of edges: "))
    print("Input ",m," edges")
    adjmat=[[0]*n for i in range(n)]
    adjlist=[[] for i in range(n)]
    #print(adjlist)
    
    for i in range(m):
        x, y=(map(int,input().split()))
        #(x)
        #print(y)
        #print(x+y)
        adjmat[x][y]=1
        adjmat[y][x]=1
        adjlist[x].append(y)
        adjlist[y].append(x)
    print("The list is")
    for i in range(n):
        print(i,end=": ")
        print(adjlist[i])
    #print(adjlist)
    print("The matrix is")
    for i in range(n):
        print(adjmat[i])








if __name__=="__main__":
    main()