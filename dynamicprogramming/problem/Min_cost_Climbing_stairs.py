# 계단을 오르는데, 각 계단마다 가중치가 있음
# 맨 꼭대기층까지 올라가는데 가중치의 총합의 최소값을 구하는문제
# 2<=n<=1000

# 아래 dfs를 하게되면 O(n^2)으로 최대 2^1000이 가능하기때문에 timeout 발생 => Memoization을 사용한 DP를 이용해 문제해결
# 풀이
def brute_force_solve(cost):
    return brute_force_dfs(len(cost), cost)

def brute_force_dfs(n, cost) :
    if n == 0 or n == 1:
        return 0
    print(n)
    return min((brute_force_dfs(n - 1, cost) + cost[n - 1]), (brute_force_dfs(n - 2, cost) + cost[n - 2]))

def dp_solve(cost):
    memoization = {}
    return dp_dfs(len(cost), cost, memoization)

def dp_dfs(n, cost, memoization):
    if n == 0 or n == 1:
        return 0
    if n not in memoization:
        memoization[n] = min((dp_dfs(n-1, cost, memoization) + cost[n-1]), (dp_dfs(n-2, cost, memoization) + cost[n-2]))
    print (n)
    return memoization[n]





if __name__ == '__main__':
    cost = [1,100,1,2,3,100,100,1000,200,300,400,200,300,100,200]
    print(brute_force_solve(cost))
    print()
    print()
    print(dp_solve(cost))
