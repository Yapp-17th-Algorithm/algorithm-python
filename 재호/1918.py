def print_without_bracket(stk):
    if len(stk) > 0:
        last_elem = stk.pop()
        if last_elem != '(':
            print(last_elem, end='')


def solution():
    priority = {
        '*': 2, '/': 2,
        '+': 1, '-': 1,
        '(': 0
    }
    expression = input()
    stk = []
    for exp in expression:
        if 'A' <= exp <= 'Z':
            print(exp, end='')
        elif exp == '(':
            stk.append(exp)
        elif exp == ')':
            while len(stk) > 0 and stk[-1] != '(':
                print(stk.pop(), end='')
            stk.pop()
        else:
            while len(stk) > 0 and priority[stk[-1]] >= priority[exp] and stk[-1] != '(':
                print_without_bracket(stk)
            stk.append(exp)
    while len(stk) != 0:
        print_without_bracket(stk)


solution()
