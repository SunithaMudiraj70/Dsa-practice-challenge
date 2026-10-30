def coin_ways(coins,amount):
    MOD=10**9+7
    dp=[0]*(amount+1)
    dp[0]=1
    for c in coins:
        for s in range(c,amount+1):
            dp[s]=dp[s]+dp[s-c]%MOD
    return dp[amount]
print(coin_ways([1,2,5],5))
