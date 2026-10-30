n,k=map(int,input().split())
mod=1000
dp=[1]*(n+1)
dp[0]=0
for _ in range(k-1):
    new=[0]*(n+1)
    for v in range(1,n+1):
        for w in range(v,n+1,v):
            new[w]=(new[w]+dp[v])%mod
    dp=new
print(sum(dp)%mod)
