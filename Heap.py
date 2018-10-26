class MaxHeap:
    def __init__(self,items=[]):
        self.heap=[0]
        self.size=1
        for i in items:
            self.heap.append(i)
            self.size=self.size+1
            self.floatUp(self.size-1)
    def push(self,data):
        self.heap.append(data)
        self.size=self.size+1
        self.floatUp(self.size-1)
    def getMax(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    def extractMax(self):
        if self.size>2:
            self.swap(1,self.size-1)
            #max=self.heap.pop()
            #print("Im here")
            max=self.heap[self.size-1]
            self.size=self.size-1

            
            self.heapify(1)
        elif self.size==2:
            max=self.heap.pop()
        else:
            max=False
        return max
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def floatUp(self,index):
        parent=index//2
        if index<=1:
            return
        elif self.heap[index]>self.heap[parent]:
            self.swap(index,parent)
            self.floatUp(parent)
    def heapify(self,index):
        left=index*2
        right=index*2+1
        largest=index
        if self.size>left and self.heap[largest]<self.heap[left]:
            largest=left
        if self.size>right and self.heap[largest]<self.heap[right]:
            largest=right
        if largest!=index:
            self.swap(index,largest)
            self.heapify(largest)
    def printHeap(self):
        print(str(self.heap[1:self.size]))


def heapSort(m):
    M=MaxHeap(m.heap[1:m.size])
    size=M.size
    for i in range(size-2):
        M.extractMax()
    print("The sorted array is")
    print(str(M.heap[1:]))

    
"""m = MaxHeap([95, 3, 21])
m.push(10)
m.printHeap()
print(str(m.extractMax()))
m.printHeap()
print(str(m.extractMax()))
m.extractMax()
m.extractMax()
#m.extractMax()
print("The actual heap is")
m.printHeap()

heapSort(m)
#print("The full heap is")
#print(str(m.heap[1:]))
"""
m=MaxHeap([10,20,30,40,50,25])
m.printHeap()
m.push(60)
print("After inserting: ")
m.printHeap()


heapSort(m)
print("The maximum is",m.extractMax())
#print("Im here")
#m.printHeap()

