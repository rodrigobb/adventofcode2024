### Advent of code - Day 4 ###

INPUT_FILENAME = 'day4_input.txt'

def find_X(matrix:list) -> list:
  result = []
  for i, row in enumerate(matrix):
    result+= [(i,j) for j, item in enumerate(row) if item == 'X']
  return result

def build_matrix() -> list:
  matrix = []
  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
      matrix.append([x for x in line if x != '\n'])
  return matrix

def is_out_of_range(start:tuple, inc:tuple, size:int, rows:int) -> bool:
  return (start[0]+3*inc[0] < 0) or (start[1]+3*inc[1] < 0) or (start[0]+3*inc[0] >= rows) or (start[1]+3*inc[1] >= size)

def is_xmas(matrix:list, start:tuple) -> bool:
  directions = [
    (-1,0),   # N
    (-1,1),   # NE
    (0,1),    # E
    (1,1),    # SE
    (1,0),    # S
    (1,-1),   # SW
    (0,-1),   # W
    (-1,-1)  # NW
  ]
  for dir in directions:
    if is_out_of_range(start, dir, len(matrix[0]), len(matrix)):
      continue

    if matrix[start[0]+dir[0]][start[1]+dir[1]] == 'M' and \
       matrix[start[0]+2*dir[0]][start[1]+2*dir[1]] == 'A' and \
       matrix[start[0]+3*dir[0]][start[1]+3*dir[1]] == 'S':
      return True

  return False

def main():
  result = 0
  input = build_matrix()
  x_list = find_X(input)

  for x in x_list:
    if is_xmas(input, x):
      result+=1

  print(f"XMAS={result}")

main()
