"""
================================================================================
                  STACK & QUEUE - COMPLETE LEARNING GUIDE
================================================================================

TWO FUNDAMENTAL LINEAR DATA STRUCTURES
---------------------------------------
Stack and Queue are Abstract Data Types (ADTs) that follow specific ordering 
principles for insertion and deletion operations.


================================================================================
                            STACK
================================================================================

WHAT IS A STACK?
----------------
A linear data structure that follows LIFO (Last In First Out) principle.
The last element added is the first one to be removed.

Analogy: Stack of plates - you add and remove from the top only.

Visual Representation:
    │     │     ← Top (newest)
    │ 30  │
    │ 20  │
    │ 10  │     ← Bottom (oldest)
    └─────┘


STACK OPERATIONS:
-----------------
1. push(x)   - Add element to top        - O(1)
2. pop()     - Remove element from top   - O(1)
3. peek()    - View top element          - O(1)
4. isEmpty() - Check if stack is empty   - O(1)
5. size()    - Get number of elements    - O(1)


STACK IMPLEMENTATION:

Using List (Array):
    class Stack:
        def __init__(self):
            self.items = []
        
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            if not self.is_empty():
                return self.items.pop()
        
        def peek(self):
            if not self.is_empty():
                return self.items[-1]
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)


Using Linked List:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    class Stack:
        def __init__(self):
            self.top = None
        
        def push(self, data):
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        
        def pop(self):
            if self.top:
                data = self.top.data
                self.top = self.top.next
                return data


STACK OPERATIONS VISUALIZATION:

push(10):         push(20):         push(30):
    │     │           │     │           │ 30  │
    │     │           │ 20  │           │ 20  │
    │ 10  │           │ 10  │           │ 10  │
    └─────┘           └─────┘           └─────┘
                                        
pop():            pop():            Empty:
    │     │           │     │           │     │
    │ 20  │           │     │           │     │
    │ 10  │           │ 10  │           │     │
    └─────┘           └─────┘           └─────┘
    returns 30        returns 20


================================================================================
                            QUEUE
================================================================================

WHAT IS A QUEUE?
----------------
A linear data structure that follows FIFO (First In First Out) principle.
The first element added is the first one to be removed.

Analogy: Line at a ticket counter - first person in line gets served first.

Visual Representation:
    Front                                    Rear
      ↓                                        ↓
    ┌────┬────┬────┬────┐
    │ 10 │ 20 │ 30 │ 40 │
    └────┴────┴────┴────┘
     ↑                ↑
    Dequeue          Enqueue
   (remove from)    (add to)


QUEUE OPERATIONS:
-----------------
1. enqueue(x) - Add element to rear      - O(1)
2. dequeue()  - Remove element from front- O(1) with linked list
3. front()    - View front element       - O(1)
4. rear()     - View rear element        - O(1)
5. isEmpty()  - Check if queue is empty  - O(1)
6. size()     - Get number of elements   - O(1)


QUEUE IMPLEMENTATION:

Using List (Array):
    class Queue:
        def __init__(self):
            self.items = []
        
        def enqueue(self, item):
            self.items.append(item)
        
        def dequeue(self):
            if not self.is_empty():
                return self.items.pop(0)  # O(n) - not efficient!
        
        def front(self):
            if not self.is_empty():
                return self.items[0]
        
        def is_empty(self):
            return len(self.items) == 0


Using collections.deque (Efficient):
    from collections import deque
    
    class Queue:
        def __init__(self):
            self.items = deque()
        
        def enqueue(self, item):
            self.items.append(item)      # O(1)
        
        def dequeue(self):
            return self.items.popleft()  # O(1) - Efficient!
        
        def front(self):
            return self.items[0]


Using Linked List:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    class Queue:
        def __init__(self):
            self.front = None
            self.rear = None
        
        def enqueue(self, data):
            new_node = Node(data)
            if self.rear:
                self.rear.next = new_node
            self.rear = new_node
            if not self.front:
                self.front = new_node
        
        def dequeue(self):
            if self.front:
                data = self.front.data
                self.front = self.front.next
                if not self.front:
                    self.rear = None
                return data


QUEUE OPERATIONS VISUALIZATION:

Initial:
    Front                  Rear
      ↓                      ↓
    ┌────┬────┬────┐
    │ 10 │ 20 │ 30 │
    └────┴────┴────┘

enqueue(40):
    Front                         Rear
      ↓                             ↓
    ┌────┬────┬────┬────┐
    │ 10 │ 20 │ 30 │ 40 │
    └────┴────┴────┴────┘

dequeue():
         Front            Rear
           ↓               ↓
         ┌────┬────┬────┐
         │ 20 │ 30 │ 40 │  (returns 10)
         └────┴────┴────┘


================================================================================
                        TYPES OF QUEUES
================================================================================

1. SIMPLE QUEUE (Linear Queue)
   - Standard FIFO queue
   - Enqueue at rear, dequeue from front

2.CIRCULAR QUEUE
   - Last position connects back to first
   - Efficient use of space
   
   Diagram:
        ┌────┬────┬────┬────┐
        │ 10 │ 20 │ 30 │ 40 │
        └──┬─┴────┴────┴─┬──┘
           └──────────────┘

3. PRIORITY QUEUE
   - Elements have priorities
   - Higher priority elements dequeued first
   - Uses heap data structure
   
   Example: [5(priority 2), 10(priority 1), 3(priority 3)]
   Dequeue order: 10, 5, 3

4. DOUBLE-ENDED QUEUE (DEQUE)
   - Can insert/remove from both ends
   - Combination of stack and queue
   
   Operations:
   - insertFront(), insertRear()
   - deleteFront(), deleteRear()
   
   Diagram:
    ← insertFront    insertRear →
    ← deleteFront    deleteRear →
    ┌────┬────┬────┬────┐
    │ 10 │ 20 │ 30 │ 40 │
    └────┴────┴────┴────┘


================================================================================
                    SPECIAL IMPLEMENTATIONS
================================================================================

1. IMPLEMENT QUEUE USING STACKS

   Using Two Stacks:
   stack1: For enqueue
   stack2: For dequeue
   
   class MyQueue:
       def __init__(self):
           self.stack1 = []  # For enqueue
           self.stack2 = []  # For dequeue
       
       def enqueue(self, x):
           self.stack1.append(x)
       
       def dequeue(self):
           if not self.stack2:
               while self.stack1:
                   self.stack2.append(self.stack1.pop())
           return self.stack2.pop() if self.stack2 else None


2. IMPLEMENT STACK USING QUEUES

   Using Two Queues:
   
   class MyStack:
       def __init__(self):
           self.queue1 = deque()
           self.queue2 = deque()
       
       def push(self, x):
           self.queue2.append(x)
           while self.queue1:
               self.queue2.append(self.queue1.popleft())
           self.queue1, self.queue2 = self.queue2, self.queue1
       
       def pop(self):
           return self.queue1.popleft() if self.queue1 else None


3. MIN STACK
   
   Stack where getMin() returns minimum element in O(1):
   
   class MinStack:
       def __init__(self):
           self.stack = []
       
       def push(self, val):
           if not self.stack:
               self.stack.append((val, val))
           else:
               current_min = self.stack[-1][1]
               self.stack.append((val, min(val, current_min)))
       
       def pop(self):
           return self.stack.pop()[0]
       
       def getMin(self):
           return self.stack[-1][1]


================================================================================
                    APPLICATIONS OF STACK
================================================================================

1. FUNCTION CALL MANAGEMENT
   - Recursion uses stack internally
   - Store return addresses

2. EXPRESSION EVALUATION
   - Infix to postfix conversion
   - Postfix evaluation
   - Check balanced parentheses

3. BACKTRACKING
   - Maze solving
   - N-Queens problem
   - Sudoku solver

4. UNDO/REDO OPERATIONS
   - Text editors
   - Photoshop layers

5. BROWSER HISTORY
   - Back button functionality

6. DEPTH-FIRST SEARCH (DFS)
   - Graph/tree traversal


================================================================================
                    APPLICATIONS OF QUEUE
================================================================================

1. SCHEDULING
   - CPU scheduling
   - Disk scheduling
   - Print spooler

2. BREADTH-FIRST SEARCH (BFS)
   - Graph/tree traversal
   - Shortest path in unweighted graph

3. BUFFERING
   - IO buffers
   - Network packets

4. REAL-WORLD SYSTEMS
   - CallCenter systems
   - Customer service
   - Ticket counters

5. ASYNCHRONOUS DATA TRANSFER
   - Pipes, file IO
   - Network communication


================================================================================
                    COMMON PROBLEMS
================================================================================

STACK PROBLEMS:
1. Balanced parentheses
2. Next greater element
3. Stock span problem
4. Largest rectangle in histogram
5. Implement min/max stack
6. Evaluate postfix expression
7. Infix to postfix conversion
8. Valid parenthesis string
9. Asteroid collision
10. Daily temperatures

QUEUE PROBLEMS:
1. Implement queue using stacks
2. Generate binary numbers
3. Sliding window maximum
4. First non-repeating character in stream
5. Level order traversal
6. Implement circular queue
7. Design circular deque
8. Task scheduler
9. Rotten oranges (BFS)
10. Snake and ladder


================================================================================
                    TIME COMPLEXITY COMPARISON
================================================================================

Operation       | Stack (Array) | Stack (LL) | Queue (Array*) | Queue (LL/Deque)
----------------|---------------|------------|----------------|------------------
Push/Enqueue    | O(1)          | O(1)       | O(1)           | O(1)
Pop/Dequeue     | O(1)          | O(1)       | O(n)*          | O(1)
Peek/Front      | O(1)          | O(1)       | O(1)           | O(1)
Search          | O(n)          | O(n)       | O(n)           | O(n)
Space           | O(n)          | O(n)       | O(n)           | O(n)

* Using simple list, pop(0) is O(n). Use deque for O(1)!


================================================================================
                    STACK vs QUEUE
================================================================================

Feature         | Stack              | Queue
----------------|--------------------|-----------------
Principle       | LIFO               | FIFO
Operations      | push/pop           | enqueue/dequeue
Access          | Top only           | Front & Rear
Applications    | Recursion, DFS     | BFS, Scheduling
Example         | Stack of plates    | Line at counter


================================================================================
                    IMPORTANT NOTES
================================================================================

1. Use collections.deque for efficient queue in Python
2. list.pop(0) is O(n) - avoid for queues!
3. Stack/Queue with array: may need resizing
4. Stack/Queue with linked list: no resizing needed
5. Always check empty before pop/dequeue
6. Stack is implicit in recursion
7. Queue is essential for BFS
8. Deque provides both stack and queue operations

================================================================================
"""
