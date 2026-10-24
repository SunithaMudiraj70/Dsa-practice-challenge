n= int(input())
arr = list(map(int, input().split()))

count = {}
for ch in arr:
  count[ch]=count.get(ch,0)+1
answer=-1

  
for ch in arr: 
  if count[ch]==1:
      answer=ch
print(answer)