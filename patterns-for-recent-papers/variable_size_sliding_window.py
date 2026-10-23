'''find the longest subarray whose sum is at most 5'''
arr=[2,1,3,1,1]
limit=5
left=0
best=0
current_sum=0
for right in range(len(arr)):
    current_sum+=arr[right]
    while current_sum>limit:
        current_sum-=arr[left]
        left+=1
    best=max(best,right-left+1)
print(best)
