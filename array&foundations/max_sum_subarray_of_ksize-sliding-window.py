arr=[2,1,5,1,3,2]
k=3
window_sum=sum(arr[:k])
best=window_sum
for i in range(k,len(arr)):
    window_sum+=arr[i]
    window_sum-=arr[i-k]
    best=max(best,window_sum)
print(best)
