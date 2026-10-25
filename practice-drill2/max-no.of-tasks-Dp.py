def max_tasks(tasks, limit):
    tasks.sort()
    used = 0
    count = 0
    for t in tasks:
        if used + t <= limit:
            used += t
            count += 1
        else:
            break
    return count

print(max_tasks([5, 3, 8, 1], 9))   # 3
print(max_tasks([8, 5, 1], 9))      # 2