a = [13,46,24,52,20,9]
n = len(a)
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if a[j] < a[min]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)