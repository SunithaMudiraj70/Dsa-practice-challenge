n=int(input())
a=list(map(int,input().split()))
K=6
# partner=K-x
'''count=0
for i in range(len(a)): 
    for j in range(i+1,len(a)):
        if a[i] + a[j] == K :
            count+=1
print(count)'''

#optimal-code:o(n):
count={}
pairs=0
for i in a:
    pairs+=count.get(K-i,0)
    count[i]=count.get(i,0)+1
print(pairs)



