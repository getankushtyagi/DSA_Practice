# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


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
                
    def print(self):
        curr = self.head
        while(curr):
            print(curr.val, end="=>")         
            curr=curr.next 
        print("\n")      
             
    # Input: head = [1,2,3,4,5]

    def odd_even(self):
        count=1
        stack_even=[]
        stack_odd=[]
        curr=self.head
        
        while(curr):
            if(count%2==0):
                stack_even.append(curr.val)
            else:
                stack_odd.append(curr.val)
            curr=curr.next
            count+=1
            
        curr=self.head
        while(curr):
            if(len(stack_odd)):
                curr.val=stack_odd.pop(0)
            else:
                curr.val=stack_even.pop(0)
            curr=curr.next
            

    
ll=LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)

ll.print()

ll.odd_even()
ll.print()
