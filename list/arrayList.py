# 완전 탐색
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] is target:
#                 return True
#     return False

# sort & two pointer
def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    nums.sort()
    print(nums)
    while l < r:
        if (nums[l] + nums[r]) > target:
            r -= 1
        elif (nums[l] + nums[r]) < target:
            l += 1
        else:
            return True
    return False


print(twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
