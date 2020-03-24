class HeapEmptyError(Exception):
    pass

class Heap:

    def __init__(self,maxSize=10):
        self.a =[None]*maxSize
        self.n = 0
        self.a[0] = 99999

    def insert(self, value):
        self.n +=1
        self.a[self.n] = value
        self.restor_up(self.n)

    def restor_up(self,i):
        k = self.a[i]  #current value
        iparent = i //2 #parent of current value

        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i=iparent
            iparent =i //2
        self.a[i] = k


    def delete_root(self):
        if self.n ==0:
            raise HeapEmptyError("Heap is empty")


