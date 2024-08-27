m = 3
n = 7

grid = [[0] * n for _ in range(m)]
memoization = [[0] * n for _ in range(m)]

def dfs(x, y):
    print(f"x={x}, y={y}")
    path_count = 0
    if m-1 == x and n-1 == y:
        return 1
    if x <= m-1 and y <= n-1 and memoization[x][y] > 0:
        return memoization[x][y]
    if x <= m-1:
        path_count += dfs(x+1,y)
    if y <= n-1:
        path_count += dfs(x, y+1)
    if x <= m-1 and y <= n-1 and memoization[x][y] == 0:
        memoization[x][y] = path_count

    return path_count


print(dfs(0,0))