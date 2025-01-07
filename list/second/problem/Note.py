import heapq
from collections import defaultdict

# 최소비용 + 가중치
# priority queue - heapq 라이브러리 사용
# heap은 리스트로도 표현이 가능
def Djikstra(times, n, k):
    graph = defaultdict(list)
    for from_v, to_v, weight in times:
        graph[from_v].append((weight, to_v))

    costs = {}
    pq = []
    heapq.heappush(pq, (0, k))
    while pq:
        cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cost
            for weight, to_v in graph[cur_v]:
                new_cost = cost + weight
                heapq.heappush(pq, (new_cost, to_v))
    if len(costs) != n:
        return -1
    return max(costs.values())

def sunyeol(nums, target):
    ans = []
    def backtracking(curr, x):
        # 맨마지막인 경우
        if len(curr) == x:
            ans.append(curr[:])
            return

        for i in nums:
            curr.append(i)
            backtracking(curr, x)
            curr.pop()

    backtracking([], target)
    return ans

def johap(nums, target):
    ans = []
    def backtracking(start, curr):
        # 맨마지막인 경우
        if len(curr) == target:
            ans.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

    backtracking(0, [])
    return ans


if __name__ == '__main__':
    times = [[2,1,1], [2,3,1], [3,4,1]]
    n = 4
    k = 2

    print(Djikstra(times, n, k))

    times2 = [[1,2,1]]
    n = 2
    k = 2
    print(Djikstra(times2, n, k))

    nums = [2,4,3,1]
    print(sunyeol(nums, 2))

    nums = [2,4,3,1]
    print(johap(nums, 2))