def min_num_rooms(meetings):
    if not meetings:
        return 0
    starts=sorted(start for start,end in meetings)
    ends=sorted(end for start,end in meetings)
    rooms=0
    best=0
    i=0
    j=0
    n=len(meetings)
    while i<n:
        if starts[i]<ends[j]:
            rooms+=1
            best=max(best,rooms)
            i+=1
        else:
            rooms-=1
            j+=1
    return best
meetings=[(0, 30), (5, 10), (15, 20)]
print(min_num_rooms(meetings))
    
        