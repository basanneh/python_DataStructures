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
    
    def insert(self,data):
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




