n = int(input())
arr = list(map(int, input().split()))

count = {}
for x in arr:
    count[x] = count.get(x, 0) + 1

answer = 0
for x in count:              # each distinct value once
    if count[x] == 2:
        answer += 1
print(answer)