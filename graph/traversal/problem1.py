from collections import deque
#
#Number of Islands

def bfs_solid(graph):
    number_of_islands = 0
    visited = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == '1' and (i, j) not in visited:
                print(f"i={i}, j={j}")
                bfs(graph, i, j, visited)
                number_of_islands += 1
    return number_of_islands

def bfs(graph, x, y, visited):
    print(f"x={x}, y={y}")
    queue = deque()
    queue.append((x, y))
    while queue:
        cur_points = queue.popleft()
        cur_x = cur_points[0]
        cur_y = cur_points[1]
        if graph[cur_x][cur_y] == '1' and (cur_x, cur_y) not in visited:
            visited.append((cur_x, cur_y))
        next_x = cur_x + 1
        next_y = cur_y + 1
        if next_x < len(graph) and graph[next_x][cur_y] == '1' and (next_x, cur_y) not in visited:
            queue.append((next_x, cur_y))
        if next_y < len(graph[cur_x]) and graph[cur_x][next_y] == '1' and (cur_x, next_y) not in visited:
            queue.append((cur_x, next_y))

def dfs_solid(graph):
    number_of_islands = 0
    visited = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == '1' and (i, j) not in visited:
                print(f"i={i}, j={j}")
                dfs(graph, (i, j), visited)
                number_of_islands += 1
    return number_of_islands

def dfs(graph, point, visited):
    x = point[0]
    y = point[1]
    print(f"x={x}, y={y}")
    if x >= len(graph):
        return
    if y >= len(graph[x]):
        return
    if graph[x][y] == '1' and (x, y) not in visited:
        visited.append((x, y))
        dfs(graph, (x + 1, y), visited)
        dfs(graph, (x, y + 1), visited)


if __name__ == '__main__':
    grid1 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '1'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    grid2 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '1', '0', '0'],
        ['1', '1', '0', '0', '1'],
        ['1', '1', '0', '1', '0'],
    ]
    print(bfs_solid(grid1))
    print(bfs_solid(grid2))
    print(dfs_solid(grid1))
    print(dfs_solid(grid2))