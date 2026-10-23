'''this is a sliding window pattern
how to recognise:the shortest or longest subarray of a string without repeating characters,find the length of contiguos subarray
Longest or shortest contiguous substring/subarray satisfying a condition. '''
def longest_unique(s):
    left=0
    last_seen={}
    best=0
    for right,ch in enumerate(s):
        if ch in last_seen and last_seen[ch]>=left:
            left=last_seen[ch]+1
        last_seen[ch]=right
        best=max(best,right-left+1)
    return best
print(longest_unique('abcabcbb'))