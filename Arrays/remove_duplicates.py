def remove_duplicates(a):
    i = 0
    for j in range(1, len(a)):
        if a[j] != a[i]:
            i += 1
            a[i] = a[j]
    return i + 1
a = [1,1,2,2,2,3,3]
print(remove_duplicates(a))
