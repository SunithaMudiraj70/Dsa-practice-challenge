'''LIS with a bitwise condition
Ordinary LIS means the longest strictly increasing subsequence. The workbook's reported Infosys variant adds a condition between adjacent values:
(x&y)* 2 < (x|y)

Here, & is bitwise AND and | is bitwise OR.'''

def lis_with_condition(a):
    n=len(a)
    if n==0:
        return 0
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            x=a[j]
            y=a[i]
            if x<y and (x&y)*2<(x|y):
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(lis_with_condition([15, 6, 5, 12, 1]))
print(lis_with_condition([17, 16, 12, 2, 8, 17, 17]))

