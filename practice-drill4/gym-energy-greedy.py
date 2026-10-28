'''You start with energy \(E\). There are \(N\) exercises, and exercise \(i\) reduces your energy by \(A[i]\). Each exercise can be performed at most twice.

Your goal is to find the minimum number of exercises needed to bring your energy to zero or below. If it is impossible, return -1.'''

E = 12
A = [2, 5, 3]
A=sorted(A,reverse=True)
need=E
answer=-1
count=0
for drain in A:
    for attempt in range(2):
        need=need-drain
        count=count+1
        if need<=0:
            answer=count
            break
    if need<=0:
        break
print(answer)


