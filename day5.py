### Advent of code - Day 5 ###
from day5_import import process_input, is_valid_order

INPUT_FILENAME = 'day5_input.txt'

def main():
  rules, orders = process_input(INPUT_FILENAME)
  valid_orders =[order for order in orders if is_valid_order(order, rules)]
  middle_pages = [v[int(len(v)/2)] for v in valid_orders]

  result = sum(middle_pages)
  print(f"Result={result}")

main()
