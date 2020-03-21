from collections import deque
class Node(object):

    def __init__(self,data):
        self.data= data
        self.lchild = None
        self.rchild = None

class bst(object):

    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self,x):
        self.root = self._insert(self.root, x)

    
    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        elif x < p.data:
            p.lchild = self._insert(p.lchild,x)
        elif x > p.data:
            p.rchild = self._insert(p.rchild,x)
        else:
            print(x, " already present in the tree")
        return p
#### Inorder traversal
    def inorder(self):
        self._inorder(self.root) 
        print() 
    def _inorder(self,current_node):
        if current_node is None:
            return
        self._inorder(current_node.lchild)
        print (current_node.data, " ")
        self._inorder(current_node.rchild)

        ## Preorder traversal
    def preorder(self):
        self._preorder(self.root)
        print()


    def _preorder(self,current_node):
        if current_node is None:
            return
        print(current_node.data, " ")
        self._preorder(current_node.lchild)
        self._preorder(current_node.rchild)

        ## Postorder Traversal

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,current_node):

        if current_node is None:
            return 
        self._postorder(current_node.lchild)
        self._postorder(current_node.rchild)
        print(current_node.data, " ")
    
    def level_order(self):
        
        if self.root is None:
            print("Tree is Empty")
            return
        qu = deque()
        qu.append(self.root)

        while len(qu) !=0:
            p = qu.popleft()
            print(p.data, " ",end='')
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)

    ## Minimum value
    def minvalue(self):
        current = self.root
        if current is None:
            return
        while(current.lchild is not None):
            current = current.lchild

        return current.data
    ## Max value
    def maxvalue(self):
        current = self.root
        if current is None:
            return
        while(current.rchild is not None):
            current.rchild = current
        
        return current.data

    
bst = bst()
bst.insert(50)
bst.insert(7)
bst.insert(40)
bst.insert(30)
bst.insert(20)
bst.insert(10)
bst.insert(60)
bst.insert(70)
bst.insert(80)
bst.insert(90)
bst.insert(100)
print("Level Order Traversal : ")
bst.level_order()
print()
bst.insert(50)
print("Minimum value in the Binary Search Tree is : ",bst.minvalue())
#print("Inorder Traversal: ",inorder_t)
