"""
================================================================================
                    LINKED LIST - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS A LINKED LIST?
-----------------------
A linked list is a linear data structure where elements (nodes) are stored in 
non-contiguous memory locations. Each node contains data and a reference (pointer) 
to the next node.

Unlike arrays, linked lists don't need contiguous memory and can grow dynamically.


================================================================================
                        NODE STRUCTURE
================================================================================

Basic Node:
    ┌──────┬──────┐
    │ Data │ Next │ → Points to next node
    └──────┴──────┘

Python Implementation:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


================================================================================
                    TYPES OF LINKED LISTS
================================================================================

1. SINGLY LINKED LIST
   -------------------
   Each node points to the next node only.
   
   Diagram:
   ┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
   │  10  │  ●───┼───→│  20  │  ●───┼───→│  30  │  ●───┼───→│  40  │ NULL │
   └──────┴──────┘    └──────┴──────┘    └──────┴──────┘    └──────┴──────┘
   HEAD                                                        TAIL


2. DOUBLY LINKED LIST
   -------------------
   Each node has two pointers: next and prev (previous).
   
   Diagram:
        ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐
   NULL │ Prev │  10  │ Next │←──→│ Prev │  20  │ Next │←──→│ Prev │  30  │ NULL │
        └──────┴──────┴──────┘    └──────┴──────┴──────┘    └──────┴──────┴──────┘
        HEAD                                                  TAIL


3. CIRCULAR LINKED LIST
   ---------------------
   Last node points back to the first node (circular).
   
   Diagram:
        ┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
        │  10  │  ●───┼───→│  20  │  ●───┼───→│  30  │  ●───┼──┐
        └──────┴──────┘    └──────┴──────┘    └──────┴──────┘  │
           ↑                                                     │
           └─────────────────────────────────────────────────────┘


4. CIRCULAR DOUBLY LINKED LIST
   ----------------------------
   Combines circular and doubly linked features.


================================================================================
                    SINGLY LINKED LIST - DETAILED
================================================================================

1. STRUCTURE

   class Node:
       def __init__(self, data):
           self.data = data
           self.next = None
   
   class LinkedList:
       def __init__(self):
           self.head = None


2. VISUALIZATION

   Empty List:
       head → NULL
   
   Single Node:
       head → [10 | ●] → NULL
   
   Multiple Nodes:
       head → [10 | ●] → [20 | ●] → [30 | ●] → NULL


================================================================================
                    BASIC OPERATIONS
================================================================================

1. INSERTION
   ----------
   
   a) Insert at Beginning (Head)
      Time: O(1), Space: O(1)
      
      Before: head → [20] → [30] → NULL
      After:  head → [10] → [20] → [30] → NULL
      
      Steps:
      1. Create new node
      2. new_node.next = head
      3. head = new_node
   
   b) Insert at End (Tail)
      Time: O(n), Space: O(1)
      
      Before: head → [10] → [20] → NULL
      After:  head → [10] → [20] → [30] → NULL
      
      Steps:
      1. Create new node
      2. Traverse to last node
      3. last_node.next = new_node
   
   c) Insert at Position
      Time: O(n), Space: O(1)
      
      Insert 25 at position 2:
      Before: head → [10] → [20] → [30] → NULL
      After:  head → [10] → [20] → [25] → [30] → NULL
      
      Steps:
      1. Traverse to (position - 1)
      2. new_node.next = current.next
      3. current.next = new_node


2. DELETION
   ---------
   
   a) Delete from Beginning
      Time: O(1), Space: O(1)
      
      Before: head → [10] → [20] → [30] → NULL
      After:  head → [20] → [30] → NULL
      
      Steps:
      1. temp = head
      2. head = head.next
      3. del temp
   
   b) Delete from End
      Time: O(n), Space: O(1)
      
      Before: head → [10] → [20] → [30] → NULL
      After:  head → [10] → [20] → NULL
      
      Steps:
      1. Traverse to second last node
      2. second_last.next = None
   
   c) Delete Node with Value
      Time: O(n), Space: O(1)
      
      Delete node with value 20:
      Before: head → [10] → [20] → [30] → NULL
      After:  head → [10] → [30] → NULL
      
      Steps:
      1. Find node with value
      2. previous.next = current.next


3. TRAVERSAL
   ----------
   Time: O(n), Space: O(1)
   
   current = head
   while current:
       print(current.data)
       current = current.next


4. SEARCHING
   ----------
   Time: O(n), Space: O(1)
   
   current = head
   position = 0
   while current:
       if current.data == target:
           return position
       current = current.next
       position += 1
   return -1


================================================================================
                    COMMON PATTERNS & TECHNIQUES
================================================================================

1. TWO POINTER TECHNIQUE (SLOW & FAST)
   ------------------------------------
   Used for: Finding middle, detecting cycle
   
   Slow pointer moves 1 step, Fast pointer moves 2 steps.
   
   Example: Find Middle Element
   
   slow = fast = head
   while fast and fast.next:
       slow = slow.next        # 1 step
       fast = fast.next.next   # 2 steps
   
   # When fast reaches end, slow is at middle


2. DUMMY NODE TECHNIQUE
   ---------------------
   Used for: Simplifying edge cases
   
   dummy = Node(0)
   dummy.next = head
   # Now operate on dummy.next
   return dummy.next


3. REVERSING A LINKED LIST
   ------------------------
   Iterative approach:
   
   prev = None
   current = head
   while current:
       next_node = current.next
       current.next = prev
       prev = current
       current = next_node
   head = prev
   
   Visual:
   Before: [1] → [2] → [3] → NULL
   After:  NULL ← [1] ← [2] ← [3]
           (head moves to 3)


4. CYCLE DETECTION (FLOYD'S ALGORITHM)
   ------------------------------------
   Uses slow and fast pointers.
   
   slow = fast = head
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
       if slow == fast:
           return True  # Cycle exists
   return False


5. FINDING CYCLE START
   --------------------
   After detecting cycle:
   - Move one pointer to head
   - Move both pointers one step at a time
   - They meet at cycle start


================================================================================
                    DOUBLY LINKED LIST - KEY DIFFERENCES
================================================================================

Node Structure:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

Advantages:
✓ Can traverse in both directions
✓ Deletion is easier (no need to track previous)
✓ Can insert before a given node easily

Disadvantages:
✗ Extra memory for prev pointer
✗ More pointers to manage


================================================================================
                    TIME COMPLEXITY COMPARISON
================================================================================

Operation               | Array  | Singly LL | Doubly LL
------------------------|--------|-----------|----------
Access by index         | O(1)   | O(n)      | O(n)
Search                  | O(n)   | O(n)      | O(n)
Insert at beginning     | O(n)   | O(1)      | O(1)
Insert at end           | O(1)*  | O(n)**    | O(1)***
Insert at middle        | O(n)   | O(n)      | O(n)
Delete from beginning   | O(n)   | O(1)      | O(1)
Delete from end         | O(1)   | O(n)      | O(1)***
Delete from middle      | O(n)   | O(n)      | O(n)

* Amortized
** O(1) if tail pointer maintained
*** If tail pointer maintained


================================================================================
                    ADVANTAGES & DISADVANTAGES
================================================================================

ADVANTAGES:
✓ Dynamic size (grows/shrinks easily)
✓ Efficient insertion/deletion at beginning: O(1)
✓ No memory wastage
✓ Can rearrange nodes without copying data

DISADVANTAGES:
✗ No random access (must traverse)
✗ Extra memory for pointers
✗ Not cache-friendly (non-contiguous memory)
✗ Reverse traversal difficult (except doubly LL)


================================================================================
                    LINKED LIST vs ARRAY
================================================================================

Feature              | Array          | Linked List
---------------------|----------------|------------------
Memory               | Contiguous     | Non-contiguous
Size                 | Fixed/Dynamic* | Dynamic
Access Time          | O(1)           | O(n)
Insert/Delete Start  | O(n)           | O(1)
Insert/Delete End    | O(1)*          | O(n) or O(1)**
Memory per element   | Just data      | Data + pointer(s)
Cache performance    | Better         | Worse

* Python lists
** With tail pointer


================================================================================
                    COMMON PROBLEMS
================================================================================

BASIC:
1. Insert node at beginning/end/position
2. Delete node from beginning/end/value
3. Search for an element
4. Find length of linked list
5. Print linked list

INTERMEDIATE:
1. Reverse a linked list (iterative & recursive)
2. Find middle element
3. Detect cycle in linked list
4. Remove duplicates from sorted list
5. Merge two sorted linked lists
6. Find nth node from end
7. Palindrome check
8. Remove nth node from end

ADVANCED:
1. Reverse in groups of k
2. Add two numbers represented as linked lists
3. Clone a linked list with random pointers
4. Flatten a multilevel linked list
5. LRU Cache implementation
6. Find intersection point of two linked lists
7. Rearrange odd-even nodes


================================================================================
                    WHEN TO USE LINKED LIST
================================================================================

USE LINKED LIST WHEN:
✓ Frequent insertions/deletions at beginning
✓ Don't know size in advance
✓ Don't need random access
✓ Implementing stack/queue
✓ Memory is fragmented

USE ARRAY WHEN:
✓ Need random access
✓ Size is known or changes rarely
✓ Need cache-friendly performance
✓ Mostly read operations


================================================================================
                    APPLICATIONS
================================================================================

1. Implementation of stacks and queues
2. Undo functionality (browser back/forward)
3. Music/video player playlists
4. Image viewer (next/previous)
5. Hash table chaining for collision resolution
6. Memory management (free list)
7. Graph adjacency list representation
8. Polynomial arithmetic
9. LRU Cache


================================================================================
                    IMPORTANT TIPS
================================================================================

1. Always check if head is None before operations
2. Use dummy node to simplify edge cases
3. Draw diagrams for complex operations
4. Remember to update head pointer when needed
5. In cycle problems, check if fast and fast.next exist
6. For doubly LL, remember to update both next and prev
7. When reversing, keep track of prev, current, and next
8. Use two pointers (slow/fast) for many problems
9. Maintain tail pointer for O(1) end insertion

================================================================================
"""
