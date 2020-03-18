class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue ==[]


    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop()

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)
       
    def display(self):
        return self.queue

q1 = Queue()
q1.enqueue(23)
q1.enqueue(12)
q1.enqueue(13)
print(q1.peek())
print(q1.display())
