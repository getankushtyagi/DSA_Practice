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
        
    # brute force 
    # def reverse(self):
    #     temp=self.head
    #     stack=[]
    #     while(temp is not None):
    #         stack.append(temp.val)
    #         temp=temp.next
            
    #     temp=self.head
    #     while(temp is not None):
    #         tempval=stack.pop()
    #         temp.val=tempval
    #         temp=temp.next
    
    #  optimal approach       
    def reverse(self):
        curr=self.head
        prev=None
        if(curr.next is None):
            return curr
        
        while(curr is not None):
            # store next
            next_node=curr.next
            
            # swap pointers 
            curr.next=prev
            curr.prev=next_node
            
            # move forward
            prev=curr
            curr=next_node
        self.head = prev
    
        
                
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

dll.print()

dll.reverse()

dll.print()
