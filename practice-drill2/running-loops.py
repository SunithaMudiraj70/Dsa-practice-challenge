'''Given an array, find the first position i where the sum of elements to the left of i equals the sum to the right. Print that index (0-based), or -1 if none exists.

[1, 7, 3, 6, 5, 6] → 3
[1, 2, 3] → -1'''

#bruteforce:
a=[1,7,3,6,5,6]
answer=-1
'''for i in range(len(a)):
    if sum(a[:i])==sum(a[i+1:]):
        answer=i
print(answer)'''
#complexity:o(N^2)
#optimal code:
left=0
total=sum(a)
for i in range(len(a)):
    right=total-left-a[i]
    if left==right:
        answer=i
        break
    left+=a[i]
print(answer)
#complexity:o(N)

