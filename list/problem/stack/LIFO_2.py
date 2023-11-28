# 온도 문제
# 각 인덱스별로 더 높은 온도가 나올때까지의 일자를 구하는 문제
# ex: [73, 75, 74, 72, 69, 78] -> [1, 4, 3, 2, 1, 0]
# 높은 온도가 끝까지 안나오면 0으로 처리
def solution(temperature: [int]):
    # 배열 [0,0,0, ~] 으로 세팅
    answer = [0] * len(temperature)
    stack = []
    cur_day = 0
    for temp in temperature:
        while stack and stack[-1][1] < temp:
            temp_tuple = stack.pop()
            save_day = temp_tuple[0]
            answer[save_day] = cur_day - save_day
        else:
            stack.append((cur_day, temp))
        cur_day += 1
    return answer


if __name__ == '__main__':
    temperature = [73, 75, 74, 72, 69, 78]
    print(solution(temperature))
