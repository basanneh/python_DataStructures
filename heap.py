from exceptions import Empty

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
        if self._currentsize == 0:
            raise Empty('Heap is empty')
        return self.data[1]
    


