class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        
        if(self.tail):
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.tail=new_node
            self.head=new_node
    
    def insert_in_between(self,target,data):
        new_node=Node(data)
        current=self.head
        while(current):
            if(current.val==target):
                new_node.next=current.next
                current.next=new_node
                return
            else:
                current=current.next
                
    def before_node(self,target,data):
        new_node=Node(data)
        curr=self.head
        
        while(curr):
            if(curr.next.val==target):
                new_node.next=curr.next
                curr.next=new_node
                return
            else:
                curr=curr.next
                    
    def print(self):
        curr = self.head
        while(curr):
            print(curr.val, end="=>")         
            curr=curr.next 
        print("\n")           



    
ll=LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_end(14)
ll.insert_at_end(15)

ll.print()

# ll.insert_in_between(12,16)

# ll.print()

ll.before_node(14,16)

ll.print()
