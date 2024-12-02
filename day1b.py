### Advent of code - Day 1 - Second Exercise ###

INPUT_FILENAME = 'day1_input.txt'


def main():
  dict1 = dict()
  dict2 = dict()
  similarity = 0

  with open(INPUT_FILENAME, 'r') as file:
    for line in file:
        data = line.strip().split()

        value1 = data[0] 
        count_value1 = int(dict1.get(value1, 0))
        dict1[value1] = count_value1 + 1

        value2 = data[-1] 
        count_value2 = int(dict2.get(value2, 0))
        dict2[value2] = count_value2 + 1

  for key in dict1:
     similarity += int(key) * dict1[key] * dict2.get(key, 0)

  print(f"Result: {similarity}")

main()
