m = 3
n = 7

grid = [[0] * n for _ in range(m)]
memoization = [[0] * n for _ in range(m)]

def dfs(x, y):
    path_count = 0
    if m-1 == x and n-1 == y:
        return 1
    if x >= m or y >= n: return 0
    if memoization[x][y] > 0:
        return memoization[x][y]
    if x <= m-1:
        path_count += dfs(x+1,y)
    if y <= n-1:
        path_count += dfs(x, y+1)
    if x <= m-1 and y <= n-1 and memoization[x][y] == 0:
        memoization[x][y] = path_count

    return path_count

# dp테이블에서 사실 0번 row의 값들과 0번 column의 값들은 모두 1임
# 이를 미리 세팅하고, x-1, y-1의 값을 더해주는 방식으로 table을 채워주는 방식으로 진행
tablelation = [[-1] * n for _ in range(m)]
def bfs():
    # 초기값 세팅
    for y in range(n):
        tablelation[0][y] = 1
    for x in range(m):
        tablelation[x][0] = 1

    for x in range(1, m):
        for y in range(1, n):
            tablelation[x][y] = tablelation[x-1][y] + tablelation[x][y-1]
    return tablelation[m-1][n-1]



print(dfs(0,0))
print(bfs())