
"""
Problem: Bubble Sort

Given an array of integers, sort it using the bubble sort algorithm.
Bubble sort repeatedly compares adjacent elements and swaps them if they are in wrong order.
Time Complexity: O(n²)
"""

class sort:
    def bubbleSorting(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if(arr[j]>arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    
    
sorting = sort()
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", arr)
print("Sorted array is:", sorting.bubbleSorting(arr))