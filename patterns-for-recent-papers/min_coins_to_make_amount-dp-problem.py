def min_coins(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for value in range(1,amount+1):
        for coin in coins:
            if coin<=value :
                dp[value]=min(dp[value],dp[value-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

print(min_coins([1, 2, 5], 11))  # 3
