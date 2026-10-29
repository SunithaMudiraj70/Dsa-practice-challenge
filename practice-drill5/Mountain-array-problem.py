'''The workbook defines a mountain as an array that increases by exactly 1 toward the middle and decreases by exactly 1 toward the other end. Both ends must have the same value.

For example:
[1, 2, 3, 2, 1]       # valid[6, 7, 8, 8, 7, 6]    # valid[1, 2, 3, 4, 5]       # not valid



Given an array, change as few elements as possible to make it a mountain.'''

n=int(input())
a=list(map(int,input().split()))
freq={}
for i in range(n):
    base=a[i]-min(i,n-1-i)
    freq[base]=freq.get(base,0)+1
print(n-max(freq.values()))