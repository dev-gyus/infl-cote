from collections import deque


def NumberOfIslands(grid):
    visited = [(0, 0)]
    queue = deque()
    queue.append((0, 0))
    max_x = len(grid[0])
    max_y = len(grid)
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(max_y):
        for j in range(max_x):
            if (i, j) not in visited and grid[i][j] == 1:
                queue.append((i, j))
                visited.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for di in range(4):
                        next_y = y + dy[di]
                        next_x = x + dx[di]
                        if 0 <= next_y < max_y and 0 <= next_x < max_x:
                            if grid[next_y][next_x] == 1 and (next_y, next_x) not in visited:
                                visited.append((next_y, next_x))
                                queue.append((next_y, next_x))
                count += 1
    return count

def numIslands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        # 경계를 벗어나거나 물('0')이거나 이미 방문한 경우
        if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] != 1):
            return

        # 방문한 땅을 '0'으로 표시 (방문 처리)
        grid[i][j] = '0'

        # 상하좌우 인접한 땅 탐색
        dfs(i+1, j)  # 아래
        dfs(i-1, j)  # 위
        dfs(i, j+1)  # 오른쪽
        dfs(i, j-1)  # 왼쪽

    rows, cols = len(grid), len(grid[0])
    islands = 0

    # 모든 셀을 순회하면서 땅('1')을 발견하면 DFS 실행
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                dfs(i, j)  # DFS로 연결된 모든 땅을 방문 처리
                islands += 1  # 하나의 섬을 완전히 탐색한 후 카운트 증가

    return islands

if __name__ == '__main__':
    grids = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0],
    ]
    print(NumberOfIslands(grids))
    grids2 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1],
    ]
    print(NumberOfIslands(grids2))

    print(numIslands(grids))
    print(numIslands(grids2))