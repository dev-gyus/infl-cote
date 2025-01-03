

def solve(temperature):
    stack = []
    result = [0 for i in range(len(temperature))]
    # 인덱스를 현재 날짜로 정하고, temp를 현재 날씨로 정함
    for cur_day, temp in enumerate(temperature):
        # 스택에 데이터가 있고, 현재 온도가 스택의 최상단 데이터의 1번인덱스 데이터(기존에 저장해놨던 온도 데이터)보다 높다면
        # 기존에 스택에 쌓인 데이터들은 모두 정리가 가능함
        # 정리할때 현재 날짜와 해당 데이터를 저장한 날짜의 차이를 구해서 저장
        while stack and stack[-1][1] < temp:
            prev_day, prev_temp = stack.pop()
            result[prev_day] = cur_day - prev_day
        # 현재 날짜 및 온도 데이터 저장
        stack.append((cur_day, temp))

    return result


if __name__ == '__main__':
    temp = [73,74,75,71,69,72,76,73]
    print(solve(temp))
