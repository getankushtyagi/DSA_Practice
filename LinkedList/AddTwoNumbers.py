"""
Problem: Add Two Numbers Represented by Linked Lists

Given two non-empty linked lists representing two non-negative integers, where digits are stored 
in reverse order, add the two numbers and return the sum as a linked list.
Example: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8), representing 342 + 465 = 807
"""

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

