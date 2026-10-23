arr=[2,3,2,5,3,2]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
print(freq)