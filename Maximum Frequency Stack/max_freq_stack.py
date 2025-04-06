class FreqStack:

    def __init__(self):
        self.data = {}
        self.max_number = 0
        self.elements = {}

    def push(self, val: int) -> None:
        if val not in self.elements:
            self.elements[val] = 0
        else:
            self.elements[val] += 1
        self.max_number = max(self.max_number, self.elements[val])
        if not self.elements[val] in self.data:
            self.data[self.elements[val]] = [val]
        else:
            self.data[self.elements[val]].append(val)


    def pop(self) -> int:
        if len(self.data[self.max_number]) == 0:
            self.max_number -= 1
        element_to_delete = self.data[self.max_number].pop()
        self.elements[element_to_delete] -= 1
        return element_to_delete
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()