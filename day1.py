### Advent of code - Day 1 ###

INPUT_FILENAME = 'day1_input.txt'


def main():
  list1 = list()
  list2 = list()
  distance = 0

  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
        data = line.strip().split()
        list1.append(int(data[0]))
        list2.append(int(data[-1]))
  
  list1.sort()
  list2.sort()

  for a, b in zip(list1, list2):
     distance += abs(a-b)

  print(f"The distance between list 1 ({len(list1)} items) and list 2 ({len(list2)} items) is {distance}")

main()
