class Stack:
    def __init__(self, size = 5):
		#STACK의생성자로 스택의 크기를 정의하고 스택을 초기화한다. STACK을 생성할때 size에대한 입력값이 없으면 size는 5가된다. 
        self.size = size
        self.my_stack=[None]*size
        self.top = -1
    def isEmpty(self):
		#스택이 비어있는지 확인한다.
        if self.top == -1:
            return True
        return False
    def isFull(self):
		#스택이 가득 찼는지 확인한다.
        if self.top == self.size - 1:
            return True
        return False
    
    def push(self, data):
		#data를 스택 맨 위에 추가한다.
        if not self.isFull():
            self.top += 1
            self.my_stack[self.top] = data

    def pop(self):
		#스택 맨 위의 데이터를 제거하고 반환한다.
        if not self.isEmpty():
            r = self.my_stack[self.top]
            del self.my_stack[self.top]
            self.top -= 1
            return r
        
    def peak(self):
		#스택 맨 위의 데이터를 반환한다. 
        if not self.isEmpty():
            return self.my_stack[self.top]
        
    def clear(self):
		#스택의 모든 요소를 제어한다. top을 -1로 초기화한다.
        if not self.isEmpty():
            self.my_stack=[None]*self.size
            self.top = -1

    def stackSize(self):
		#스택의 현재 크기인 현재 요소의 수를 반환한다.
        return self.top + 1
   
    def stackPrint(self):
		#스택의 모든 요소를 출력한다.
        if not self.isEmpty():
            print(*self.my_stack)
    def stackReverse(self):
		#스택을 역순으로 바꾼다.
        if not self.isEmpty():
            self.my_stack.reverse()
    def stackSort(self):
		#스택을 정렬한다.
        if not self.isEmpty():
            self.my_stack.sort()




stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.stackPrint()
stack.stackReverse()
stack.stackPrint()
stack.stackSort()

print(stack.peak())
print(stack.stackSize())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.stackReverse()
stack.stackPrint()
print(stack.pop())
stack.clear()