n = int(input())
arr = list(map(int, input().split()))

count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1

best = arr[0]
for x in count:
    if count[x] > count[best]:
        best = x
print(best)