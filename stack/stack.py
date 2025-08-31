class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,element):
        self.items.append(element)

    def pop(self):
        return self.items.pop() if not self.is_empty() else "Stack is Empty"
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else "Stack is Empty"
    
    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        if self.is_empty():
            return "Stack is Empty"
        values = [str(x) for  x in reversed(self.items)]
        return "\n".join(values)
    
    

new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.pop()
print(new_stack)
print(new_stack.peek())