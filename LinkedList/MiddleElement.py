class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.next=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head:
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=new_node
            self.tail=new_node
    def print(self):
        curr = self.head
        while(curr):
            print(curr.data, end="=>")         
            curr=curr.next 
        print("\n")
        
    def find_middle(self):
        Length=0
        curr =self.head
        while(curr):
            Length+=1
            curr=curr.next
        print("length of Linked List",Length)
        
        val=self.head
        i=0
        while(val):
            if(i==Length/2):
                return val.data
            i+=1
            val =val.next
            
                
        
        
ll=LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_end(14)
ll.insert_at_end(15)
ll.insert_at_end(16)
ll.insert_at_end(17)
ll.insert_at_end(18)

ll.print()

print(ll.find_middle())
        
        
        