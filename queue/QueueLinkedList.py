class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node
    
    def isEmpty(self):
        return self.linkedList.head is None
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no Node in the Queue"
        else:
            temp_node = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp_node.value   
    
    def peek(self):
        return self.linkedList.head.value if not self.isEmpty() else "There is not any node in the Queue"
    
    def delete(self):
        self.linkedList = LinkedList()   

        
custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
custQueue.enqueue(4)
print(custQueue)    
print(custQueue.dequeue()) 
print(custQueue.peek())    
