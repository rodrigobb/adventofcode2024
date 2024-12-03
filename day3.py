### Advent of code - Day 3 ###
import re
from functools import reduce


INPUT_FILENAME = 'day3_input.txt'

def get_muls(line:str) -> list:
   muls = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)", line)
   return muls

def main():
  result = 0
  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
        muls = get_muls(line)
        factors = list(map(lambda x: int(x[0])*int(x[1]), muls))
        result += reduce(lambda x,y: x+y, factors)
        
  print(f"Result = {result}")

main()
