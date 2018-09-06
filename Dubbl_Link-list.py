class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insertFirst(self,data):
        node=Node(data)
        if self.head is None:
            self.head=self.tail=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node

    def insertLast(self,data):
        node=Node(data)
        if self.tail is None:
            self.head=self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
        
    def printh_t(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def printt_h(self):
        temp=self.tail
        while temp!=None:
            print(temp.data)
            temp=temp.prev

ll=DLinkedList()
ll.insertFirst(10)
ll.insertFirst(20)
ll.insertFirst(30)
ll.insertLast(0)
ll.printt_h()
#ll.printh_t()
        