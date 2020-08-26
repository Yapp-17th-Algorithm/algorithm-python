def is_expression(char):
    return char == '*' or char == '+' or char == '/' or char == '-'


def cal(a, b, exp):
    if exp == '*':
        return a * b
    if exp == '/':
        return a / b
    if exp == '+':
        return a + b
    if exp == '-':
        return a - b


def solution():
    char_dict = {}
    N = int(input())
    exps = input()
    for i in range(N):
        char_dict[chr(i + 65)] = int(input())

    num_stack = []
    for exp in exps:
        if exp in char_dict.keys():
            exp = char_dict[exp]
        if is_expression(exp):
            last_num = num_stack.pop()
            last_second_num = num_stack.pop()
            num_stack.append(cal(last_second_num, last_num, exp))
        else:
            num_stack.append(exp)

    print('%.2f' % num_stack[0])


solution()
