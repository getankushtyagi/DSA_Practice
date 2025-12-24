class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
        


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.tail=new_node
            self.head=new_node
        
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
    
            
            
            
ll=LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_beginning(4)
ll.insert_at_end(15)

ll.print_list()


