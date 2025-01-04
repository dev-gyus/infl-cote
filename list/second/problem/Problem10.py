from collections import deque

def SPBM(grid):
    ans = -1
    # (0,0)이 1이면 가는길 없음
    if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
        return ans
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    visited = [[False] * len(grid[0]) for i in range(len(grid))]
    queue = deque()
    queue.append((1, (0, 0)))
    while queue:
        length, cur_yx = queue.popleft()
        cur_y = cur_yx[0]
        cur_x = cur_yx[1]
        visited[cur_y][cur_x] = True
        print(length, cur_y, cur_x)
        if cur_y == (len(grid) - 1) and cur_x == (len(grid[0]) - 1):
            if ans <= 0:
                ans = length
            else:
                ans = min(ans, length)
        for i in range(8):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            # 다음 y, x값이 방문이 가능한 idx값이고, 방문을 해야하는 곳이고 (값이 0이면), 다음 방문할 곳을 아직 방문하지 않았다면 방문 예약
            if 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0]):
                if grid[next_y][next_x] == 0 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((length + 1, (next_y, next_x)))
    return ans


if __name__ == '__main__':
    grid = [
        [0,0,0],
        [1,1,0],
        [1,1,0],
    ]
    print(SPBM(grid))

    grid2 = [
        [1,0,0],
        [1,1,0],
        [1,1,0],
    ]
    print(SPBM(grid2))

    grid3 = [
        [0,0,0],
        [1,0,0],
        [1,1,0],
    ]
    print(SPBM(grid3))

    grid4 = [
        [0,0,0],
        [0,1,0],
        [0,0,0],
    ]
    print(SPBM(grid4))