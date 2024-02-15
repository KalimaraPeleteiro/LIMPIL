class Stack():

    def __init__(self, size):
        self.buffer = [0 for _ in range(size)]
        self.pointer = -1

    def push(self, number):
        self.pointer += 1
        self.buffer[self.pointer] = number
    
    def pop(self):
        number = self.buffer[self.pointer]
        self.pointer -= 1
        return number
    
    def top(self):
        return self.buffer[self.pointer]