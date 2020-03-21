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
        self._inorder(current_node.lchld)
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

