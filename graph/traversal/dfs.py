graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}
visit = []

def dfs(cur_v) :
    if cur_v is None or cur_v in visit:
        return
    visit.append(cur_v)
    for v in graph[cur_v]:
        dfs(v)


if __name__ == '__main__':
    dfs('A')
    print(visit)