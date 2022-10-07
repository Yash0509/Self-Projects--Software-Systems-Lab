class Heap:
    """
    Heap Class is made
    """
    def __init__(self, cap):
        """
        This is constructor
        
        :param cap: integer
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """
        This is parent function which finds parent element
        
        :param i: integer
        
        :return: integer
        """
        return (i - 1) // 2
    
    def left(self, i):
        """
        This is left function which finds left element
        
        :param i: integer
        
        :return: integer
        """
        return (2 * i) + 1
    
    def right(self, i):
        """
        This is right function which finds right element
        
        :param i: integer
        
        :return: integer
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """
        This is insert function which performs insertion operation to insert element in heap.
        
        :param val: integer
        """
        if self.n != self.M:
            self.H[self.n] = val
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """
        This is min function which performs operation to extract minimum value from heap
        
        :return: integer
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """
        This is Heapify function which sorts Heap in bottom up or top down manner
        
        :param root: integer
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """
        This is deleteMin function which performs deletion operation to delete minimum value from heap.
        
        """
        if n > 0:
            if n == 1:
                self.H = []
                n = 0
            else:
                n -= 1
                self.H[0] = self.H[n]
                self.Heapify(0)