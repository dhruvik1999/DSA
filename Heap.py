class Heap(object):

	def __init__(self,heapSize=10):
		self.heapSize=heapSize
		self.heap=[0]*heapSize
		self.curruntPosition=-1

	def insert(self,item):
		if self.isFull():
			print("Heap is full")
			return
		else:
			self.curruntPosition+=1
			self.heap[self.curruntPosition]=item
			self.fixup(self.curruntPosition);


	def isFull(self):
		if self.curruntPosition==self.heapSize:
			return True
		else:
			return False

	def fixup(self,index):
		parentIndex=(index-1)//2

		while parentIndex>=0 and self.heap[parentIndex] < self.heap[index]:
			self.heap[index],self.heap[parentIndex]=self.heap[parentIndex],self.heap[index]
			#
			index=parentIndex
			parentIndex=(parentIndex-1)//2

	def heapsort(self):

		for i in range(0,self.curruntPosition+1):
			temp=self.heap[0]
			print(temp )
			self.heap[self.curruntPosition-i],self.heap[0]=self.heap[0],self.heap[self.curruntPosition-i]
			self.fixDown(0,self.curruntPosition-i-1)

	def extractMax(self):
		temp=self.heap[0]
		#print(temp )
		self.heap[self.curruntPosition],self.heap[0]=self.heap[0],self.heap[self.curruntPosition]
		self.curruntPosition-=1
		self.fixDown(0,self.curruntPosition)
		return temp

	def show(self):
		for i in range(self.curruntPosition+1):
			print(self.heap[i])




	def fixDown(self,index,upto):
		while index <= upto:
			leftChild=2*index+1
			rightChild=2*index+2

			if leftChild < upto:
				childToSwap=None

				if rightChild>upto:
					childToSwap=leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap=leftChild
					else:
						childToSwap=rightChild

				if self.heap[index] < self.heap[childToSwap]:
					self.heap[index],self.heap[childToSwap]=self.heap[childToSwap],self.heap[index]
				else:
					break

				index = childToSwap
			else:
				break


if __name__ == "__main__":
	heap=Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)
	heap.show()

