nums = [6, 7, 8, 4, 1]
k = int(input("Enter the number: "))
found = -1
for i in range(len(nums)):
    if nums[i] == k:
        found = i
        break
print(found)