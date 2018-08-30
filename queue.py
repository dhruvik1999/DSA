class Node:
	def __init__(self,data):
		self.data= data
		self.next= None

class Queue:
	def  __init__(self):
		self.head=None
		self.tail=None
		self.size=-1

	def enqueue(self,data):
		node=Node(data)
		if self.head==None:
			self.head=node
			self.tail=node
		else:
			self.head.next=node
			self.head=node
		self.size+=1

	def dequeue(self):
		if self.tail==None:
			print("Queue is Empty:<")
		elif self.size==0:
			self.head=None
			self.tail=None
			self.size-=1
		else:
			self.tail=self.tail.next
			self.size-=1

	def isEmpty(self):
		if self.size==-1:
			return True
		return False

	def Front(self):
		if(self.isEmpty()):
			#print("Stack is Empty")
			return;
		else:
			return self.head.data

	def Back(self):
		if(self.isEmpty()):
			#print("Stack in Empty")
			return;
		else:
			return self.tail.data

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
print(queue.Front())
print(queue.Back())
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.Front())
queue.enqueue(2)
print(queue.Front())
print(queue.Back())

