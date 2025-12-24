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
        
    def find_element(self,element):
        curr=self.head
        i=0
        while curr:
            if(curr.data==element):
                return i
            
            curr=curr.next
            i+=1     
        
    
    
    
    
ll=LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_end(14)
ll.insert_at_end(15)

ll.print()

print(ll.find_element(14))
# ll.print()