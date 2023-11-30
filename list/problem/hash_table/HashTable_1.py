def solution(nums: [int], target: int) -> bool:
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = True
    for num in nums:
        nums_dict[num] = False
        need_value = target - num
        if need_value in nums_dict and nums_dict[need_value]:
            return True
    return False


if __name__ == '__main__':
    nums = [5, 10, 7, 60, 200]
    target = 14
    print(solution(nums, target))