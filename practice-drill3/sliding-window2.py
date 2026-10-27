'''All numbers are non-negative. Find the length of the shortest contiguous subarray whose sum is ≥ S. Print 0 if none exists.

[2, 3, 1, 2, 4, 3], S = 7 → 2 (the subarray [4, 3])
[1, 1, 1], S = 10 → 0
[5], S = 5 → 1'''


n,s=map(int,input().split())
a=list(map(int,input().split()))
left=0
best=n+1
current_sum=0
for right in range(n):
    current_sum+=a[right]
    while current_sum>=s:
        best=min(best,right-left+1)
        current_sum-=a[left]
        left+=1
if best == n+1:
        print(0)
else:
    print(best)