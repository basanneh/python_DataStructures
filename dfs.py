
class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjList= []
        self.visited = False
        self.predecessor = None

class DepthFirstSearch(object):
    def dfs(self,node):
        node.visited = True
        print(node.name, end=" ")
        for n in node.adjList:
            if not n.visited:
                self.dfs(n)



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjList.append(node2)

node2.adjList.append(node3)
node2.adjList.append(node4)
node4.adjList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)
print()


