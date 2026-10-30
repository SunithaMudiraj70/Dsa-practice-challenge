'''Given two strings, find the longest sequence of characters appearing in both strings in the same order, not necessarily consecutively.

Example:
s1 = "abcde"
s2 = "ace"'''
def lcs(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
print(lcs("abcde","abc"))

        