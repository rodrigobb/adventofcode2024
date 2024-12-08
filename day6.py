### Advent of code - Day 6 (tests) ###
from day6_import import load_map

INPUT_FILENAME = 'day6_input.txt'


def main():
    map, guard = load_map(INPUT_FILENAME)
    print(guard.position)
    while guard.is_in_map(map):
        map[guard.position[0]][guard.position[1]] = 'X'
        guard.move(map)

    print(f"Guard moved {guard.counter} places and finished in {guard.position}")

main()
