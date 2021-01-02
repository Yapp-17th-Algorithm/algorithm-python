import sys
sys.stdin = open("input.txt", "r")

d, number = map(int, input().split())
number = str(number)
move_x, move_y = map(int, input().split())
board_length = 2 ** d

start_x = 0
start_y = 0
length = board_length

def number_to_index(number):
  global start_x
  global start_y
  global length

  length = length // 2

  if number == '1':
    start_x += length
  elif number == '2':
    pass
  elif number == '3':
    start_y += length
  elif number == '4':
    start_x += length
    start_y += length

for num in number:
  number_to_index(num)

target_x = start_x + move_x
target_y = start_y - move_y
target_start_x = 0
target_start_y = 0
result_number = ''
length = board_length

def index_to_number():
  global target_x
  global target_y
  global target_start_x
  global target_start_y
  global result_number
  global length

  length = length // 2

  if target_start_x <= target_x < target_start_x + length and target_start_y <= target_y < target_start_y + length:
    result_number += '2'
  elif target_start_x + length <= target_x < target_start_x + length * 2 and target_start_y <= target_y < target_start_y + length:
    result_number += '1'
    target_start_x += length
  elif target_start_x <= target_x < target_start_x + length and target_start_y + length <= target_y < target_start_y + length * 2:
    result_number += '3'
    target_start_y += length
  elif target_start_x + length <= target_x < target_start_x + length * 2 and target_start_y + length <= target_y < target_start_y + length * 2:
    result_number += '4'
    target_start_x += length
    target_start_y += length


while len(result_number) < d:
  index_to_number()

print(result_number)

# 이제 이거 최적화만 하면 될 듯?