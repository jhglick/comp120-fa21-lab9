"""
File: quicksort.py 
Author: COMP 120 class
Date: 2021
Description: Has functions to merge sort a list.
"""
def quick_sort(items):
    """
    Sort items from smallest to largest
    using quick sort.
    """
    quick_sort_recursive(items, 0, len(items) - 1)

def quick_sort_recursive(items, low, high):
    """
    Sort items[low:high+1] from smallest to largest
    using quick sort.
    """
    if low < high:
        pivot_index = partition(items, low, high)
        quick_sort_recursive(items, low, pivot_index - 1)
        quick_sort_recursive(items, pivot_index + 1, high)

def partition(items, low, high):
    """
    Partition the items in items[low:high+1]
    """
    
    pivot_value = items[low]
    left = low + 1
    right = high
    while left <= right:
        while left <= right and items[left] <= pivot_value:
            left += 1
        while right >= left and items[right] > pivot_value:
            right -= 1
        if right > left:
            temp = items[right]
            items[right] = items[left]
            items[left] = temp
    items[low] = items[right]
    items[right] = pivot_value
    return right

def quick_sort_b(items):
    """
    Sort items from smallest to largest
    using quick sort.
    """
    quick_sort_recursive_b(items, 0, len(items) - 1)

def quick_sort_recursive_b(items, low, high):
    """
    Sort items[low:high+1] from smallest to largest
    using quick sort.
    """
    if low < high:
        pivot_index = partition_b(items, low, high)
        quick_sort_recursive_b(items, low, pivot_index - 1)
        quick_sort_recursive_b(items, pivot_index + 1, high)

def partition_b(items, low, high):
    """
    Partition the items in items[low:high+1]
    """
    pass  # replace this

if __name__ == "__main__":
    items1 = [77, 94, 4, 12, 33, 54, 66, 19, 8, 50]
    items1_after = [19, 8, 4, 12, 33, 50, 66, 54, 94, 77]
    pivot_index_correct = 5
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [77, 94, 4, 12, 50, 54, 66, 19, 33]
    items1_after = [19, 33, 4, 12, 50, 54, 66, 77, 94]
    pivot_index_correct = 4
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Correct pivot index {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Correct list is {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [77, 94, 4, 12, 50, 54, 66, 19, 8, 33]
    items1_after = [19, 33, 4, 12, 8, 50, 66, 54, 77, 94]
    pivot_index_correct = 5
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [50, 94, 4, 12, 33, 54, 66, 19, 8, 77]
    items1_after = [19, 8, 4, 12, 33, 50, 66, 54, 94, 77]
    pivot_index_correct = 5
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [50, 94, 4, 12, 77, 54, 66, 19, 8, 33]
    items1_after = [19, 33, 4, 12, 8, 50, 66, 54, 77, 94]
    pivot_index_correct = 5                                                 
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [33, 94, 4, 12, 50, 54, 66, 19, 8, 77]
    items1_after = [19, 8, 4, 12, 33, 50, 66, 54, 94, 77] 
    pivot_index_correct = 5                                                
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [33, 94, 4, 12, 77, 54, 66, 19, 8, 50]
    items1_after = [19, 33, 4, 12, 8, 50, 66, 54, 77, 94] 
    pivot_index_correct = 5                                                
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [1, 21, 42, 78, 99, 101,150, 165, 189, 191]
    items1_after = [1, 21, 42, 78, 99, 101, 150, 165, 189, 191]  
    pivot_index_correct = 4                                               
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")

    items1 = [42, 1]
    items1_after = [1, 42]  
    pivot_index_correct = 1                                              
    print(f"calling partition_b with {items1}")
    pivot_index = partition_b(items1, 0, len(items1) - 1)
    if pivot_index != pivot_index_correct or items1 != items1_after:
        print("Incorrect")
        print(f"Your pivot index = {pivot_index}")
        print(f"Should be {pivot_index_correct}")
        print(f"Your list is {items1}")
        print(f"Should be {items1_after}")
    else:
        print("Correct. Nice job!")
