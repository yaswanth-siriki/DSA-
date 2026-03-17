a = [1,2,3,4,5]
temp = a[0]
for i in range(len(a)-1):
    a[i] = a[i+1]
a[-1] = temp
print(a)