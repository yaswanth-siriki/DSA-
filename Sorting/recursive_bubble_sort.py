def bubble_sort_recursive(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)
arr = [13,46,24,52,20,9]
bubble_sort_recursive(arr, len(arr))
print("Sorted array:", arr)

