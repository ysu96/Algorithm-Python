
def reachTheEnd(grid, maxTime):
    # Write your code here
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    q = [(0,0,0)]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    visited[0][0] = True
    while q:
        r,c,t = q.pop(0)
        if r==len(grid)-1 and c==len(grid[0])-1 and maxTime >= t:
            return "Yes"

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < len(grid) and 0<= nc < len(grid[0]):
                if grid[nr][nc] == '.' and visited[nr][nc] == False:
                    q.append((nr,nc,t+1))
                    visited[nr][nc] = True
    return "No"