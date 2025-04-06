class Queue:
    def __init__(self):
        self.data = []
    def push(self, element):
        self.data.append(element)
    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]
    def pop(self):
        if len(self.data) == 0:
            self.data = []
            return None
        to_return = self.data[0]
        self.data = self.data[1:]
        return to_return
    def size(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
class MyStack:

    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()

    def push(self, x: int) -> None:
        self.second_queue.push(x)
        while not self.first_queue.is_empty():
            self.second_queue.push(self.first_queue.pop())

        self.first_queue, self.second_queue = self.second_queue, self.first_queue
        

    def pop(self) -> int:
        return self.first_queue.pop()

    def top(self) -> int:
        return self.first_queue.peek()
        

    def empty(self) -> bool:
        return self.first_queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()