class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack ==[]
    
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack==[]:
            print("The stack is Empty")
            return
        self.stack.pop()

    def peek(self):
        if self.stack==[]:
            print("The stack is Empty")
            return
        return self.stack[-1]

    def display(self):
      print(self.stack)

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
s1.pop()
s1.display()
