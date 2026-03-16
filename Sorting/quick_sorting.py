def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
numbers = [13, 46, 24, 52, 20, 9]
sorted_numbers = quick_sort(numbers)
print("Sorted array:", sorted_numbers)