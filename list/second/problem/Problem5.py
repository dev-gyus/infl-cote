
# Sort & Two Pointers
# O(NlogN)
def solve(nums, target):
    # O(NlogN)
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        if (nums[left] + nums[right]) > target:
            right -= 1
        elif (nums[left] + nums[right]) < target:
            left += 1
        else:
            return True
    return False

# Dict 이용 (O(N)
def solve2(nums, target):
    dictionary = {}
    # O(n)
    for num in nums:
        dictionary[num] = True
    # O(n)
    for num in nums:
        # 자기자신은 제외
        dictionary.pop(num)
        if (target - num) in dictionary:
            return True
    return False


if __name__ == '__main__':
    nums = [2, 1, 5, 7]
    target = 4
    print(solve2(nums, target))