'''1.	Prefix: a = [2, 4, 6, 8], sum of positions 2 to 3. → expected 10'''

a=[2,4,6,8]
n=len(a)
prefix=[0]*(n+1)
for i in range(n):
  prefix[i+1]=prefix[i]+a[i]
  L=2
  R=3
  answer=prefix[R]-prefix[L-1]
print(answer)