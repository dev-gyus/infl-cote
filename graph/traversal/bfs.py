from collections import deque


def bfs(graph, start_vertex):
    visit = [start_vertex]
    if graph is None or start_vertex is None or start_vertex not in graph:
        return visit
    queue = deque(start_vertex)

    while queue:
        cur_vertex = queue.popleft()
        for vertex in graph[cur_vertex]:
            if vertex not in visit:
                queue.append(vertex)
                visit.append(vertex)
    return visit

if __name__ == '__main__':
    tarGraph = {
        'A': ['B', 'D', 'E'],
        'B': ['A', 'C', 'D'],
        'C': ['B'],
        'D': ['A', 'B'],
        'E': ['A']
    }

    print(bfs(tarGraph, 'A'))