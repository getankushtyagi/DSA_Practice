# 1 x : Call enqueue(x)
# 2: Call dequeue()
# 3: Call getFront()
# 4: Call isEmpty()
# 5: Call size()


# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.head=None
        self.tail=None
        self._size=0
        

    def isEmpty(self):
        # Return True if queue is empty, else False
        if(self.head):
            return False
        return True
        

    def enqueue(self, x):
        # Add element x to the rear
        new_node=Node(x)
        
        if(self.tail):
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head= new_node
            self.tail= new_node
        self._size+=1

        

    def dequeue(self):
        # Remove the front element
        if self.isEmpty():
            return -1
        val=self.head.data
        self.head=self.head.next
        
        if self.head is None:
            self.tail = None
            
        self._size-=1
        return val
        


    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.isEmpty():
            return -1
        return self.head.data


    def size(self):
        # Return current size
        return self._size
        
        
        