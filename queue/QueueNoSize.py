class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self,value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        return "There is not element is Queue List" if self.isEmpty() else self.items.pop(0)
    
    def peek(self):
        return "There is not element is Queue List" if self.isEmpty() else self.items[0]
    
    def delete(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
    
    

