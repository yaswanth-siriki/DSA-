a = [13, 46, 24, 52, 20, 9]
n = len(a)
for i in range(1, n):
    x= a[i]
    j = i - 1
    while j >= 0 and a[j] > x:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x
print(a)