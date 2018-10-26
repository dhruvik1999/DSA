class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.height=0
        self.parent=None

class AVL:
    def __init__(self):
        self.root=None
    
    def calHeight(self,node):
        if node==None:
            return -1
        return node.height
    
    def calcBalance(self,node):
        if node==None:
            return 0
        
        return self.calHeight(node.left) - self.calHeight(node.right)
    
    def rotateRight(self,node):

        tempLeftChild = node.left
        t = tempLeftChild.right

        tempLeftChild.right=node
        node.left=t

        tempLeftChild.parent=node.parent
        node.parent=tempLeftChild
        if t != None:
            t.parent=node

        node.height=max(self.calHeight(node.left),self.calHeight(node.right)) + 1
        tempLeftChild.height = max(self.calHeight(tempLeftChild.left),self.calHeight(tempLeftChild.right)) + 1
    
        return tempLeftChild

    def rotateLeft(self,node):

        tempRightChild=node.right
        t=tempRightChild.left

        tempRightChild.left=node
        node.right=t

        tempRightChild.parent=node.parent
        node.parent=tempRightChild
        if t != None:
            t.parent=node

        node.height=max(self.calHeight(node.left),self.calHeight(node.right)) + 1
        tempRightChild.height=max(self.calHeight(tempRightChild.left),self.calHeight(tempRightChild.right)) + 1

        return tempRightChild

    def insert(self,data):
        if self.root == None:
            self.root=Node(data)
        else:
            self.root = self.insertNode(data,self.root,None)
        
    def insertNode(self,data,node,parent):

        if node == None:
            n=Node(data)
            n.parent=parent
            return n
        
        if data > node.data:
            node.right = self.insertNode(data,node.right,node)
        else:
            node.left = self.insertNode(data,node.left,node)
        
        node.height=max(self.calHeight(node.right),self.calHeight(node.left)) + 1
        return self.violationHeight(data,node)

    def violationHeight(self,data,node):
        if self.calcBalance(node) >1 and data < node.left.data:
            #print("L L ",node.data)
            return self.rotateRight(node)
        
        if self.calcBalance(node) < -1 and data > node.right.data:
            #print("R R ",node.data)
            return self.rotateLeft(node)

        if self.calcBalance(node) > 1 and data  > node.left.data:
            
            node.left = self.rotateLeft(node.left)
            #print("L R ",node.data)
            return self.rotateRight(node)
        
        if self.calcBalance(node) < -1 and data < node.right.data:
            node.right = self.rotateRight(node.right)
            #print("R L ",node.data)
            return self.rotateLeft(node)

        return node
    
    def Travarse(self):
        if self.root != None:
            self.InOrder(self.root)
    
    def InOrder(self,node):
        if node.left:
            self.InOrder(node.left)
            
        print(node.data)
        print(node.parent)
        
        if node.right:
            self.InOrder(node.right)

    def minimum(self,node):
        if node==None:
            return

        temp=node
        while temp.left!=None:
            temp=temp.left

        return temp

    def maximum(self,node):
        if node==None:
            return 

        temp=node
        while node.right!=None:
            node=node.right
        return node

    def search(self,data):
        temp=self.root

        while temp!=None:
            if temp.data == data:
                return temp

            if temp.data < data:
                temp=temp.right
            else:
                temp=temp.left

        return Node("Not Exists")

    def successor(self,node):
        if node.data >= self.maximum(self.root).data:
            print("Not Exists")
            return
        
        if node.right!=None:
            return self.minimum(node.right)
        else:
            x=node
            y=node.parent

            while y!=None and y.right==x:
                x=y
                y=y.parent
            return y

    def predecessor(self,node):
        if node.data <= self.minimum(self.root).data:
            print("Not Exists")
            return
        
        if node.left!=None:
            return self.maximum(node.left)
        else:
            x=node
            y=node.parent

            while y!=None and y.left==x:
                x=y
                y=y.left
            return y

    def delete(self,data,node):
        key=self.search(data)
        if node==None:
            return None
        
        if data > key.data:
            node.right=self.delete(data,node.right)
        elif data < key.data:
            node.left=self.delete(data,data.left)
        else:
            if key.left==None and key.right==None:
                if key.data > key.parent.data:
                    key.parent.right=None
                else:
                    key.parent.left=None
                
            elif key.left==None or key.right==None:
            
                if key.data>key.parent.data:
                    if key.left!=None:
                        key.left.parent=key.parent
                        key.parent.right=key.left
                    else:
                        key.right.parent=key.parent
                        key.parent.right=key.right
                else:
                    if key.left!=None:
                        key.left.parent=key.parent
                        key.parent.left=key.left
                    else:
                        key.right.parent=key.parent
                        key.parent.left=key.right
                    
            else:
                p=self.successor(key)
                self.delete(p.data,self.root)
                p.parent=key.parent
                key.data=p.data
                key.parent=p.parent
        
        if not node:
            return node
        
        node.height=max(self.calHeight(node.left),self.calHeight(node.right))+1;
        self.violationHeight(data,node)
        
        
    



avl=AVL()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(7)
avl.insert(6)
avl.insert(-1)
avl.insert(8)
avl.insert(9)
avl.insert(10)
avl.insert(11)
avl.insert(12)
print(avl.maximum(avl.root).data)
print(avl.minimum(avl.root).data)
print("element found!!!!",avl.search(4))
avl.delete(4,avl.root)
avl.Travarse()
print(avl.search(4).data)
