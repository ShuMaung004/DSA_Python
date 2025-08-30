class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CircularlyDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    def reverse_traverse(self):
        if not self.tail:
            return
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break
    
    def search(self, target):
        if not self.head:
            return False
        temp_node = self.head
        while temp_node:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds")
            return
        if index == 0:
            self.prepend(value)
            return 
        if index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        prev_node = self.get(index - 1)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        if not self.head:
            return "Empty list"
        current_node = self.head
        values = []
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " <---> ".join(values)


# Example usage
new_cdll = CircularlyDoublyLinkedList()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.append(40)
print(new_cdll)         
new_cdll.remove(2)
print(new_cdll)        
