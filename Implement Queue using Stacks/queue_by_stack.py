class Stack:
    def __init__(self):
        self.data = []
    def push(self, element):
        self.data.append(element)
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0

class MyQueue:

    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, x: int) -> None:
        self.first_stack.push(x)

    def pop(self) -> int:
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self) -> int:
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.peek()

    def empty(self) -> bool:
        return self.first_stack.is_empty() and self.second_stack.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()