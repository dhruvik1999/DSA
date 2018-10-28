class LinkedList:
    def __init__(self):
        self.head=ListNode();
        self.tail=self.head
        self.size=0

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        node=ListNode(x,None)
        if pos.next == None:
            pos.next=node
        else:
            node.next=pos.next
            pos.next=node
        self.size+=1

        
    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        if pos.next!=None:
            pos.next=pos.next.next
            self.size-=1
        else:
            print("Error")
        

    def print(self):
        """ Print all the elements of a list in a row."""
        temp=self.head.next
        while temp!=None:
            print(temp.value)
            temp=temp.next
        

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        counter=0
        temp=self.head
        while counter!=i:
            if temp.next==None:
                print("Index is out of bound..")
                return
            temp=temp.next;
            counter+=1

        temp.next=ListNode(x,temp.next)





    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        while temp!=None:
            if temp.value==x:
                print("Found..")
                return
            temp=temp.next
        print("Value not found..")

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        return self.size;

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.size==0:
            return True
        else:
            return False
        pass


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ')
    L.print()
    L.insert(12,L.head.next)
    print('List is: ')
    L.print()
    L.insert(2,L.head)
    print('List is: ')
    L.print()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ')
    L.print()
    L.delete(L.head.next)
    print('List is: ')
    L.print()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.print()

if __name__ == '__main__':
    main()