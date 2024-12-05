### Advent of code - Day 5 ###
from day5_import import process_input, is_valid_order
from day5_test_out import TEST_VALID_PAGES

INPUT_FILENAME = 'day5_test_input.txt'

def test():
  rules, orders = process_input(INPUT_FILENAME)
  valid_orders =[order for order in orders if is_valid_order(order, rules)]
  middle_pages = [v[int(len(v)/2)] for v in valid_orders]

  print(middle_pages)
  assert(middle_pages == TEST_VALID_PAGES)

test()
