'''
Andy has \(N\) days. Some days have obligations that he must attend. He is allowed to cancel at most \(K\) obligations.

After cancelling obligations, he wants the longest consecutive block of days with no obligations.

Your task is to return the maximum possible length of that free block.
Example
Suppose:
- Total days: \(N=10\)
- Obligation days: [2, 3, 6, 7, 9]
- Maximum cancellations: \(K=2\)'''

N=10
M=5
K=2
days=[2,3,6,7,9]
days.sort()
days=[0]+days+[N+1]
for i in range(M-K+1):
    K=min(K,M)
    best=0
    free_days=days[i+K+1]-days[i]-1
    best=max(best,free_days)
print(best)

