class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.length == 0
    
    def push(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        popped_node  = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def peek(self):
        return self.top.value if not self.is_empty() else None
    
    def clear(self):
        self.top = None
        self.length = 0

    def __str__(self):
        current_node = self.top
        values = []
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        return "\n".join(values)
    


new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)

print(new_stack.top.value)
print()
print(new_stack.peek())
print()
print(new_stack)


