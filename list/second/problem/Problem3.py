from webbrowser import open_new


def non_stack(string: str):
    # ) = 0, } = 1, ] = 2
    count_arr = [0, 0, 0]
    # O(n)
    for s in string:
        if s == "(":
            count_arr[0] += 1
        elif s == "{":
            count_arr[1] += 1
        elif s == "[":
            count_arr[2] += 1
        elif s == ")":
            if count_arr[0] > 0:
                count_arr[0] -= 1
            elif count_arr[0] <= 0:
                return False
        elif s == "}":
            if count_arr[1] > 0:
                count_arr[1] -= 1
            elif count_arr[1] <= 0:
                return False
        elif s == "]":
            if count_arr[2] > 0:
                count_arr[2] -= 1
            elif count_arr[2] <= 0:
                return False
    return True


def using_stack(string: str):
    stack = []
    for s in string:
        if s == "(":
            stack.append(")")
        elif s == "{":
            stack.append("}")
        elif s == "[":
            stack.append("]")
        elif not stack or s != stack.pop():
            return False
    return not stack


if __name__ == '__main__':
    string = "{()[]}"
    string2 = ")("
    string3 = "([]}}}}}"
    string4 = "(((([]}}}}}"
    print(non_stack(string))
    print(non_stack(string2))
    print(non_stack(string3))
    print(non_stack(string4))

    print(using_stack(string))
    print(using_stack(string2))
    print(using_stack(string3))
    print(using_stack(string4))