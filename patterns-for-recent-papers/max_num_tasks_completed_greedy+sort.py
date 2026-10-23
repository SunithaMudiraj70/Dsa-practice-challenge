'Maximum tasks you can finish in 8 units of time.'
def max_tasks(tasks,limit):
    tasks.sort()
    used=0
    duration=0
    count=0
    for duration in tasks:
        if used+duration<=limit:
            used+=duration
            count+=1
        else:
            break

    return count

print(max_tasks([4, 2, 7, 1, 3], 8))

