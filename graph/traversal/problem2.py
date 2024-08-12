# 최단 거리 구하는 문제
# 최단 거리는 dfs, bfs로 다 풀 수는 있지만
# 그냥 bfs로 푸는게 효율적 (한 사이클에 모든 방향을 탐색할 수 있기 때문)
from collections import deque

#asdf
#문제에서 grid의 x,y 길이는 동일함
def calculate(grid) :
    if len(grid) == 1 : return 1
    row = len(grid)
    col = len(grid[0])
    row_idx = 0
    col_idx = 0
    start_point = (row_idx, col_idx)
    end_vertex = grid[len(grid) - 1][len(grid[len(grid) - 1]) - 1]
    visited = [[False] * col for _ in range(len(grid[0]))]
    min_path_len = -1
    # 시작 노드와 종점 노드의 값이 1이면 절대로 경로가 만들어 질 수 없으므로 -1 반환
    if grid[start_point[0]][start_point[1]] == '1' or end_vertex == '1' :
        return min_path_len
    queue = deque()
    queue.append((0, 0, 1))
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (1, 1), (1, -1), (-1, -1), (-1, 1)
            ]
    while queue:
        (cur_row, cur_col, cur_len) = queue.popleft()
        if cur_row == row -1 and cur_col == col -1 :
            min_path_len = cur_len
            break
        for dr_r, dr_c in direct:
            next_row = cur_row + dr_r
            next_col = cur_col + dr_c
            if 0 <= next_row < row and 0 <= next_col < col and not visited[next_row][next_col] and grid[next_row][next_col] == '0':
                queue.append((next_row, next_col, cur_len + 1))
                visited[next_row][next_col] = True
    return min_path_len



if __name__ == '__main__':
    grid1 = [
        ['0', '1', '1', '1', '0'],
        ['1', '0', '0', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['0', '0', '0', '1', '0'],
    ]
    print(calculate(grid1))