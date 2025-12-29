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
    
    def insert_in_between(self,data,target):
        new_node=Node(data)
        count=1
        current=self.head
        while current:
            if(count == target):
                new_node.next=current.next
                new_node.prev=current
                current.next=new_node
                return
            count+=1
            current=current.next    
                
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

dll.insert_in_between(6,2)

dll.print()