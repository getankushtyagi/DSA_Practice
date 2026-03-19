"""
================================================================================
              DOUBLY LINKED LIST - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS A DOUBLY LINKED LIST?
------------------------------
A linear data structure where each node contains:
- Data
- Pointer to the next node
- Pointer to the previous node

This allows bidirectional traversal unlike singly linked lists.


================================================================================
                        NODE STRUCTURE
================================================================================

Python Implementation:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node


Visual Representation:

    ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐
    │ Prev │  10  │ Next │←──→│ Prev │  20  │ Next │←──→│ Prev │  30  │ Next │
    └──────┴──────┴──────┘    └──────┴──────┴──────┘    └──────┴──────┴──────┘
    ↑                                                                            ↑
   NULL                                                                         NULL
   (Head)                                                                       (Tail)


================================================================================
                    DOUBLY LINKED LIST CLASS
================================================================================

Basic Structure:

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Optional: for O(1) end operations
    
    def is_empty(self):
        return self.head is None


================================================================================
                        BASIC OPERATIONS
================================================================================

1. INSERT AT HEAD (BEGINNING)
   -----------------------------
   Time: O(1), Space: O(1)
   
   Before:
   HEAD → [10]←→[20]←→[30] → NULL
   
   Insert 5 at head:
   HEAD → [5]←→[10]←→[20]←→[30] → NULL
   
   Code:
   def insert_at_head(self, data):
       new_node = Node(data)
       
       if self.head is None:
           self.head = self.tail = new_node
           return
       
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node


2. INSERT AT TAIL (END)
   ----------------------
   Time: O(1) with tail pointer, O(n) without
   Space: O(1)
   
   Before:
   HEAD → [10]←→[20]←→[30] → NULL
   
   Insert 40 at tail:
   HEAD → [10]←→[20]←→[30]←→[40] → NULL
   
   Code (with tail pointer):
   def insert_at_tail(self, data):
       new_node = Node(data)
       
       if self.tail is None:
           self.head = self.tail = new_node
           return
       
       new_node.prev = self.tail
       self.tail.next = new_node
       self.tail = new_node


3. INSERT AT POSITION
   -------------------
   Time: O(n), Space: O(1)
   
   Insert 25 at position 2:
   Before: HEAD → [10]←→[20]←→[30] → NULL
   After:  HEAD → [10]←→[20]←→[25]←→[30] → NULL
   
   Code:
   def insert_at_position(self, data, position):
       if position == 0:
           self.insert_at_head(data)
           return
       
       new_node = Node(data)
       current = self.head
       
       for _ in range(position - 1):
           if current is None:
               return  # Position out of bounds
           current = current.next
       
       if current is None:
           return
       
       new_node.next = current.next
       new_node.prev = current
       
       if current.next:
           current.next.prev = new_node
       else:
           self.tail = new_node
       
       current.next = new_node


4. DELETE FROM HEAD
   -----------------
   Time: O(1), Space: O(1)
   
   Before: HEAD → [10]←→[20]←→[30] → NULL
   After:  HEAD → [20]←→[30] → NULL
   
   Code:
   def delete_from_head(self):
       if self.head is None:
           return None
       
       data = self.head.data
       self.head = self.head.next
       
       if self.head:
           self.head.prev = None
       else:
           self.tail = None
       
       return data


5. DELETE FROM TAIL
   -----------------
   Time: O(1) with tail pointer
   Space: O(1)
   
   Before: HEAD → [10]←→[20]←→[30] → NULL
   After:  HEAD → [10]←→[20] → NULL
   
   Code:
   def delete_from_tail(self):
       if self.tail is None:
           return None
       
       data = self.tail.data
       self.tail = self.tail.prev
       
       if self.tail:
           self.tail.next = None
       else:
           self.head = None
       
       return data


6. DELETE NODE WITH VALUE
   -----------------------
   Time: O(n), Space: O(1)
   
   Delete node with value 20:
   Before: HEAD → [10]←→[20]←→[30] → NULL
   After:  HEAD → [10]←→[30] → NULL
   
   Code:
   def delete_value(self, value):
       current = self.head
       
       while current:
           if current.data == value:
               if current.prev:
                   current.prev.next = current.next
               else:
                   self.head = current.next
               
               if current.next:
                   current.next.prev = current.prev
               else:
                   self.tail = current.prev
               
               return True
           current = current.next
       
       return False


7. DELETE ALL OCCURRENCES
   ------------------------
   Time: O(n), Space: O(1)
   
   Delete all nodes with value X:
   Before: HEAD → [10]←→[20]←→[10]←→[30]←→[10] → NULL
   After:  HEAD → [20]←→[30] → NULL  (for X=10)
   
   Code:
   def delete_all_occurrences(self, value):
       current = self.head
       
       while current:
           if current.data == value:
               next_node = current.next
               
               if current.prev:
                   current.prev.next = current.next
               else:
                   self.head = current.next
               
               if current.next:
                   current.next.prev = current.prev
               else:
                   self.tail = current.prev
               
               current = next_node
           else:
               current = current.next


================================================================================
                        TRAVERSAL OPERATIONS
================================================================================

1. FORWARD TRAVERSAL (Head to Tail)
   ---------------------------------
   def print_forward(self):
       current = self.head
       while current:
           print(current.data, end=\" <-> \")
           current = current.next
       print(\"NULL\")


2. BACKWARD TRAVERSAL (Tail to Head)
   -----------------------------------
   def print_backward(self):
       current = self.tail
       while current:
           print(current.data, end=\" <-> \")
           current = current.prev
       print(\"NULL\")


================================================================================
                    COMMON OPERATIONS
================================================================================

1. FIND LENGTH
   ------------
   def length(self):
       count = 0
       current = self.head
       while current:
           count += 1
           current = current.next
       return count


2. SEARCH ELEMENT
   ---------------
   def search(self, value):
       current = self.head
       position = 0
       
       while current:
           if current.data == value:
               return position
           current = current.next
           position += 1
       
       return -1


3. REVERSE THE LIST
   -----------------
   Swap next and prev pointers for all nodes
   
   def reverse(self):
       current = self.head
       self.head, self.tail = self.tail, self.head
       
       while current:
           current.prev, current.next = current.next, current.prev
           current = current.prev  # Moving to next (which is now prev)


4. FIND MIDDLE
   ------------
   Using slow-fast pointer technique
   
   def find_middle(self):
       slow = fast = self.head
       
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
       
       return slow.data if slow else None


5. DETECT PALINDROME
   ------------------
   Compare from both ends
   
   def is_palindrome(self):
       if not self.head:
           return True
       
       left = self.head
       right = self.tail
       
       while left != right and left.prev != right:
           if left.data != right.data:
               return False
           left = left.next
           right = right.prev
       
       return True


================================================================================
                    ADVANTAGES & DISADVANTAGES
================================================================================

ADVANTAGES over Singly Linked List:
✓ Bidirectional traversal
✓ Delete node in O(1) if node pointer is given
✓ Insert before a node easily
✓ Reverse traversal without recursion
✓ Better for navigation (browser back/forward)

DISADVANTAGES:
✗ Extra memory for prev pointer
✗ More pointers to manage (complexity)
✗ More operations needed for insertion/deletion
✗ All operations take slightly more time


DOUBLY LL vs SINGLY LL:

Feature              | Singly LL  | Doubly LL
---------------------|------------|------------
Memory per node      | Less       | More
Traversal            | One way    | Both ways
Deletion complexity  | O(n)       | O(1) with node pointer
Implementation       | Simpler    | More complex
Reverse              | O(n)       | O(1) pointer swap


================================================================================
                    APPLICATIONS
================================================================================

1. BROWSER NAVIGATION
   - Back and Forward buttons
   - Navigation history

2. MUSIC/VIDEO PLAYER
   - Previous and Next track
   - Playlist navigation

3. UNDO/REDO FUNCTIONALITY
   - Text editors
   - Image editing software

4. LRU CACHE IMPLEMENTATION
   - Maintain recently used items
   - Quick removal from middle

5. DEQUE (DOUBLE-ENDED QUEUE)
   - Insert/delete from both ends

6. MEMORY MANAGEMENT
   - Free list in allocators

7. GAMES
   - Card games (move cards back and forth)
   - Browser tabs


================================================================================
                    CIRCULAR DOUBLY LINKED LIST
================================================================================

Variation where:
- Last node's next points to first node
- First node's prev points to last node

Visualization:
        ┌─────────────────────────────┐
        ↓                             ↑
    ┌───────┬───────┐  ┌───────┬───────┐  ┌───────┬───────┐
    │←  10  →│       │↔│←  20  →│       │↔│←  30  →│       │
    └───────┴───────┘  └───────┴───────┘  └───────┴───────┘
        ↑                                              ↓
        └──────────────────────────────────────────────┘

Advantages:
- Can reach any node from any other node
- Useful for round-robin scheduling


================================================================================
                    COMMON PROBLEMS
================================================================================

BASIC:
1. Insert at head/tail/position
2. Delete from head/tail
3. Delete node with value
4. Traverse forward and backward
5. Find length
6. Search element

INTERMEDIATE:
1. Reverse doubly linked list
2. Find middle element
3. Delete all occurrences of value
4. Sort doubly linked list
5. Remove duplicates from sorted DLL
6. Clone DLL with random pointers
7. Pairs with given sum in sorted DLL
8. Check if palindrome

ADVANCED:
1. LRU Cache using DLL
2. Convert binary tree to DLL
3. Flatten multilevel DLL
4. Rotate DLL by N nodes
5. Quicksort on DLL
6. Merge K sorted DLLs
7. Find triplet with given sum


================================================================================
                    IMPLEMENTATION TIPS
================================================================================

1. Always update both next AND prev pointers
2. Handle edge cases:
   - Empty list
   - Single node
   - Two nodes
3. Check if operating on head or tail
4. Maintain head and tail pointers for efficiency
5. When deleting, check both prev and next
6. Draw diagrams for complex operations
7. Test with small examples first
8. Remember: node.next.prev should equal node
9. When inserting, set new_node pointers first
10. Null check before accessing node.next or node.prev


================================================================================
                    COMPLETE EXAMPLE
================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=\" <-> \")
            current = current.next
        print(\"NULL\")

# Usage
dll = DoublyLinkedList()
dll.insert_at_tail(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.print_list()  # Output: 10 <-> 20 <-> 30 <-> NULL


================================================================================
                    KEY TAKEAWAYS
================================================================================

1. Each node has TWO pointers (next and prev)
2. Allows bidirectional traversal
3. Better for certain operations than singly LL
4. Trade memory for functionality
5. Careful pointer management is crucial
6. Ideal when you need to go back and forth
7. Used in many practical applications
8. More complex but more powerful than singly LL

================================================================================
"""
