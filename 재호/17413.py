def append_reverse_word_to_stk(stk, word_stk):
    word_stk.reverse()
    stk += word_stk


def solution():
    S = input()
    stk = []
    word_stk = []
    flag = False
    for char in S:
        if char == '<':
            flag = True
            if len(word_stk) > 0:
                append_reverse_word_to_stk(stk, word_stk)
                word_stk = []
            stk.append(char)
        elif char == '>':
            flag = False
            stk.append(char)
        else:
            if flag:
                stk.append(char)
            elif not flag and char == ' ':
                append_reverse_word_to_stk(stk, word_stk)
                word_stk = []
                stk.append(char)
            else:
                word_stk.append(char)
    if len(word_stk) > 0:
        append_reverse_word_to_stk(stk, word_stk)
    print(''.join(stk))


solution()
