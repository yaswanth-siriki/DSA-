def missing_number(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)
nums = list(map(int, input("Enter numbers: ").split(',')))
print("Missing number:", missing_number(nums))