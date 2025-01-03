
# nums 배열을 가지고 만들 수 있는 가장 긴 연속 된 수의 갯수
def solve(nums):
    # O(NlogN)
    nums.sort()
    keys = {}
    for num in nums:
        keys[num] = True
    result = []
    ans = 0
    # O(N)
    for idx, num in enumerate(nums):
        if keys.get(num):
            result.append(keys.pop(num))
        if num + 1 not in keys:
            ans = max(ans, len(result))
            result = []
    return ans

if __name__ == '__main__':
    arr = [0,3,7,2,5,8,4,6,0,1]
    arr2 = [100,4,200,1,3,2]
    print(solve(arr))
    print(solve(arr2))