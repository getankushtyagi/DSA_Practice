"""
================================================================================
                        ARRAY - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS AN ARRAY?
-----------------
An array is a linear data structure that stores elements of the same type in 
contiguous memory locations. Each element can be accessed using its index.

Properties:
- Fixed size (in most languages, dynamic in Python)
- Homogeneous elements (same data type)
- Random access using index: O(1)
- Contiguous memory allocation


================================================================================
                        ARRAY BASICS
================================================================================

1. ARRAY DECLARATION & INITIALIZATION

Python Lists (Dynamic Arrays):
    # Empty array
    arr = []
    
    # Array with values
    arr = [1, 2, 3, 4, 5]
    
    # Array with specific size (initialized with zeros)
    arr = [0] * 5  # [0, 0, 0, 0, 0]
    
    # Array from range
    arr = list(range(1, 6))  # [1, 2, 3, 4, 5]


2. ARRAY INDEXING

    arr = [10, 20, 30, 40, 50]
    
    Index:     0   1   2   3   4
    Value:    10  20  30  40  50
    
    # Positive indexing (from start)
    arr[0]  → 10
    arr[2]  → 30
    
    # Negative indexing (from end)
    arr[-1] → 50  (last element)
    arr[-2] → 40  (second last)


3. ARRAY SLICING

    arr = [10, 20, 30, 40, 50, 60]
    
    arr[1:4]    → [20, 30, 40]     # From index 1 to 3
    arr[:3]     → [10, 20, 30]     # From start to index 2
    arr[3:]     → [40, 50, 60]     # From index 3 to end
    arr[::2]    → [10, 30, 50]     # Every 2nd element
    arr[::-1]   → [60, 50, 40, 30, 20, 10]  # Reverse


================================================================================
                    BASIC ARRAY OPERATIONS
================================================================================

1. TRAVERSAL - Visit each element
   Time: O(n), Space: O(1)
   
   for i in range(len(arr)):
       print(arr[i])
   
   # Or using for-each
   for element in arr:
       print(element)


2. INSERTION
   
   a) At End: O(1) amortized
      arr.append(60)
   
   b) At Beginning: O(n) - shifts all elements
      arr.insert(0, 5)
   
   c) At Position: O(n) - shifts elements
      arr.insert(2, 25)


3. DELETION
   
   a) From End: O(1)
      arr.pop()
   
   b) From Beginning: O(n) - shifts all elements
      arr.pop(0)
   
   c) By Value: O(n)
      arr.remove(30)
   
   d) From Position: O(n)
      del arr[2]


4. SEARCHING
   
   a) Linear Search: O(n)
      element = 30
      for i in range(len(arr)):
          if arr[i] == element:
              print(f"Found at index {i}")
   
   b) Binary Search: O(log n) - Only for sorted arrays
      # See BinarySearch.py for implementation


5. UPDATING
   Time: O(1)
   
   arr[2] = 100  # Update element at index 2


================================================================================
                    COMMON ARRAY PATTERNS
================================================================================

1. TWO POINTER TECHNIQUE
   Used for: Pair finding, reversing, partitioning
   
   Example: Reverse an array
   ```
   left, right = 0, len(arr) - 1
   while left < right:
       arr[left], arr[right] = arr[right], arr[left]
       left += 1
       right -= 1
   ```

2. SLIDING WINDOW
   Used for: Subarrays, substrings
   
   Example: Maximum sum of k consecutive elements
   ```
   window_sum = sum(arr[:k])
   max_sum = window_sum
   
   for i in range(k, len(arr)):
       window_sum = window_sum - arr[i-k] + arr[i]
       max_sum = max(max_sum, window_sum)
   ```

3. PREFIX SUM
   Used for: Range queries, subarray sums
   
   arr = [1, 2, 3, 4, 5]
   prefix = [1, 3, 6, 10, 15]
   
   Sum from index i to j = prefix[j] - prefix[i-1]

4. KADANE'S ALGORITHM
   Used for: Maximum subarray sum
   
   max_sum = current_sum = arr[0]
   for i in range(1, len(arr)):
       current_sum = max(arr[i], current_sum + arr[i])
       max_sum = max(max_sum, current_sum)

5. DUTCH NATIONAL FLAG (3-way partitioning)
   Used for: Sorting 0s, 1s, 2s
   
   Uses three pointers: low, mid, high


================================================================================
                    MULTI-DIMENSIONAL ARRAYS
================================================================================

1. 2D ARRAY (MATRIX)

   matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
   
   Visualization:
       Col 0  Col 1  Col 2
   Row 0  1     2      3
   Row 1  4     5      6
   Row 2  7     8      9
   
   Access: matrix[row][col]
   Example: matrix[1][2] = 6


2. MATRIX TRAVERSAL
   
   a) Row-wise:
      for i in range(len(matrix)):
          for j in range(len(matrix[0])):
              print(matrix[i][j], end=' ')
          print()
   
   b) Column-wise:
      for j in range(len(matrix[0])):
          for i in range(len(matrix)):
              print(matrix[i][j], end=' ')
   
   c) Diagonal:
      for i in range(len(matrix)):
          print(matrix[i][i])


3. COMMON MATRIX OPERATIONS
   
   a) Transpose:
      transposed = [[matrix[j][i] for j in range(len(matrix))] 
                    for i in range(len(matrix[0]))]
   
   b) Rotate 90° clockwise:
      - Transpose
      - Reverse each row


================================================================================
                    TIME COMPLEXITY SUMMARY
================================================================================

Operation                   | Time Complexity
----------------------------|------------------
Access (by index)           | O(1)
Search (unsorted)           | O(n)
Search (sorted)             | O(log n) - binary search
Insert at end               | O(1) amortized
Insert at beginning/middle  | O(n)
Delete from end             | O(1)
Delete from beginning/middle| O(n)
Traverse                    | O(n)


================================================================================
                    ARRAY vs OTHER DATA STRUCTURES
================================================================================

ARRAY vs LINKED LIST:
- Array: Random access O(1), Insert/Delete O(n)
- Linked List: Random access O(n), Insert/Delete O(1)
- Array: Contiguous memory
- Linked List: Scattered memory with pointers

ARRAY vs DYNAMIC ARRAY (Python List):
- Static Array: Fixed size
- Dynamic Array: Resizes automatically (doubling strategy)


================================================================================
                    COMMON PROBLEMS & TECHNIQUES
================================================================================

1. SEARCHING PROBLEMS
   - Linear search
   - Binary search
   - Find first/last occurrence
   - Search in rotated sorted array

2. SORTING PROBLEMS
   - Bubble sort, Selection sort, Insertion sort: O(n²)
   - Merge sort, Quick sort, Heap sort: O(n log n)
   - Counting sort, Radix sort: O(n) - special cases

3. ROTATION PROBLEMS
   - Left rotate by k positions
   - Right rotate by k positions
   - Reverse method

4. SUBARRAY PROBLEMS
   - Maximum subarray sum (Kadane's)
   - Subarray with given sum
   - Longest subarray with condition

5. TWO POINTER PROBLEMS
   - Two sum problem
   - Three sum problem
   - Container with most water
   - Remove duplicates from sorted array

6. FREQUENCY PROBLEMS
   - Count frequency of elements
   - Find majority element
   - First repeating element

7. REARRANGEMENT
   - Move zeros to end
   - Separate even and odd
   - Sort 0s, 1s, 2s


================================================================================
                    ADVANTAGES & DISADVANTAGES
================================================================================

ADVANTAGES:
✓ Fast access: O(1) random access
✓ Cache-friendly (contiguous memory)
✓ Simple and easy to use
✓ Efficient iteration
✓ Low memory overhead

DISADVANTAGES:
✗ Fixed size (in most languages)
✗ Expensive insertion/deletion: O(n)
✗ Wasted space if not fully used
✗ Difficult to resize


================================================================================
                    PRACTICE PROBLEMS
================================================================================

BEGINNER:
1. Reverse an array
2. Find maximum and minimum element
3. Find second largest element
4. Check if array is sorted
5. Remove duplicates from sorted array

INTERMEDIATE:
1. Two sum problem
2. Maximum subarray sum (Kadane's)
3. Merge two sorted arrays
4. Binary search
5. Rotate array by k positions
6. Find missing number
7. Move zeros to end

ADVANCED:
1. Three sum problem
2. Trapping rain water
3. Stock buy and sell
4. Longest consecutive sequence
5. Median of two sorted arrays
6. Container with most water


================================================================================
                    IMPORTANT NOTES
================================================================================

1. In Python, lists are dynamic arrays that automatically resize
2. Always check array bounds to avoid IndexError
3. Use negative indexing for accessing from end: arr[-1]
4. List comprehensions are Pythonic: [x*2 for x in arr]
5. Slicing creates a new list (copy), not a view
6. sorted() creates new list, sort() sorts in-place
7. For large arrays, consider using NumPy for better performance

================================================================================
"""
