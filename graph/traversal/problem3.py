# keys and rooms
# 첫번째 방을 제외한 나머지 방에 입장하려면 열쇠가 있어야함. 입장하면 그 안에 열쇠뭉치를 찾을 수 있을때
# 모든 방을 방문이 가능한지 여부 반환

def solve(rooms) :
    key_chain = {}
    for key in rooms[0]:
        key_chain[key] = True
    visit = [False for _ in rooms]
    visit[0] = True
    dfs(rooms, rooms[0], visit)
    for visit_result in visit:
        if not visit_result:
            return False
    return True


def dfs(rooms, idx_arr, visit):
    print(f"idx_arr = {idx_arr} ")
    for idx in idx_arr:
        if 0 <= idx < len(rooms) and not visit[idx]:
            visit[idx] = True
            dfs(rooms, rooms[idx], visit)

if __name__ == "__main__":
    room_arr = [[1], [4], [5], [2], [3], [3,4]]
    print(solve(room_arr))