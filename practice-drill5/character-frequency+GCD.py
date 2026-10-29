'''
You are given a string S. You may rearrange its characters and then split it into the maximum number of identical pieces.

For example:
S = "ababcc"


There are two as, two bs and two cs.

We can rearrange the string into:
abc | abc


The answer is 2


If we want p identical pieces, p must divide every character frequency. Otherwise, we cannot distribute each character equally across all the pieces.

So p must divide both 4 and 6.
- p = 1 works.
- p = 2 works.
- p = 4 does not divide 6.
The largest valid number is:
\[
\gcd(4,6)=2
\]

For multiple character frequencies, calculate their overall GCD. That is the maximum number of identical pieces'''



from collections import Counter
from math import gcd
s=input().strip()
freq=Counter(s)
answer=0
for count in freq.values():
    answer=gcd(answer,count)
print(answer)