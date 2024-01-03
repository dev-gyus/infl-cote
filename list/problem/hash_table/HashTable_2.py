# 랜덤의 숫자가 들어있는 배열이 주어짐
# 이 배열에서 연속되는 수의 최대 길이를 구하는 문제
# [2,5,4,3,1,100,200] => [1,2,3,4,5] -> return 5
# 배열의 길이: 0<= length <= 10^9

# O(nLog(n))으로 푸는 방식
def solution_nlogn(nums: [int]) -> int:
    if not nums:
        return 0

    number_dict = {}
    for number in nums:
        number_dict[number] = 1

    list.sort(nums)
    start_number = nums[0]
    next_number = start_number + 1
    count = 0

    for num in number_dict.keys():
        if next_number in number_dict:
            next_number += 1
            count += 1
    return count + 1

# 0(n)으로 푸는 방식
def solution_n(nums: [int]):
    if not nums:
        return 0

    num_dict = {}
    first_num = 0
    for num in nums:
        num_dict[num] = num + 1
        if first_num == 0:
            first_num = num
        elif first_num > num:
            first_num = num

    count = 0
    max_count = 0
    next_num = num_dict[first_num]
    for num in num_dict.keys():
        if next_num in num_dict:
            next_num += 1
            count += 1
            if count > max_count:
                max_count = int(count)
        else:
            next_num = num + 1
            count = 0
    return max_count + 1






if __name__ == '__main__':
    nums = [2, 5, 4, 3, 7, 9, 8, 6, 23, 13, 11, 100]
    # print(solution_nlogn(nums))
    print(solution_n(nums))
