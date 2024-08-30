##Two pointer solution
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None for _ in range(k)]
        self.left = -1
        self.right = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty(): ## DO NOT FORGET
            self.left = 0
            self.right = 0
        else:
            self.right = (self.right + 1) % self.capacity

        self.queue[self.right] = value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.left == self.right: ## DO NOT FORGET
            self.left = -1
            self.right = -1
            return True
        
        self.left = (self.left + 1) % self.capacity
        return True
        
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.right]

    def isEmpty(self) -> bool:
        return True if self.right == -1 else False

    def isFull(self) -> bool:
        if (self.right + 1) % self.capacity == self.left:
            return True
        return False