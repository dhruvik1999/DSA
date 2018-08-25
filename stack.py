class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head=None
		self.size=-1

	def push(self,data):
		node = Node(data)
		if self.head==None:
			self.head = node
		else:
			node.next=self.head
			self.head=node
		self.size+=1

	def pop(self):
		if self.head==None:
			print("Stack is Empty")
			return;

		if self.head.next==None:
			top=self.head.data
			self.head=None
		else:
			top=self.head.data
			self.head=self.head.next
		self.size-=1
		return top

	def top(self):
		if self.head!=None:
			return self.head.data
		else:
			return "No Data"

	def isEmpty(self):
		if self.size==-1:
			return True
		else:
			return False

stack = Stack()
stack.pop()
stack.push(1)
print(stack.top())
stack.pop()
print(stack.top())
if stack.isEmpty():
	print("Empty")
else:
	print("Not Empty")

stack.push(2)
print(stack.top())
