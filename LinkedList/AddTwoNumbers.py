class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
        


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.value, end="=>")
            curr=curr.next
        print("None")
        
    def insert_at_end(self,data):
        new_node=Node(data)
        
        if(self.tail):
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.tail=new_node
            self.head=new_node
    
    def add_two_numbers(self, l1, l2):
        
            
            
            
l1=LinkedList()
l1.insert_at_end(5)
l1.insert_at_end(7)
l1.insert_at_end(8)

l2=LinkedList()
l2.insert_at_end(6)
l2.insert_at_end(4)
l2.insert_at_end(7)

l1.print_list()
l2.print_list()

