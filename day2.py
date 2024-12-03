### Advent of code - Day 2 ###

INPUT_FILENAME = 'day2_input.txt'


def is_safe(l :list) -> bool:
  for i,j in zip(l, l[1:]):
     if abs(i - j) > 3:
        return False
  
  inc = all(i < j for i, j in zip(l, l[1:]))
  dec = all(i > j for i, j in zip(l, l[1:]))

  return inc or dec


def main():
  result = 0
  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
        data = [int(x) for x in line.strip().split()]
        if is_safe(data):
           result += 1
  
  print(f"{result} safe reports")

main()
