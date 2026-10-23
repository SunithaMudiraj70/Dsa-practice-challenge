def max_subarray_sum(arr):
    best=arr[0]
    curr=arr[0]
    for i in arr[1:]:
        curr=max(i,curr+i)
        best=max(best,curr)
    return best
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))