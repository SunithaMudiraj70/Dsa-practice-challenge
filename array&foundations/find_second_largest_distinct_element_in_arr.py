arr=[10,5,8,10,3]
largest=float("-inf")
second=float("-inf")
for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif num<largest and num>second:
        second=num
if second==float("-inf"):
    print('no distinct value found')
else:
    print(second)