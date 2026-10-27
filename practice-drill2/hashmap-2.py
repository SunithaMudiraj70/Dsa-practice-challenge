n, k = map(int, input().split())
a = list(map(int, input().split()))

found = False
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            found = True
            break               # leaves the inner loop
    if found:
        break                   # leaves the outer loop
print("YES" if found else "NO")


'''optimal code:
n, k = map(int, input().split())
a = list(map(int, input().split()))

seen = set()                    # values we've passed so far
found = False
for x in a:
    if k - x in seen:           # CHECK first
        found = True
        break
    seen.add(x)                 # STORE after
print("YES" if found else "NO")'''