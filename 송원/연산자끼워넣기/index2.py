import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")

n = int(input())
maxNumber = 0
minNumber = 1000000000

# 숫자들을 배열에 담는다
numbers = list(map(int, input().split()))

# 연산자들을 배열에 담는다
operators = ['+', '-', '*', '//']
all_operators = []
temp = list(map(int, input().split()))
for i in range(len(temp)):
  for _ in range(temp[i]):
    all_operators.append(operators[i])

# 연산자들의 경우의 수를 모두 구한다
operator_cases = set(permutations(all_operators, len(all_operators)))

# 두 배열을 이중순회하며 값을 구하는데, 값이 최대보다 크면 최대를 교체하고, 최소보다 작으면 최소를 교체한다.
for operator_case in operator_cases:
  equation = str(numbers[0])
  for i in range(len(operator_case)):
    if operator_case[i] == '//' and int(equation) < 0:
      equation = str(-int(equation))
      equation += str(operator_case[i]) + str(numbers[i + 1])
      equation = str(-eval(equation))
    else:
      equation += str(operator_case[i]) + str(numbers[i + 1])
      equation = str(eval(equation))
  
  result = int(equation)

  if result >= maxNumber:
    maxNumber = result
  
  if result <= minNumber:
    minNumber = result

print(maxNumber)
print(minNumber)