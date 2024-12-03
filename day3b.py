### Advent of code - Day 3 ###
import re
from functools import reduce


INPUT_FILENAME = 'day3_input.txt'

def get_muls(line:str) -> list:
  muls = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", line)
  return muls

def remove_ignored(text:str) -> str:
  clean_text = ""
  next_dont = re.search("don't\\(\\)", text)
  if next_dont is not None:
    next_dont_index = next_dont.span()[0]
    clean_text += text[:next_dont_index]
    
    next_do = re.search("do\\(\\)", text[next_dont.span()[1]:])
    if next_do is not None:
      next_index = next_dont.span()[1] + next_do.span()[0]
      clean_text += remove_ignored(text[next_index:])
  else:
    clean_text += text

  return clean_text

def main():
  text = ""
  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
      text += line

  text = remove_ignored(text)

  muls = get_muls(text)
  factors = list(map(lambda x: int(x[0])*int(x[1]), muls))
  result = reduce(lambda x,y: x+y, factors)
  print(f"Result = {result}")

main()
