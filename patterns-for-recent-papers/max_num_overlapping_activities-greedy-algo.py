def max_activities(intervals):
    intervals.sort(key=lambda item:item[1])
    count=0
    last_end=float('-inf')
    for start,end in intervals:
        if start>=last_end:
            count+=1
            last_end=end
    return count
print(max_activities([(1, 3), (2, 4), (3, 5), (5, 7)]))