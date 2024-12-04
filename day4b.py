### Advent of code - Day 4 ###

INPUT_FILENAME = 'day4_input.txt'

def find_A(matrix:list) -> list:
  result = []
  for i, row in enumerate(matrix):
    result+= [(i,j) for j, item in enumerate(row) if item == 'A']
  return result

def build_matrix() -> list:
  matrix = []
  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
      matrix.append([x for x in line if x != '\n'])
  return matrix

def is_out_of_range(start:tuple, size:int, rows:int) -> bool:
  return (start[0]-1 < 0) or (start[1]-1 < 0) or (start[0]+1 >= rows) or (start[1]+1 >= size)

def is_x_mas(matrix:list, start:tuple) -> bool:
  if is_out_of_range(start, len(matrix[0]), len(matrix)):
    return False

  """
  M . S   M . M   S . M   S . S
  . A .   . A .   . A .   . A .
  M . S   S . S   S . M   M . M
  """
  return (matrix[start[0]-1][start[1]-1] == 'M' and matrix[start[0]-1][start[1]+1] == 'S' and matrix[start[0]+1][start[1]-1] == 'M' and matrix[start[0]+1][start[1]+1] == 'S') or \
     (matrix[start[0]-1][start[1]-1] == 'M' and matrix[start[0]-1][start[1]+1] == 'M' and matrix[start[0]+1][start[1]-1] == 'S' and matrix[start[0]+1][start[1]+1] == 'S') or \
     (matrix[start[0]-1][start[1]-1] == 'S' and matrix[start[0]-1][start[1]+1] == 'M' and matrix[start[0]+1][start[1]-1] == 'S' and matrix[start[0]+1][start[1]+1] == 'M') or \
     (matrix[start[0]-1][start[1]-1] == 'S' and matrix[start[0]-1][start[1]+1] == 'S' and matrix[start[0]+1][start[1]-1] == 'M' and matrix[start[0]+1][start[1]+1] == 'M')

def main():
  result = 0
  input = build_matrix()
  A_list = find_A(input)

  for a in A_list:
    if is_x_mas(input,a):
      result+=1

  print(f"X-MAS={result}")

main()
