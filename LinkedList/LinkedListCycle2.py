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
            
    # Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
    # There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
    # Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
    def detectCycle(self):
        if(self.head is None):
            return None

        slow=fast=self.head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                break
        else:
            return None
        
        slow=self.head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    
            
            
            
ll=LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(5)
ll.insert_at_end(4)
ll.insert_at_end(15)
ll.insert_at_end(15)

ll.print_list()

print(ll.hasCycle())
