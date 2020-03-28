#from exceptions import Empty

class Heap:

    def __init__(self):
        self._maxsize = 10
        self._data = [None] * self._maxsize
        self._count = 0

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def maxh(self):
        if self._count == 0:
            print('Heap is empty')
            return
        return self.data[1]
    
    def insert(self,value):
        if self._count == self._maxsize:
            print('No space')
            return
        self._count +=1
        i = self._count
        while i!=1 and value > self._data[i//2]:
            self._data[i] = self._data[i//2]
            i = i // 2
        self._data[i] = value

    def deletemax(self):
        if self._count == 0:
            raise Empty('Heap is Empty')
        x = self._data[1]
        y = self._data[self._count]
        self._count -=1
        i = 1
        ci = 2
        while ci <= self._count:
            if ci < self._count and self._data[ci] < self._data[ci + 1]:
                ci +=1
            if y>= self._data[ci]:
                break
            self._data[i] = self._data[ci]
            i = ci
            ci = ci * 2
        self._data[i] = y


h = Heap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(20)
h.insert(10)
print(h._data)
h.deletemax()
print(h._data)

h.insert(90)
print(h._data)
