"""
================================================================================
                    SORTING ALGORITHMS - COMPLETE GUIDE
================================================================================

WHAT IS SORTING?
----------------
Sorting is the process of arranging elements in a specific order (ascending or 
descending). It's one of the most fundamental operations in computer science.

Why Sorting Matters:
- Enables binary search (O(log n) instead of O(n))
- Makes finding duplicates easier
- Organizes data for human consumption
- Foundation for many other algorithms


================================================================================
                    CLASSIFICATION OF SORTING ALGORITHMS
================================================================================

1. BY TIME COMPLEXITY:
   - Simple Sorts: O(n²) - Bubble, Selection, Insertion
   - Efficient Sorts: O(n log n) - Merge, Quick, Heap
   - Special Sorts: O(n) - Counting, Radix, Bucket

2. BY SPACE COMPLEXITY:
   - In-place: O(1) extra space - Bubble, Selection, Insertion, Quick
   - Out-of-place: O(n) extra space - Merge, Counting

3. BY STABILITY:
   - Stable: Preserves relative order of equal elements
     (Bubble, Insertion, Merge)
   - Unstable: May change relative order
     (Selection, Quick, Heap)

4. BY APPROACH:
   - Comparison-based: Compare elements (most common)
   - Non-comparison: Use properties of data (Counting, Radix)


================================================================================
                        1. BUBBLE SORT
================================================================================

CONCEPT:
Repeatedly swap adjacent elements if they're in wrong order.
Largest element "bubbles up" to its correct position in each pass.

VISUALIZATION:
Pass 1: [5, 2, 8, 1, 9]
        [2, 5, 8, 1, 9]  (swap 5, 2)
        [2, 5, 1, 8, 9]  (swap 8, 1)
        [2, 5, 1, 8, 9]  (9 in position)

Pass 2: [2, 1, 5, 8, 9]  (8 in position)
Pass 3: [1, 2, 5, 8, 9]  (sorted)

ALGORITHM:
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break  # Already sorted

COMPLEXITY:
- Time: Best O(n), Average O(n²), Worst O(n²)
- Space: O(1)
- Stable: Yes
- In-place: Yes

WHEN TO USE:
- Small datasets
- Nearly sorted data
- Educational purposes


================================================================================
                        2. SELECTION SORT
================================================================================

CONCEPT:
Find minimum element and place it at the beginning.
Repeat for remaining unsorted portion.

VISUALIZATION:
[64, 25, 12, 22, 11]
 ↑ min=11, swap with first
[11, 25, 12, 22, 64]
     ↑ min=12, swap with second
[11, 12, 25, 22, 64]
         ↑ min=22, swap with third
[11, 12, 22, 25, 64]
             ↑ already in place
Sorted: [11, 12, 22, 25, 64]

ALGORITHM:
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

COMPLEXITY:
- Time: Best O(n²), Average O(n²), Worst O(n²)
- Space: O(1)
- Stable: No
- In-place: Yes

WHEN TO USE:
- Small datasets
- Memory is limited
- Simplicity is important


================================================================================
                        3. INSERTION SORT
================================================================================

CONCEPT:
Build sorted array one element at a time by inserting each element 
in its correct position.
Like sorting playing cards in your hand.

VISUALIZATION:
[5, 2, 8, 1, 9]
[5] [2, 8, 1, 9]         (5 is sorted)
[2, 5] [8, 1, 9]         (insert 2 before 5)
[2, 5, 8] [1, 9]         (8 in place)
[1, 2, 5, 8] [9]         (insert 1 at start)
[1, 2, 5, 8, 9]          (sorted)

ALGORITHM:
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

COMPLEXITY:
- Time: Best O(n), Average O(n²), Worst O(n²)
- Space: O(1)
- Stable: Yes
- In-place: Yes

WHEN TO USE:
- Small datasets
- Nearly sorted data (very efficient!)
- Online sorting (elements arrive one at a time)


================================================================================
                        4. MERGE SORT
================================================================================

CONCEPT:
Divide and Conquer algorithm.
Divide array into halves, recursively sort them, then merge.

VISUALIZATION:
                [38, 27, 43, 3, 9, 82, 10]
                ↙                         ↘
        [38, 27, 43, 3]              [9, 82, 10]
        ↙            ↘                ↙         ↘
    [38, 27]      [43, 3]         [9, 82]      [10]
    ↙    ↘        ↙    ↘          ↙   ↘
  [38]  [27]    [43]  [3]       [9]  [82]      [10]
    ↘    ↙        ↘    ↙          ↘   ↙
    [27, 38]      [3, 43]         [9, 82]      [10]
        ↘            ↙                ↘         ↙
        [3, 27, 38, 43]              [9, 10, 82]
                ↘                         ↙
                [3, 9, 10, 27, 38, 43, 82]

ALGORITHM:
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

COMPLEXITY:
- Time: Best O(n log n), Average O(n log n), Worst O(n log n)
- Space: O(n)
- Stable: Yes
- In-place: No

WHEN TO USE:
- Large datasets
- Guaranteed O(n log n) performance
- Need stable sorting
- Linked lists (no random access needed)


================================================================================
                        5. QUICK SORT
================================================================================

CONCEPT:
Divide and Conquer algorithm.
Pick pivot, partition array around pivot, recursively sort partitions.

VISUALIZATION:
[7, 2, 1, 6, 8, 5, 3, 4]  pivot=4
[2, 1, 3, 4, 8, 5, 6, 7]  (elements < 4 left, >= 4 right)
 ↓       ↓  ↓           ↓
[1, 2, 3] 4 [8, 5, 6, 7]  (recursively sort left and right)

Partitioning Process (pivot = 4):
[7, 2, 1, 6, 8, 5, 3, 4]
 i→                    p
    i→
       i→
                i→
                      i→
          swap smaller elements with pivot

ALGORITHM:
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)

COMPLEXITY:
- Time: Best O(n log n), Average O(n log n), Worst O(n²)
- Space: O(log n) for recursion stack
- Stable: No
- In-place: Yes (with modifications)

WHEN TO USE:
- Large datasets
- Average case matters more than worst case
- In-place sorting needed
- Cache-friendly performance


================================================================================
                        6. HEAP SORT
================================================================================

CONCEPT:
Build max heap, repeatedly extract maximum element and rebuild heap.

VISUALIZATION:
Array: [4, 10, 3, 5, 1]

Build Max Heap:
        10
       /  \\
      5    3
     / \\
    4   1

Heap Sort Process:
1. Swap 10 with 1, heapify
2. Swap 5 with 1, heapify
3. Continue...

ALGORITHM:
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    def heap_sort(arr):
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        # Extract elements
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)

COMPLEXITY:
- Time: Best O(n log n), Average O(n log n), Worst O(n log n)
- Space: O(1)
- Stable: No
- In-place: Yes

WHEN TO USE:
- Large datasets
- Memory is limited
- Guaranteed O(n log n) needed


================================================================================
                        7. COUNTING SORT
================================================================================

CONCEPT:
Count frequency of each element, use counts to place elements in sorted order.
Works for integers with small range.

VISUALIZATION:
Input:  [1, 4, 1, 2, 7, 5, 2]
Count:  [0, 2, 2, 0, 1, 1, 0, 1]
Index:   0  1  2  3  4  5  6  7

Cumulative: [0, 2, 4, 4, 5, 6, 6, 7]

Output: [1, 1, 2, 2, 4, 5, 7]

ALGORITHM:
    def counting_sort(arr):
        if not arr:
            return arr
        
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        count = [0] * range_val
        output = [0] * len(arr)
        
        # Count occurrences
        for num in arr:
            count[num - min_val] += 1
        
        # Cumulative count
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # Build output
        for num in reversed(arr):
            index = count[num - min_val] - 1
            output[index] = num
            count[num - min_val] -= 1
        
        return output

COMPLEXITY:
- Time: O(n + k) where k is range
- Space: O(n + k)
- Stable: Yes
- In-place: No

WHEN TO USE:
- Small range of integers
- Need linear time sorting
- Stability is important


================================================================================
                        8. RADIX SORT
================================================================================

CONCEPT:
Sort by individual digits/characters from least significant to most significant.

VISUALIZATION:
Input: [170, 45, 75, 90, 802, 24, 2, 66]

Sort by 1s place:
[170, 90, 802, 2, 24, 45, 75, 66]

Sort by 10s place:
[802, 2, 24, 45, 66, 170, 75, 90]

Sort by 100s place:
[2, 24, 45, 66, 75, 90, 170, 802]

COMPLEXITY:
- Time: O(d * (n + k)) where d is digits, k is base
- Space: O(n + k)
- Stable: Yes
- In-place: No

WHEN TO USE:
- Fixed-length integer keys
- Need linear time
- Stability matters


================================================================================
                    COMPARISON TABLE
================================================================================

Algorithm    | Best      | Average   | Worst     | Space | Stable | In-place
-------------|-----------|-----------|-----------|-------|--------|----------
Bubble       | O(n)      | O(n²)     | O(n²)     | O(1)  | Yes    | Yes
Selection    | O(n²)     | O(n²)     | O(n²)     | O(1)  | No     | Yes
Insertion    | O(n)      | O(n²)     | O(n²)     | O(1)  | Yes    | Yes
Merge        | O(n log n)| O(n log n)| O(n log n)| O(n)  | Yes    | No
Quick        | O(n log n)| O(n log n)| O(n²)     | O(log n)| No   | Yes
Heap         | O(n log n)| O(n log n)| O(n log n)| O(1)  | No     | Yes
Counting     | O(n + k)  | O(n + k)  | O(n + k)  | O(k)  | Yes    | No
Radix        | O(d*n)    | O(d*n)    | O(d*n)    | O(n+k)| Yes    | No


================================================================================
                    CHOOSING THE RIGHT SORT
================================================================================

Small Data (n < 50):
→ Insertion Sort (simple, fast for small n)

Nearly Sorted:
→ Insertion Sort (O(n) best case)

Stability Required:
→ Merge Sort (guaranteed O(n log n))

Limited Space:
→ Heap Sort or Quick Sort (in-place)

Guaranteed Performance:
→ Merge Sort or Heap Sort (O(n log n) worst case)

Average Case Performance:
→ Quick Sort (fastest in practice)

Integer Keys with Small Range:
→ Counting Sort (O(n))

Fixed-length Integer Keys:
→ Radix Sort (O(dn))

General Purpose:
→ Quick Sort or Python's Timsort


================================================================================
                    PYTHON'S BUILT-IN SORT
================================================================================

Python uses TIMSORT (hybrid of Merge Sort and Insertion Sort):

# In-place sort
arr.sort()                    # Modifies arr
arr.sort(reverse=True)        # Descending
arr.sort(key=lambda x: x[1])  # Custom key

# Returns new sorted list
new_arr = sorted(arr)
sorted(arr, reverse=True)
sorted(arr, key=len)

Timsort:
- Time: O(n log n) worst case, O(n) best case
- Stable: Yes
- Adaptive: Faster on partially sorted data


================================================================================
                    IMPORTANT CONCEPTS
================================================================================

1. STABILITY:
   Stable sorts preserve relative order of equal elements.
   
   Input:  [(4,'a'), (3,'b'), (4,'c'), (3,'d')]
   Stable sort by first element:
   Output: [(3,'b'), (3,'d'), (4,'a'), (4,'c')]
                     ↑ order preserved

2. IN-PLACE:
   Sorts array using O(1) extra space.
   No need for additional array.

3. ADAPTIVE:
   Performance improves on partially sorted data.
   Examples: Insertion Sort, Timsort

4. DIVIDE AND CONQUER:
   Break problem into subproblems, solve recursively.
   Examples: Merge Sort, Quick Sort


================================================================================
                    PRACTICE PROBLEMS
================================================================================

BEGINNER:
1. Implement bubble sort
2. Implement selection sort
3. Implement insertion sort
4. Sort array in descending order
5. Find kth smallest element using sorting

INTERMEDIATE:
1. Implement merge sort
2. Implement quick sort
3. Sort array of 0s, 1s, and 2s (Dutch flag)
4. Merge k sorted arrays
5. Sort by frequency
6. Custom comparator sorting

ADVANCED:
1. Implement heap sort
2. External sorting (file too large for memory)
3. Median of medians
4. Pancake sorting
5. Sort array based on another array
6. Implement Timsort

================================================================================
"""
