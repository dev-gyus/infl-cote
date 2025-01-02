
# {}, [], () 문제
# "{}[]()" 만으로 구성되어있는 문자열이 주어졌을때 괄호가 여닫혔는지 확인하는 코드를 작성
# s = '{{}}[()]' <- return true
# s = '{]}[()]' <- return false

def isValid(s: str):
    closer_stack = []
    for char in s:
        if char == '(':
            closer_stack.append(')')
        elif char == '{':
            closer_stack.append('}')
        elif char == '[':
            closer_stack.append(']')
        # 닫는 괄호들의 차례인 경우
        elif len(closer_stack) <= 0 or closer_stack.pop() != char:
            return False
    return True
