class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            self.head.prev=new_node
        self.head=new_node
    
    def middle(self):
        if(self.head.next is None):
            return self.head
        
        slow = self.head
        fast=self.head
        
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        
        print(slow.val)
            
    def print(self):
        curr = self.head
        while(curr):
            print(curr.val, end="=>")         
            curr=curr.next 
        print("\n")
                        
                        
dll=DoublyLinkedList()
dll.insert_at_head(1)
dll.insert_at_head(2)
dll.insert_at_head(3)
dll.insert_at_head(4)
dll.insert_at_head(5)
dll.insert_at_head(6)
dll.insert_at_head(7)

dll.print()

dll.middle()