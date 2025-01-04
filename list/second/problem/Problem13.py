import heapq


def NDT(times, n, k):
    nodes = {}
    for from_v, to_v, value in times:
        if from_v not in nodes:
            nodes[from_v] = []
        nodes[from_v].append((value, to_v))
    pq = []
    costs = {}
    heapq.heappush(pq, (0, k))
    while pq:
        cur_v_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_v_cost
            if cur_v in nodes:
                for to_v_cost, to_v in nodes[cur_v]:
                    next_cost = to_v_cost + cur_v_cost
                    heapq.heappush(pq, (next_cost, to_v))
    if len(costs) != n:
        return -1
    # 동시에 보낼 수 있으므로 최대값만 조회하면 그 값보다 낮은 비용이 드는 버텍스에는 이미 신호가 모두 도달 할 것임
    else:
        return max(costs.values())

if __name__ == '__main__':
    times = [[2,1,2], [2,3,5], [2,4,1], [4,3,3]]
    n = 4
    k = 2

    print(NDT(times, n, k))