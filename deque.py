class Deque:
    #덱을 초기화하는 함수 frotn 와 rear 모두 -1에서부터 시작한다.
    def __init__(self, capacity=6):
        self.capacity = capacity
        self.list = [None]*capacity
        self.front = -1
        self.rear = -1
    #front와 rear가 같은지 유무를 반환하여 비어있는지 확인할수있는 함수이다.
    def isEmpty(self):
        if self.front == self.rear:
            print("비어있습니다.")
            return True
        return False
    #rear의 +1이 front와 같은지 유무를 반환하여 꽉 찾는지 확인할수있는 함수이다.
    def isFull(self):
        if (self.rear + 1) % self.capacity == self.front:
            print("꽉 찼습니다.")
            return True
        return False

    #꽉차지 않았을때 rear을 한칸 늘리고 그 위치에 데이터를 삽입하는 함수이다.
    def addRear(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.list[self.rear] = e
            print("Rear")
            print(self.list)
    #꽉차지 않았을때 front를 한칸 늘리고 그 위치에 데이터를 삽입하는 함수이다.
    def addFront(self, e):
        if not self.isFull():
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.list[self.front] = e
            print("Front")
            print(self.list)
    #덱이 비어있지 않을때 현재 front위치의 값을 r에 저장하고 front의 값을 None으로 한 뒤 front를 한칸 줄이고 r을 반환하는 함수이다.
    def deleteFront(self):
        if not self.isEmpty():
            r = self.list[self.front]
            self.list[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return r

    #덱이 비어있지 않을때 현재 rear위치의 값을 r에 저장하고 rear의 값을 None으로 한 뒤 rear를 한칸 줄이고 r을 반환하는 함수이다.
    def deleteRear(self):
        if not self.isEmpty():
            r = self.list[self.rear]
            self.list[self.rear] = None
            self.rear = (self.rear - 1+ self.capacity) % self.capacity
            return r
    #front위치의 값을 반환한다.
    def getFront(self):
        if not self.isEmpty():
            return self.list[self.front]
    #rear위치의 값을 반환한다.
    def getRear(self):
        if not self.isEmpty():
            return self.list[self.rear]

    def init(self):
	#덱을 초기화 합니다. 리스트의 모든 요소가 None이 되며 front와 rear가 -1이 됩니다.
        if not self.isEmpty():
            self.list = [None]*self.capacity
            self.front = -1
            self.rear = -1
    #덱의 요소 개수를 계산해서 덱의길이를 반환합니다.
    def getLength(self):
        length = (self.rear - self.front + self.capacity) % self.capacity
        return length
    #덱에서 가장 큰 요소를 반환한다.
    def getMax(self):
        max = self.list[self.front]
        for i in range(self.capacity):
            if self.list[i] is not None and self.list[i] > max:
                max = self.list[i]
        return max




A = Deque()
A.addFront(1)
A.addFront(2)
A.addRear(3)
A.addRear(4)
A.addRear(5)
A.getLength()
A.addRear(6)
print(A.getMax())
print(A.getFront())
print(A.getRear())
print(A.deleteFront())
print(A.deleteFront())
print(A.deleteRear())
print(A.deleteRear())
print(A.deleteRear())
A.init()