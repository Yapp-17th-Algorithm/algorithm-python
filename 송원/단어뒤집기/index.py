import sys
sys.stdin = open("input.txt", "rt")
words = input()
answer = ''
i = 0

while i <= len(words) - 1:
  if words[i] == '<':
    tag = ''
    while words[i] != '>':
      tag += words[i]
      i += 1
    tag += words[i]
    answer += tag
    i += 1
  else:
    # words[i]가 공백일 때를 대비
    if words[i] == ' ':
      answer += words[i]
      i += 1
      continue

    word = ''
    while i <= len(words) - 1 and (words[i] != '<' and words[i] !=' '):
      word += words[i]
      i += 1
    answer += word[::-1]

print(answer)
