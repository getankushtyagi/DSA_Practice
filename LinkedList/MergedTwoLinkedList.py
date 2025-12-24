class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
        
    def mergeTwoList(self,List1,List2):
        if List1.head is None:
            return List2
        if List2.head is None:
            return List1
        
        List1.tail.next=List2.head
        List1.tail=List2.tail
        return List1
        
    def print_list(self):
        current=self.head
        
        while(current):
            print(current.value, end="=>")
            current=current.next
        print("None")
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.tail=new_node
            self.head=new_node
            
            
        
l1=LinkedList()
l1.insert_at_beginning(10)
l1.insert_at_beginning(9)
l1.insert_at_beginning(8)



        
l2=LinkedList()
l2.insert_at_beginning(13)
l2.insert_at_beginning(12)
l2.insert_at_beginning(11)



merged = l1.mergeTwoList(l1, l2)
merged.print_list()