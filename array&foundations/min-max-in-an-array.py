arr = [2, 5, 8, 3, 10, 7]

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += num
    else:
        odd += num

print("Sum of even numbers:", even)
print("sum of odd numbers:", odd)