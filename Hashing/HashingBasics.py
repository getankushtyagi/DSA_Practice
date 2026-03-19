"""
================================================================================
                    HASHING - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS HASHING?
----------------
Hashing is a technique to map data of arbitrary size to fixed-size values.
It provides O(1) average time for insertion, deletion, and search operations.

Key Components:
1. Hash Function: Converts key to array index
2. Hash Table: Data structure that stores key-value pairs
3. Collision Resolution: Handle when two keys map to same index


================================================================================
                        HASH FUNCTION
================================================================================

WHAT IS A HASH FUNCTION?
------------------------
A function that takes a key and returns an index in the hash table.

Properties of Good Hash Function:
✓ Deterministic: Same key always gives same hash
✓ Uniform Distribution: Minimizes collisions
✓ Fast to compute: O(1) operation
✓ Minimize clustering: Spread keys evenly

Common Hash Functions:

1. DIVISION METHOD:
   hash(key) = key % table_size
   
   Example: key = 25, table_size = 10
   hash(25) = 25 % 10 = 5

2. MULTIPLICATION METHOD:
   hash(key) = floor(m * (k * A % 1))
   where A is constant (0.618033 golden ratio often used)

3. MID-SQUARE METHOD:
   Square the key, take middle digits

4. FOLDING METHOD:
   Divide key into parts, add them

For Strings:
   hash(string) = Σ (char * 31^i) % table_size
   
   Example: \"cat\"
   hash = (c * 31² + a * 31¹ + t * 31⁰) % table_size


================================================================================
                        HASH TABLE STRUCTURE
================================================================================

Basic Structure:

Index    Value
-----    -----
  0   →  None
  1   →  [\"apple\", 5]
  2   →  None
  3   →  [\"banana\", 3]
  4   →  [\"cherry\", 8]
  5   →  None
  ...

With Chaining (Multiple values at index):

Index    Value (Linked List)
-----    -------------------
  0   →  None
  1   →  [\"apple\", 5] → [\"apricot\", 2] → None
  2   →  None
  3   →  [\"banana\", 3] → None
  4   →  [\"cherry\", 8] → None
  5   →  None


================================================================================
                        COLLISION RESOLUTION
================================================================================

COLLISION: When two keys hash to the same index.

Example:
   hash(\"John\") = 3
   hash(\"Jane\") = 3  ← Collision!


METHOD 1: SEPARATE CHAINING (OPEN HASHING)
-------------------------------------------
Store multiple elements at same index using linked list.

Visualization:
Index
  0  →  None
  1  →  [25] → [75] → None
  2  →  [12] → None
  3  →  [33] → [63] → None
  4  →  None

Insert 25: hash(25) = 1
Insert 75: hash(75) = 1  (collision, add to chain)

Pros:
✓ Simple to implement
✓ Hash table never fills up
✓ Less sensitive to hash function

Cons:
✗ Extra memory for pointers
✗ Cache performance poor

Implementation:
    class HashTable:
        def __init__(self, size=10):
            self.size = size
            self.table = [[] for _ in range(size)]
        
        def hash_function(self, key):
            return hash(key) % self.size
        
        def insert(self, key, value):
            index = self.hash_function(key)
            # Check if key exists
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            # Add new key-value pair
            self.table[index].append((key, value))
        
        def search(self, key):
            index = self.hash_function(key)
            for k, v in self.table[index]:
                if k == key:
                    return v
            return None
        
        def delete(self, key):
            index = self.hash_function(key)
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
            return False


METHOD 2: OPEN ADDRESSING (CLOSED HASHING)
-------------------------------------------
Find another empty slot when collision occurs.

a) LINEAR PROBING:
   Try next slot: h(k), h(k)+1, h(k)+2, ...
   
   Example:
   Insert 25: hash(25) = 3 → table[3] = 25
   Insert 35: hash(35) = 3 (collision) → try 4 → table[4] = 35
   Insert 45: hash(45) = 3 (collision) → try 4 (occupied) → try 5 → table[5] = 45
   
   Index: 0  1  2  3   4   5   6  7  8  9
   Value: _  _  _  25  35  45  _  _  _  _
   
   Clustering Problem: Forms clusters of occupied cells

b) QUADRATIC PROBING:
   Try slots: h(k), h(k)+1², h(k)+2², h(k)+3², ...
   
   Reduces primary clustering

c) DOUBLE HASHING:
   Use second hash function:
   h(k, i) = (h1(k) + i * h2(k)) % table_size
   
   Example:
   h1(k) = k % 10
   h2(k) = 7 - (k % 7)
   
   Best open addressing method

Implementation (Linear Probing):
    class HashTable:
        def __init__(self, size=10):
            self.size = size
            self.table = [None] * size
        
        def hash_function(self, key):
            return hash(key) % self.size
        
        def insert(self, key, value):
            index = self.hash_function(key)
            
            # Linear probing
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    self.table[index] = (key, value)
                    return
                index = (index + 1) % self.size
            
            self.table[index] = (key, value)
        
        def search(self, key):
            index = self.hash_function(key)
            start_index = index
            
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    return self.table[index][1]
                index = (index + 1) % self.size
                if index == start_index:
                    break
            return None


================================================================================
                        LOAD FACTOR
================================================================================

Load Factor (α) = Number of elements / Table size

Example:
   10 elements in table of size 20
   α = 10/20 = 0.5

Impact on Performance:
- Higher load factor → More collisions → Slower operations
- Lower load factor → Less collisions → Wasted space

Typical Thresholds:
- Chaining: Rehash when α > 1.0
- Open Addressing: Rehash when α > 0.7

REHASHING:
When load factor exceeds threshold:
1. Create new table (usually 2x size)
2. Recompute hash for all elements
3. Insert into new table
4. Delete old table


================================================================================
                        PYTHON DICTIONARIES
================================================================================

Python's built-in dict uses hash tables:

# Create dictionary
ages = {\"Alice\": 25, \"Bob\": 30}
ages = dict(Alice=25, Bob=30)

# Operations
ages[\"Alice\"]           # O(1) access
ages[\"Charlie\"] = 35   # O(1) insertion
del ages[\"Bob\"]         # O(1) deletion
\"Alice\" in ages         # O(1) membership test

# Methods
ages.keys()             # All keys
ages.values()           # All values
ages.items()            # Key-value pairs
ages.get(\"Alice\", 0)   # Get with default

# Dictionary comprehension
squares = {x: x**2 for x in range(10)}


PYTHON SETS:
Sets also use hashing:

# Create set
fruits = {\"apple\", \"banana\", \"cherry\"}
fruits = set([\"apple\", \"banana\"])

# Operations - All O(1) average
fruits.add(\"date\")
fruits.remove(\"banana\")
\"apple\" in fruits

# Set operations
set1 | set2            # Union
set1 & set2            # Intersection
set1 - set2            # Difference
set1 ^ set2            # Symmetric difference


================================================================================
                        HASH TABLE APPLICATIONS
================================================================================

1. FREQUENCY COUNTING
   Count occurrences of elements
   
   def count_frequency(arr):
       freq = {}
       for num in arr:
           freq[num] = freq.get(num, 0) + 1
       return freq
   
   arr = [1, 2, 2, 3, 3, 3]
   # Output: {1: 1, 2: 2, 3: 3}

2. TWO SUM PROBLEM
   Find two numbers that add up to target
   
   def two_sum(arr, target):
       seen = {}
       for i, num in enumerate(arr):
           complement = target - num
           if complement in seen:
               return [seen[complement], i]
           seen[num] = i
       return None
   
   Time: O(n), Space: O(n)

3. CACHING (MEMOIZATION)
   Store computed results
   
   cache = {}
   def fibonacci(n):
       if n in cache:
           return cache[n]
       if n <= 1:
           return n
       cache[n] = fibonacci(n-1) + fibonacci(n-2)
       return cache[n]

4. DETECTING DUPLICATES
   Find first repeated element
   
   def first_duplicate(arr):
       seen = set()
       for num in arr:
           if num in seen:
               return num
           seen.add(num)
       return None

5. ANAGRAMS
   Group anagrams together
   
   def group_anagrams(words):
       anagrams = {}
       for word in words:
           key = ''.join(sorted(word))
           anagrams.setdefault(key, []).append(word)
       return list(anagrams.values())

6. SUBARRAY WITH GIVEN SUM
   Find subarray with sum = k
   
   def subarray_sum(arr, k):
       prefix_sum = {0: -1}
       current_sum = 0
       
       for i, num in enumerate(arr):
           current_sum += num
           if current_sum - k in prefix_sum:
               start = prefix_sum[current_sum - k] + 1
               return arr[start:i+1]
           prefix_sum[current_sum] = i
       return None


================================================================================
                        TIME COMPLEXITY
================================================================================

Operation       | Average    | Worst Case
----------------|------------|------------
Search          | O(1)       | O(n)
Insert          | O(1)       | O(n)
Delete          | O(1)       | O(n)
Space           | O(n)       | O(n)

Worst case occurs when:
- All keys hash to same index (all collisions)
- Poor hash function
- High load factor

With good hash function and load factor < 0.75:
→ Average case is O(1)


================================================================================
                        ADVANTAGES & DISADVANTAGES
================================================================================

ADVANTAGES:
✓ Fast operations: O(1) average time
✓ Dynamic sizing
✓ Flexible keys (any hashable type)
✓ Efficient for large datasets
✓ No need for sorted data

DISADVANTAGES:
✗ No order preservation
✗ Worst case can be O(n)
✗ Space overhead
✗ Hash function design is crucial
✗ Not cache-friendly


================================================================================
                        HASH TABLE vs OTHER STRUCTURES
================================================================================

HASH TABLE vs ARRAY:
- Array: O(1) access by index, O(n) search
- Hash Table: O(1) search by key, no index access

HASH TABLE vs BINARY SEARCH TREE:
- Hash Table: O(1) average, no order
- BST: O(log n), maintains order

HASH TABLE vs LINKED LIST:
- Hash Table: O(1) search
- Linked List: O(n) search


================================================================================
                        PERFECT HASHING
================================================================================

When keys are known in advance:

PERFECT HASH FUNCTION:
- No collisions
- Each key maps to unique index
- O(1) worst case guaranteed

Example:
Keys: {\"apple\", \"banana\", \"cherry\"}
Design hash function with no collisions

Used in:
- Compilers (keyword lookup)
- Databases (constant lookup tables)


================================================================================
                        BLOOM FILTER
================================================================================

Space-efficient probabilistic data structure:

Properties:
- Can have false positives
- No false negatives
- Very space efficient

Use Cases:
- Check if element might be in set
- Web browsers (malicious URL detection)
- Databases (avoid disk lookups)


================================================================================
                        COMMON PROBLEMS
================================================================================

BEGINNER:
1. Implement hash table with chaining
2. Count frequency of elements
3. Find first non-repeating character
4. Check if two strings are anagrams
5. Find duplicates in array

INTERMEDIATE:
1. Two sum problem
2. Group anagrams
3. Longest substring without repeating characters
4. Subarray sum equals k
5. Isomorphic strings
6. Valid sudoku
7. Top k frequent elements

ADVANCED:
1. LRU Cache
2. Design HashMap
3. Find all anagrams in string
4. Longest consecutive sequence
5. Copy list with random pointer
6. Four sum problem
7. Palindrome pairs


================================================================================
                        IMPORTANT NOTES
================================================================================

1. Hash function quality is crucial for performance
2. Choose appropriate initial size to minimize rehashing
3. Load factor affects performance-space tradeoff
4. Python's hash() is not consistent across runs (for security)
5. Only immutable objects are hashable in Python
6. Sets are unordered - don't rely on insertion order (use OrderedDict)
7. For string keys, rolling hash is efficient
8. Collision resolution impacts worst-case performance

================================================================================
"""
