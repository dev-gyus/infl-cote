
# O(n^2)
def solve(nums, target):
    # O(n)
    for i in range(len(nums)):
        # O(n)
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) is target:
                return True
    # 결과적으로 O(n^2)
    return False

# O(NlogN)
def solve2(nums, target):
    # O(NlogN)
    nums.sort()
    left = 0
    right = len(nums) - 1
    # O(n)
    while left != right:
        print(f"left: {left}, right: {right}")
        if (nums[left] + nums[right]) < target:
            left += 1
        elif (nums[left] + nums[right]) > target:
            right -= 1
        else:
            return True
    return False



if __name__ == '__main__':
    # print(solve([1, 2, 3, 4, 5, 6], 20))
    print(solve2([1, 2, 3, 4, 5, 6], 20))
    print(solve2([1, 2, 3, 4, 5, 6], 3))