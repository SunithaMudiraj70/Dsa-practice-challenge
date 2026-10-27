'''All numbers are non-negative. Find the length of the longest contiguous subarray whose sum is ≤ S.

a = [2, 1, 3, 1, 1], S = 5 → 3
a = [6, 7], S = 5 → 0'''


n=int(input())
a=list(map(int,input().split()))
left=0
best=0
current_sum=0
limit=5
for right in range(len(a)):
    current_sum+=a[right]
    while current_sum>limit:
        current_sum-=a[left]
        left+=1
    best=max(best,right-left+1)
print(best)



