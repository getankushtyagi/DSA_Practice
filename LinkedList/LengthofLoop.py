"""
Problem: Find Length of Loop in Linked List

Given a linked list that contains a cycle/loop, find the length of the loop.
Use Floyd's cycle detection algorithm (slow-fast pointers) to detect and measure the loop.
"""

def lengthOfLoop(self, head):
    if(head is None):
        return

    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            count=1
            temp=slow.next
            while(temp != slow):
                count+=1
                temp=temp.next
                return count
    else:
        return 0