def solution(nums: [int], target: int) -> bool:
    nums_dict = {}
    for num in nums:
        need_value = target - num
        if need_value in nums_dict:
            return True
        else:
            nums_dict[num] = True
    return False


if __name__ == '__main__':
    nums = [5, 9, 10, 20, 60, 200]
    target = 14
    print(solution(nums, target))