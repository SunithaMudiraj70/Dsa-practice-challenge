'''question:count how many positions i have left sum equal to right sum.

[0, 0, 0] → 3
[1, 2, 3] → 0
[1, 7, 3, 6, 5, 6] → 1'''


n=int(input ())
a=list(map(int,input().split()))
'''count=0
for i in range(len(a)):
    if sum(a[:i])==sum(a[i+1:]):
        count+=1
print(count)'''
#o(N):
count=0
left=0
total=sum(a)
for i in range(len(a)):
    right=total-left-a[i]
    if left==right:
        count+=1
    left+=a[i]
    
    

print(count)


        




