class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        return True

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self,target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return True
            current = current.next
            index += 1
        return False
    
    def get(self,index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_values(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
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
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = None
        self.length -= 1
        return popped_node
    
    def remove(self,index ):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()
        prev_node = self.get(index - 1)
        prev_node.next = popped_node.next
        popped_node = prev_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = []
        temp_node = self.head
        while temp_node:
            result.append(str(temp_node.value))
            temp_node = temp_node.next
        return "->".join(result)
    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(40)
new_linked_list.append(50)
# new_linked_list.insert(2,30)
# print(new_linked_list)
# new_linked_list.search(50)
# print(" ==== " ,new_linked_list.search(50))
new_linked_list.traverse()

# 10 -> 20 -> 40 -> 50