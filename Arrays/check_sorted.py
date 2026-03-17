x = [3,2,1,5,2,10,12]
n = len(x)
is_sorted = True
for i in range(n-1):
    if x[i] > x[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("The array is sorted")
else:
    print("The array is not sorted")