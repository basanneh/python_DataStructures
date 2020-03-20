class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack =[]


    def enqueue(self,data):
        self.in_stack.append(data)


    def dequeue(self):
        if len(self.out_stack)==0:

            #Move all the data from in_stack to out_stack and then do a pop

            while len(self.in_stack )>0:
                pop_value= self.in_stack.pop()
                self.out_stack.append(pop_value)

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty stack")
                
        return self.out_stack.pop()


s1= QueueTwoStacks()
s1.enqueue(12)
s1.enqueue(1)
s1.enqueue(2)
print(s1.in_stack)
s1.enqueue(3)
s1.enqueue(46)

print(s1.in_stack)
print(s1.dequeue())
print(s1.in_stack)

print(s1.out_stack)
