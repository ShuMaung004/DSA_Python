class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1
    
    def get(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bound")
        if index > self.length // 2:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        return current

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Index out of bound")

        if index == 0:
            self.prepend(value)
            return 
        if index == self.length:   # inserting at the end
            self.append(value)
            return

        new_node = Node(value)
        prev_node = self.get(index-1)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1
    
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
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

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <--> "
            temp_node = temp_node.next
        return result



newDLL = DoublyLinkedList()
newDLL.append(10)
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
print(newDLL)           
newDLL.insert(2, 50)
print(newDLL)           
removed = newDLL.remove(3)
print("Removed:", removed)  
print(newDLL)           
