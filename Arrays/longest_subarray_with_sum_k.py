def longest_subarray_with_sum_k(arr, k):
    prefix_map = {} 
    current_sum = 0
    max_length = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == k:
            max_length = i + 1
        if (current_sum - k) in prefix_map:
            length = i - prefix_map[current_sum - k]
            max_length = max(max_length, length)
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i
    return max_length
arr = [2, -1, 2, 3, -2, 1, 1]
k = 4
print(longest_subarray_with_sum_k(arr, k)) 