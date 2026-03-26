nums = list(map(int, input("Enter numbers: ").split(',')))
xor = 0
for i in range(len(nums)):
    xor = xor^nums[i]
print(xor) 