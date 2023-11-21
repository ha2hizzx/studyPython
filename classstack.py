class Stack:
    def __init__(self, size = 5):
        self.size = size
        self.my_stack=[None]*size
        self.top = -1
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def isFull(self):
        if self.top == self.size - 1:
            return True
        return False
    
    def push(self, data):
        if not self.isFull():
            self.top += 1
            self.my_stack[self.top] = data

    def pop(self):
        if not self.isEmpty():
            r = self.my_stack[self.top]
            del self.my_stack[self.top]
            self.top -= 1
            return r
        
    def peak(self):
        if not self.isEmpty():
            return self.my_stack[self.top]
        
    def clear(self):
        if not self.isEmpty():
            self.my_stack=[None]*self.size
            self.top = -1

    def stackSize(self):
        return self.top
    
    def lastpush(self):
        if not self.isEmpty():
            return self.my_stack[self.top]
    def reverse(self):
        if not self.isEmpty():
            reverse = reversed(self.my_stack)
            print(*reverse)





stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.reverse()
print(stack.lastpush())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())