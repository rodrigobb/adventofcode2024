### Advent of code - Day 7 (tests) ###
from day7_import import load_map

INPUT_FILENAME = 'day7_test_input.txt'
TEST_SOLUTION = 3749
TEST_EXTENDED_SOLUTION = 11387

def test():
    calibrations = load_map(INPUT_FILENAME)
    result = 0
    for calibration in calibrations:
        calibration.validate(False)

    result = sum([c.result for c in calibrations if c.solved])
    assert(result == TEST_SOLUTION)

    for calibration in calibrations:
        calibration.validate(True)

    result = sum([c.result for c in calibrations if c.solved])
    assert(result == TEST_EXTENDED_SOLUTION)


test()
