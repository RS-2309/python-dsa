class MaxHeap:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        if len(self.heap) == 1:
            return
        
        return self.__heapify_up(len(self.heap)-1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        minimum = self.heap.pop()

        self.__heapify_down()

        return minimum

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def __heapify_up(self, index):
        while index != 0:
            if self.heap[index] <= self.heap[(index-1)//2]:
                return True
            
            else:
                index_new = (index - 1)//2
                self.heap[index], self.heap[index_new] = self.heap[index_new], self.heap[index]
                return self.__heapify_up(index_new)

    def __heapify_down(self, index = 0):
        if 2*index + 2 >= len(self.heap) and 2*index + 1 < len(self.heap):
            if self.heap[index] >= self.heap[2*index+1]:
                return True
            self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
            return True
        
        if 2*index + 1 >= len(self.heap):
            return True
        
        if self.heap[2*index + 1] <= self.heap[2*index+2]:
            if self.heap[index] >= self.heap[2*index+2]:
                return True
            self.heap[index], self.heap[2*index+2] = self.heap[2*index+2], self.heap[index]
            return self.__heapify_down(2*index+2)
        
        if self.heap[2*index + 1] >= self.heap[2*index+2]:
            if self.heap[index] >= self.heap[2*index+1]:
                return True
            self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
            return self.__heapify_down(2*index+1)