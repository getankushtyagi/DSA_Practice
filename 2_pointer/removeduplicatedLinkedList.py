# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def removeDuplicate(self):
        if not self.head:
            return 0

        current = self.head
        next_node = current.next
        unique = 1

        while next_node:
            if current.val == next_node.val:
                # remove duplicate
                current.next = next_node.next
                next_node = next_node.next
            else:
                # move both pointers forward
                current = next_node
                next_node = next_node.next
                unique += 1

        return unique
            
    def print(self):
        curr = self.head
        while(curr):
            print(curr.val, end="=>")         
            curr=curr.next 
        print("\n")


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return LinkedList()
    
    ll = LinkedList()
    ll.head = ListNode(values[0])
    current = ll.head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    ll.tail = current
    return ll


# Test cases
if __name__ == "__main__":
    # print("Test Case 1: No duplicates")
    # ll1 = create_linked_list([1, 2, 3, 4, 5])
    # print("Before: ", end="")
    # ll1.print()
    # unique_count = ll1.removeDuplicate()
    # print("After:  ", end="")
    # ll1.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 2: All duplicates")
    # ll2 = create_linked_list([1, 1, 1, 1, 1])
    # print("Before: ", end="")
    # ll2.print()
    # unique_count = ll2.removeDuplicate()
    # print("After:  ", end="")
    # ll2.print()
    # print(f"Unique elements: {unique_count}")
    
    print("\nTest Case 3: Consecutive duplicates")
    ll3 = create_linked_list([1, 1, 2, 3, 3])
    print("Before: ", end="")
    ll3.print()
    unique_count = ll3.removeDuplicate()
    print("After:  ", end="")
    ll3.print()
    print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 4: Multiple duplicate groups")
    # ll4 = create_linked_list([1, 1, 2, 2, 3, 3, 4, 4])
    # print("Before: ", end="")
    # ll4.print()
    # unique_count = ll4.removeDuplicate()
    # print("After:  ", end="")
    # ll4.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 5: Duplicates at beginning")
    # ll5 = create_linked_list([1, 1, 1, 2, 3])
    # print("Before: ", end="")
    # ll5.print()
    # unique_count = ll5.removeDuplicate()
    # print("After:  ", end="")
    # ll5.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 6: Duplicates at end")
    # ll6 = create_linked_list([1, 2, 3, 3, 3])
    # print("Before: ", end="")
    # ll6.print()
    # unique_count = ll6.removeDuplicate()
    # print("After:  ", end="")
    # ll6.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 7: Two elements duplicate")
    # ll7 = create_linked_list([1, 1])
    # print("Before: ", end="")
    # ll7.print()
    # unique_count = ll7.removeDuplicate()
    # print("After:  ", end="")
    # ll7.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 8: Two elements no duplicate")
    # ll8 = create_linked_list([1, 2])
    # print("Before: ", end="")
    # ll8.print()
    # unique_count = ll8.removeDuplicate()
    # print("After:  ", end="")
    # ll8.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 9: Single element")
    # ll9 = create_linked_list([1])
    # print("Before: ", end="")
    # ll9.print()
    # unique_count = ll9.removeDuplicate()
    # print("After:  ", end="")
    # ll9.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nTest Case 10: Empty list")
    # ll10 = create_linked_list([])
    # print("Before: ", end="")
    # ll10.print()
    # unique_count = ll10.removeDuplicate()
    # print("After:  ", end="")
    # ll10.print()
    # print(f"Unique elements: {unique_count}")
    
    # # LeetCode Example Test Cases
    # print("\n" + "="*50)
    # print("LEETCODE EXAMPLE TEST CASES")
    # print("="*50)
    
    # print("\nLeetCode Example 1: [1,1,2] -> [1,2]")
    # ll_ex1 = create_linked_list([1, 1, 2])
    # print("Before: ", end="")
    # ll_ex1.print()
    # unique_count = ll_ex1.removeDuplicate()
    # print("After:  ", end="")
    # ll_ex1.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\nLeetCode Example 2: [1,1,2,3,3] -> [1,2,3]")
    # ll_ex2 = create_linked_list([1, 1, 2, 3, 3])
    # print("Before: ", end="")
    # ll_ex2.print()
    # unique_count = ll_ex2.removeDuplicate()
    # print("After:  ", end="")
    # ll_ex2.print()
    # print(f"Unique elements: {unique_count}")
    
    # print("\n✅ All test cases completed!")


    # print("\nTest Case 9: Single element")
    # ll9 = create_linked_list([1])
    # print("Before: ", end="")
    # ll9.print()
    # ll9.removeDuplicate()
    # print("After:  ", end="")
    # ll9.print()
    
    # print("\nTest Case 10: Mixed pattern of duplicates")
    # ll10 = create_linked_list([1, 2, 2, 3, 4, 4, 4, 5])
    # print("Before: ", end="")
    # ll10.print()
    # ll10.removeDuplicate()
    # print("After:  ", end="")
    # ll10.print()
    
    # print("\n✅ All test cases completed!")
