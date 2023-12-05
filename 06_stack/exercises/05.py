class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.move_elements()
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        self.move_elements()
        return self.stack2[-1] if self.stack2 else None

    def empty(self):
        return not self.stack1 and not self.stack2

    def move_elements(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
