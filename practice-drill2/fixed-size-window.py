'''2.	Window: a = [1, 4, 2, 10, 2, 3, 1, 0, 20], K = 4, maximum window sum. → expected 24'''

a = [1, 4, 2, 10, 2, 3, 1, 0, 20]
K=4
window_sum=sum(a[:K])
best=window_sum
for i in range(K,len(a)):
  window_sum+=a[i]
  window_sum-=a[i-K]
  best=max(best,window_sum)
print(best)