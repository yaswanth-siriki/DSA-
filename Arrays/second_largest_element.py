x = [1,2,4,7,7,5]
n = len(x)
largest = x[0]
for i in range(n):
    if(x[i] > largest):
        largest = x[i]
second_largest = -1 
for j in range(n):
    if(x[j] > second_largest and x[j] != largest):
        second_largest = x[j]
print("Largest number is = ",largest)
print("second largest number is = ",second_largest)