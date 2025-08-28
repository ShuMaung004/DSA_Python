class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CS_linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1


    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1


    def insert(self,index,value):
        if index > self.length or index < 0:
            raise Exception("Index out of bound")
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1


    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.value)+ " " ,end= " ")
            temp_node = temp_node.next
            if temp_node.next == self.head:
                print() #new line
                break


    def search(self, target):
        temp_node = self.head
        while temp_node:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    
    def get(self, index):
        if index >= self.length or index < -1:
            raise Exception("Index out of bound exception")
        elif index == -1:
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
        

    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    
    def pop_first(self):
        temp = self.head
        if self.head == None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.tail.next = self.head
        self.length -= 1
        return temp
    
    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            temp_node = self.head
            while temp_node.next is not self.head:
                temp_node = temp_node.next
            temp_node.next = self.head
            self.tail = temp_node
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            raise Exception("index out of bound")
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove_all(self):
        if self.length == 0:
            return
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        values = []
        while temp_node:
            values.append(str(temp_node.value))
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return " -> ".join(values)
    

new_cs_linked_list = CS_linkedList()
new_cs_linked_list.append(10)
new_cs_linked_list.append(20)
new_cs_linked_list.append(30)
new_cs_linked_list.append(40)

print(new_cs_linked_list)
