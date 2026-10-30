def knapsack(items,w):
    dp=[0]*(w+1)
    for weight,value in items:
        for cap in range(w,weight-1,-1):
            dp[cap]=max(dp[cap],dp[cap-weight]+value)
    return dp[w]
print(knapsack([(1, 1), (3, 4), (4, 5)], 4))

