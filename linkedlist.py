class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,data):
        self.size +=1
        current = self.head
        temp = Node(data)
        if current is None:
            self.head = temp
        else:
            while(current.next is not None):
                current = current.next
            current.next = temp

    def size(self):
        return self.size

    def insertStart(self,data):
        self.size +=1
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next =self.head
            self.head = temp

    def display(self):
        current = self.head
        if current is None:
            print("The list is empty ")
            return
        else:
            while(current):
                print("%d " %current.data)
                current =current.next

    
l1 =linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.display()
l1.insertStart(5)
l1.display()
l1.insertStart(0)
l1.display()
