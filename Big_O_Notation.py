# Big O Notation Examples in Python

# Example 1: Constant Time - O(1)
# A function that always takes the same time to execute, regardless of input size.

def get_first_element(lst):
    # This function returns the first element from the list.
    # It always takes the same amount of time to access the first item, no matter how large the list is.
    return lst[0]  # O(1): Constant time complexity

# Example 2: Linear Time - O(n)
# A function that iterates over all elements in the input.

def print_elements(lst):
    # This function loops through each element in the list and prints it.
    # The time it takes to run will increase linearly with the size of the list.
    for element in lst:  # O(n): We are iterating over each element once.
        print(element)

# Example 3: Quadratic Time - O(n^2)
# A function with nested loops that causes the time complexity to grow quadratically with the input size.

def print_pairs(lst):
    # This function prints all possible pairs of elements from the list.
    # It uses two nested loops, so the time complexity is proportional to the square of the list size.
    for i in lst:  # Outer loop: O(n)
        for j in lst:  # Inner loop: O(n)
            print(i, j)  # O(n^2): Quadratic time complexity

# Example 4: Logarithmic Time - O(log n)
# A function that reduces the problem size in half with each iteration, like a binary search.

def binary_search(arr, target):
    # This function performs a binary search on a sorted list to find the target element.
    # With each iteration, it reduces the search range by half, which results in logarithmic time complexity.
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            left = mid + 1  # Narrow the search to the right half
        else:
            right = mid - 1  # Narrow the search to the left half
    return -1  # If the target is not found, return -1

# Example 5: Exponential Time - O(2^n)
# A function that solves a problem by recursively solving two smaller sub-problems, causing exponential growth in time complexity.

def fibonacci(n):
    # This function calculates the nth Fibonacci number using recursion.
    # Since it calls itself twice for each value of n, the number of calls grows exponentially with n.
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # O(2^n): Exponential time complexity

# Example 6: Factorial Time - O(n!)
# A function that calculates the factorial of a number using recursion, leading to factorial time complexity.

def factorial(n):
    # This function calculates the factorial of a number recursively.
    # The recursive calls grow as a factorial function, leading to very high time complexity for large n.
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)  # O(n!): Factorial time complexity

# Example 7: Linearithmic Time - O(n log n)
# An example of a time complexity that appears in efficient sorting algorithms like Merge Sort and Quick Sort.

def merge_sort(arr):
    # This function performs a merge sort on the input array.
    # Merge sort is an efficient sorting algorithm with time complexity O(n log n).
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2  # Find the middle index
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    # Merge two sorted lists into one sorted list.
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)  # Append the remaining elements
    return sorted_list  # O(n log n): Linearithmic time complexity

# Time Complexity Summary:
# - O(1): Constant time
# - O(n): Linear time
# - O(n^2): Quadratic time
# - O(log n): Logarithmic time
# - O(2^n): Exponential time
# - O(n!): Factorial time
# - O(n log n): Linearithmic time

# Big O Notation is essential for analyzing the performance of algorithms and understanding their scalability.
