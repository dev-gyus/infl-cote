def dfs(idx, rooms, stack, visited):
    if idx >= len(rooms) or not rooms[idx]:
        return
    visited[idx] = True
    keys = rooms[idx]
    for room_num in keys:
        if room_num < len(rooms) and not visited[room_num]:
            stack.append(room_num)
    if stack:
        next_visit_room_idx = stack.pop()
        dfs(next_visit_room_idx, rooms, stack, visited)


def KR(rooms):
    if not rooms:
        return False
    idx = 0
    stack = []
    visited = [False] * len(rooms)
    dfs(idx, rooms, stack, visited)

    return all(visited)


if __name__ == '__main__':
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(KR(rooms))
    rooms2 = [[1],[2],[1],[3]]
    print(KR(rooms2))
    rooms3 = [[1],[2,3,0],[1],[3]]
    print(KR(rooms3))
    rooms4 = []
    print(KR(rooms4))
    rooms5 = [[]]
    print(KR(rooms5))

    rooms6 = [[1,3],[3,0,1],[1],[2]]
    print(KR(rooms6))