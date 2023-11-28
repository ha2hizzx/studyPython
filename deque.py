class Deque:
    def __init__(self, capacity=6):
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == self.rear:
            print("비어있습니다.")
            return True
        return False
    
    def isFull(self):
        if (self.rear + 1) % self.capacity == self.front:
            print("꽉 찼습니다.")
            return True
        return False

    def addRear(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.list[self.rear] = e
            print(self.list)

    def addFront(self, e):
        if not self.isFull():
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.list[self.front] = e
            print(self.list)

    def deleteFront(self):
        if not self.isEmpty():
            r = self.list[self.front]
            self.list[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return r

    def deleteRear(self):
        if not self.isEmpty():
            r = self.list[self.rear]
            self.list[self.rear] = None
            self.rear = (self.rear - 1) % self.capacity
            return r

    def getFront(self):
        if not self.isEmpty():
            return self.list[(self.front+1) % self.capacity]
        
    def getRear(self):
        if not self.isEmpty():
            return self.list[self.rear]

A = Deque()
A.addFront(1)
A.addFront(2)
A.addRear(3)
A.addRear(4)
A.addRear(5)
print(A.getFront())
print(A.getRear())
print(A.deleteFront())
print(A.deleteFront())
print(A.deleteRear())
print(A.deleteRear())
print(A.deleteRear())