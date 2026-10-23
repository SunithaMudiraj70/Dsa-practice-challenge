def unique_element(arr):
    result=0
    for num in arr:
        result^=num
    return result
print(unique_element([4,1,2,1,2]))