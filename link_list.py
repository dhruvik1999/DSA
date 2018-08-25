class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkList:
	def __init__(self):
		self.head = None
		self.size=0
		self.tail=None

	def denote_head(self):
		Ghead=self.head

	def insert_first(self,data):
		node = Node(data)
		if self.head==None:
			self.head = node
			self.tail=node
		else:
			node.next=self.head
			self.head = node
		self.size+=1

	def print_all(self):
		temp=self.head
		while temp!=None:
			print(temp.data)
			temp=temp.next

	def insert_last(self,data):
		node=Node(data)
		if self.tail==None:
			self.tail=node
		else:
			self.tail.next=node
		self.size+=1

	def delete_first(self):
		self.head=self.head.next
		self.size-=1

	def delete_last(self):
		temp=self.head
		for i in range(self.size):
			if i==self.size-2:
				temp.next=None
				self.size-=1
			else:
				temp=temp.next


	def size1(self):
		return self.size;

ll=LinkList()
ll.insert_first(1)
ll.insert_first(2)
ll.insert_first(3)
ll.insert_last(0)
ll.delete_last()
#ll.delete_first()
ll.print_all()
print("size is :",ll.size1())

