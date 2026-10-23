
arr = [3, 1, 4, 1, 5]

n = len(arr)
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

L = 2
R = 4

answer = prefix[R] - prefix[L - 1]

print(answer)
