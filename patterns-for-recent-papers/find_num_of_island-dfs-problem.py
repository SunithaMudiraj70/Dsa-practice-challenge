def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    rows,cols=len(grid),len(grid[0])
    visited=set()
    count=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]!="1"or (r,c) in visited:
                continue
            count+=1
            visited.add((r,c))
            stack=[(r,c)]
            while stack:
                x,y=stack.pop()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+dy,y+dy
                    if (0<nx<rows) and (0<ny<cols) and grid[nx][ny]=="1" and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        stack.append((nx,ny))
    return count     
grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["0","0","0","0"]
]
print(num_islands(grid))    