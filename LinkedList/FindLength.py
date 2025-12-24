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
        
    def delete_head(self):
        self.head=self.head.next
        
    def find_length(self):
        count=0
        curr =self.head
        while(curr):
            count+=1
            curr=curr.next
        return count
            
        
        
    
    
    
    
ll=LinkedList()
ll.insert_at_end(12)
ll.insert_at_end(13)
ll.insert_at_end(14)
ll.insert_at_end(15)

ll.print()

# ll.delete_head()
# ll.print()

print('length of linked list',ll.find_length())