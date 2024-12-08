### Advent of code - Day 6 (tests) ###
from day6_import import load_map

INPUT_FILENAME = 'day6_test_input.txt'
TEST_SOLUTION = 41

def test():
    map, guard = load_map(INPUT_FILENAME)
    print(guard.position)
    while guard.is_in_map(map):
        map[guard.position[0]][guard.position[1]] = 'X'
        guard.move(map)

    for line in map:
        print(line)
    print(f"Guard moved {guard.counter} times")
    assert(guard.counter == TEST_SOLUTION)

test()
