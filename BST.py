class Node:
    def __init__(self,data=None):
        self.parent=None
        self.data=data
        self.left=None
        self.right=None
​
class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root == None:
            self.root=Node(data)
        else:
            temp=self.root
            parent=None
            while temp != None:
                if data <= temp.data:
                    parent=temp
                    temp=temp.left
                else:
                    parent=temp
                    temp=temp.right
            node=Node(data)
            node.parent=parent
            if parent.data < data:
                parent.right=node
            else:
                parent.left=node
            temp=node
​
    def serch(self,key):
        temp=self.root
        while temp != None:
            if temp.data == key:
                return temp
            
            if temp.data < key:
                temp=temp.right
            else:
                temp=temp.left
            
        return None
    
    def delete(self,key):
        #print(key)
        
        if key.left==None and key.right==None:
            if key.data > key.parent.data:
                key.parent.right=None
            else:
                key.parent.left=None
                
        elif key.left==None or key.right==None:
            
            if key.data>key.parent.data:
                if key.left!=None:
                    key.parent.right=key.left
                else:
                    key.parent.right=key.right
            else:
                if key.left!=None:
                    key.parent.left=key.left
                else:
                    key.parent.left=key.right
                    
        else:
            p=self.successor(key).data
            self.delete(self.successor(key))
            key.data=p
    
    def successor(self,ref):
        if ref.right!=None:
            return self.minimum(ref.right)
        else:
            x=ref
            y=ref.parent
            
            while y!=None and y.right==x:
                x=y
                y=y.parent
                print(y.data)
            return y
​
    def predisessor(self,ref):
        if ref.left!=None:
            return self.maximum(ref.left)
        else:
            x=ref
            y=ref.parent
            
            while y!=None and y.left==x:
                x=y
                y=y.parent
            
            return y
    
    def inorder(self,ref):
        if ref is None:
            return
        self.inorder(ref.left)
        print(ref.data)
        self.inorder(ref.right)     
        
    def minimum(self,ref):
        temp=ref
        while temp.left!=None:
            temp=temp.left
        return temp
        
    def maximum(self,ref):
        temp=ref
        while temp.right!=None:
            temp=temp.right
        return temp
​

​
