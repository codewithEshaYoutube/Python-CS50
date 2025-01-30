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
# 1. Array (List in Python)
# Time Complexity:
# - Access: O(1)
# - Search (Unsorted): O(n)
# - Insert/Delete (end): O(1), O(n) for arbitrary positions

# Example 1: Accessing an element
arr = [1, 2, 3, 4, 5]
print(arr[2])  # O(1) time complexity

# Example 2: Searching for an element
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, 3))  # O(n) time complexity

# Example 3: Inserting an element at the end
arr.append(6)  # O(1) time complexity
print(arr)

# 2. Linked List
# Time Complexity:
# - Access: O(n)
# - Insert/Delete (front): O(1)
# - Insert/Delete (end): O(n) unless you maintain a tail pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  # O(1) time complexity
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

# Example 1: Inserting at the front
ll = LinkedList()
ll.insert_at_front(1)  # O(1)
ll.insert_at_front(2)  # O(1)
ll.display()  # Output: 2 -> 1 ->

# 3. Hash Table (Dictionary in Python)
# Time Complexity:
# - Insert/Search/Delete: O(1) average, O(n) worst case (with collisions)

# Example 1: Inserting/Search/Delete in a dictionary
hash_table = {}
hash_table["a"] = 1  # O(1) average time complexity
hash_table["b"] = 2  # O(1)
print(hash_table["a"])  # O(1)
del hash_table["b"]  # O(1)
print(hash_table)

# 4. Binary Search Tree (BST)
# Time Complexity:
# - Search/Insert/Delete (balanced): O(log n)
# - Worst case (unbalanced): O(n)

class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)

# Example 1: Insert into BST
bst = BST()
root = None
root = bst.insert(root, 10)
root = bst.insert(root, 20)
root = bst.insert(root, 5)
print(bst.search(root, 20))  # O(log n) time complexity if balanced

# 5. Queue (Using List as a Queue)
# Time Complexity:
# - Enqueue (append): O(1)
# - Dequeue (pop from front): O(n)

from collections import deque

queue = deque()
queue.append(1)  # O(1)
queue.append(2)  # O(1)
print(queue.popleft())  # O(1) for deque, O(n) for list

# 6. Sorting Algorithms
# Time Complexity for Merge Sort: O(n log n), Space Complexity: O(n)
# Time Complexity for Bubble Sort: O(n^2), Space Complexity: O(1)

# Example 1: Merge Sort (O(n log n) time complexity, O(n) space complexity)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example 2: Bubble Sort (O(n^2) time complexity)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Testing Merge Sort
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array with Merge Sort:", arr)

# Testing Bubble Sort
arr2 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr2)
print("Sorted array with Bubble Sort:", arr2)


