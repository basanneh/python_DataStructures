class Node(object):
    
    def __init__(self,value):
        self.data = value
        self.lchild = None
        self.rchild = None

class Bst(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,node):
        if data < node.data:
            if node.lchild:
                self._insert(data,node.lchild)
            else:
                node.lchild = Node(data)
        elif data > node.data:
            if node.rchild:
                self._insert(data,node.rchild)
            else:
                node.rchild = Node(data)

        else:
            print("Cannot have Duplicates")


bst = Bst()
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
bst.insert(90)

