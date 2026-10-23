arr = [0, 0, 0, 0, 0]
n = len(arr)
diff = [0] * (n + 1)

updates = [(1, 3, 3), (2, 4, 2)]

for left, right, value in updates:
    diff[left] += value
    diff[right + 1] -= value

running = 0

for i in range(n):
    running += diff[i]
    arr[i] += running

print(arr)