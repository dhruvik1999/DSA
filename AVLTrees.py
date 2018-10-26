class TreeNode(object): 
    def __init__(self, val=None): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1 
        self.parent=None
    def __str__(self):
        return str(self.val)
class AVL_Tree(object): 
    def insert(self, root, key): 
        if root is None: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 
        balance = self.getBalance(root) 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root)  
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 
    def search(self,root,key):
        if root==None:
            print("Not found")
            valu=None
            #return False
        elif key<root.val:
            valu=self.search(root.left,key)
        elif key>root.val:
            valu=self.search(root.right,key)
        else:
            print("Found")
            valu=root
            #return True
        return valu
    def successor(self,root,val):
        valu=self.search(root,val)
        if valu==None:
            #print("Im here")
            return None
        else:
            if valu.right is not None:
                return self.minimum(valu.right)
            succ=None
            while root is not None:
                if valu.val < root.val:
                    succ=root
                    root=root.left
                elif valu.val>root.val:
                    root=root.right
                else:
                    break
            return succ
    def predecessor(self,root,val):
        valu=self.search(root,val)
        if valu==None:
            return None
        else:
            if valu.left is not None:
                return self.maximum(valu.left)
            succ=None
            while root is not None:
                if root.val<valu.val:
                    succ=root
                    root=root.right
                elif valu.val<root.val:
                    root=root.right
                else:
                    break
                return succ
                pass





        
    def delete(self, root, key): 
        if root is None: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right,temp.val) 
        if root is None: 
            return root 
  
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 

        balance = self.getBalance(root) 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root)  
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 
    def leftRotate(self, z): 
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.right = T2 
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 
  
    def rightRotate(self, z): 
        y = z.left 
        T3 = y.right 
        y.right = z 
        z.left = T3 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 
  
    def getHeight(self, root): 
        if root is None: 
            return 0
        return root.height 
  
    def getBalance(self, root): 
        if root is None: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
        if root==None: 
            return
        print(root.val,end=" ") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
    def inOrder(self,root):
        if root==None:
            return
        self.inOrder(root.left)
        print(root.val,end=" ") 
        self.inOrder(root.right)
    def minimum(self,root):
        if root.left==None:
            print("Minimum is",root.val)
            return root
        else:
            self.minimum(root.left)
    def maximum(self,root):
        if root.right==None:
            print("Maximum is",root.val)
            return root
        else:
            self.maximum(root.right)



class AVL:
    def __init__(self):
        self.root=None
        self.tree=AVL_Tree()
    def insert(self,val):
        self.root=self.tree.insert(self.root,val)
    def preOrder(self):
        self.tree.preOrder(self.root)
    def inOrder(self):
        self.tree.inOrder(self.root)
    def delete(self,val):
        self.root=self.tree.delete(self.root,val)
    def search(self,val):
        self.tree.search(self.root,val)
    def minimum(self):
        self.tree.minimum(self.root)
    def maximum(self):
        self.tree.maximum(self.root)
    def successor(self,val):
        valu=self.tree.successor(self.root,val)
        print("The successor of", val,"is",valu)
    def predecessor(self,val):
        valu=self.tree.predecessor(self.root,val)
        print("The predecessor of",val,"is",valu)
        pass

mytree=AVL()

#print(type(mytree.tree))
mytree.insert(10)
mytree.insert(20)
mytree.insert(30)
mytree.insert(40)
mytree.insert(50)
mytree.insert(25)
mytree.successor(20)
mytree.predecessor(20)
mytree.insert(10)
mytree.preOrder()
print ()
mytree.search(10)
mytree.minimum()
mytree.delete(10)
mytree.delete(10)
mytree.minimum()
mytree.search(10)
mytree.inOrder()
print ()
mytree.search(25)