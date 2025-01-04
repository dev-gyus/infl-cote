# climbing stairs
# 한번에 1스텝, 2스텝 올라가기 가능
# n-1번에서 1스텝, n-2에서 2스텝해서 마지막 계단으로 올라갈 수 있으므로
# n번째 계단에 도착하는 방법의 수는 n-1번째 계단에 도착하는 방법 수 + n-2번째 계단에 도착하는 방법 수

# Topdown
def dfs(stair, memoization):
    if stair == 1:
        return 1
    if stair == 2:
        return 2
    if stair not in memoization:
        memoization[stair] = (dfs(stair - 1, memoization) + dfs(stair - 2, memoization))
    return memoization[stair]

def Topdown(n):
    memoization = {}
    return dfs(n, memoization)


def BottomUp(stairs):
    memoization = {
        1: 1,
        2: 2
    }
    for i in range(3, stairs + 1):
        if i not in memoization:
            memoization[i] = memoization[i-1] + memoization[i-2]
    return memoization[stairs]

if __name__ == '__main__':
    print(Topdown(5))
    print(BottomUp(5))