# 총 계단의 수 = n
# 1 <= n <= 45
# 한 번에 계단 1칸 혹은 2칸을 오를 수 있으며
# 이 경우 n개의 계단이 주어지면 오를 수 있는 방법의 수를 구하는 문제

# bottom - up? / top - down ?
# 1 - 1
# 11, 2 - 2
# 111, 12, 21 - 3
# 1111, 112, 121, 211, 22 - 5
# 11111, 1112, 1211, 2111, 1121, 122, 221, 212 - 8
# 111111, 11112, 11121, 11211, 12111, 21111, 1122, 1212, 1221, 2121, 2112, 2211, 222 - 13

# 피보나치 수

top_down_memoization = {}
def top_down_climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in top_down_memoization:
        top_down_memoization[n] = top_down_climb_stairs(n - 1) + top_down_climb_stairs(n - 2)
    return top_down_memoization[n]

bottom_up_memoization = {
    1: 1,
    2: 2
}
def bottom_up_climb_stairs(n):
    for idx in range(3, n):
        if n not in top_down_memoization:
            top_down_memoization[n] = top_down_climb_stairs(n - 1) + top_down_climb_stairs(n - 2)
    return top_down_memoization[n]

if __name__ == '__main__':
    n = 6
    print(top_down_climb_stairs(n))
    print(bottom_up_climb_stairs(n))