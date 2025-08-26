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
        new_mode = Node(value)
        if not self.head:
            self.head = new_mode
            self.tail = new_mode
        else:
            new_mode.next = self.head
            self.head = new_mode
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
            # print(temp_node.value)
            temp_node.next = new_node
        return True

    
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
new_linked_list.insert(2,30)
print(new_linked_list)

# 10 -> 20 -> 40 -> 50