from BinaryTree import BinaryTree
def buildParseTree(expr):
    expr=expr.split()
    tree=BinaryTree(' ')
    current=tree
    for i in expr:
        if i == '(':
            if current.leftChild==None:
                current.insertLeft(' ')
            current=current.leftChild
        elif i in ['+','-','*','/']:
            current.setRootVal(i)
            if current.rightChild==None:
                current.insertRight(' ')
            current=current.rightChild
        elif i not in ['+','-','*','/'] and i != ')':
            current.setRootVal(int(i))
            current=current.parent
        elif i==')':
            current=current.parent
    return tree

def printPrefix(tree):
    Tree=tree
    a=[]
    def preorder(tree):
        if tree!=None:
            a.append(tree.key)
            preorder(tree.leftChild)
            preorder(tree.rightChild)
        if tree==None:
            return
    preorder(Tree)
    return a


def printPostfix(tree):
    a=[]
    def postorder(tree):
        if tree!=None:
            if tree.leftChild!=None:
                postorder(tree.leftChild)
            if tree.rightChild!=None:
                postorder(tree.rightChild)
            a.append(tree.key)
    postorder(tree)
    return a


def operate(a,b,op):
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='/':
        return a/b
    if op=='*':
        return a*b


def evaluate(tree):
    if tree.key in ['+','-','/','*']:
        a=evaluate(tree.leftChild)
        b=evaluate(tree.rightChild)
        c=operate(a,b,tree.key)
        return c
    else:
        return tree.key
    pass

def main():
    exp=input("Input fully paranthesized expression: ")
    tree=buildParseTree(exp)
    print("Prefix: ",printPrefix(tree))
    print("Postfix: ",printPostfix(tree))
    print("The evaluated expression is ",evaluate(tree))



if __name__=='__main__':
    main()

