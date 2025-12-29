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
    
    def insert_at_end(self,data):
        new_node=Node(data)
        curr=self.head
        if(curr is None):
            self.head=new_node
            return
            
        while curr.next:
            curr=curr.next
            
        curr.next=new_node
        new_node.prev=curr
    
    def delete_head(self):
        if(self.head is None):
            return
        
        current=self.head.next
        self.head.next=None
        self.head.prev=None
        self.head=current
        
                
    def print(self):
        curr = self.head
        while(curr):
            print(curr.val, end="=>")         
            curr=curr.next 
        print("\n")
                        
                        
dll=DoublyLinkedList()
# dll.insert_at_head(1)
# dll.insert_at_head(2)
# dll.insert_at_head(3)
# dll.insert_at_head(4)

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_end(6)

dll.delete_head()




dll.print()