'''4.	BFS: a 2×2 grid of all 0s, top-left to bottom-right. → expected 2'''


from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    queue = deque([(0, 0, 0)])          # (row, col, distance)
    visited = {(0, 0)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, distance = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return distance
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, distance + 1))
    return -1

print(shortest_path([[0, 0], [0, 0]]))   # 2