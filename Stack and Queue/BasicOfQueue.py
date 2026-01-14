class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.items=[]
        self.size=n

    
    def isEmpty(self):
        # Check if queue is empty
        if(len(self.items)==0):
            return True
        else:
            return False

    
    def isFull(self):
        # Check if queue is full
        if(len(self.items)==self.size):
            return True
        return False

    
    def enqueue(self, x):
        if(self.isFull()):
            return -1
        self.items.append(x)

    
    def dequeue(self):
        # Dequeue
        if(self.isEmpty()):
            return -1
        return self.items.pop(0)

    # we only need to return not the pop
    def getFront(self):
        # Get front element
        if(self.isEmpty()):
            return -1
        return self.items[0]
       
    # we only need to return not the pop
    def getRear(self):
        # Get rear element 
        if(self.isEmpty()):
            return -1
        return self.items[-1]
        
        