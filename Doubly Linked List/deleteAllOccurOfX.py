"""
Problem: Delete All Occurrences of X in Doubly Linked List

Given a doubly linked list and a value X, delete all nodes that contain the value X.
Update both next and prev pointers to maintain the doubly linked structure.
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def