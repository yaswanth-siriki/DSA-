nums = list(map(int, input("Enter numbers: ").split(',')))
maxi = 0 
count = 0
for i in range(len(nums)):
    if(nums[i] == 1):
        count += 1
        maxi = max(maxi,count)
    else:
        count = 0
print(maxi)