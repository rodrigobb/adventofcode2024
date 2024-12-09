### Advent of code - Day 7 ###
from day7_import import load_map

INPUT_FILENAME = 'day7_input.txt'

def main():
    calibrations = load_map(INPUT_FILENAME)
    result = 0
    for calibration in calibrations:
        calibration.validate(True)

    result = sum([c.result for c in calibrations if c.solved])
    print(f"RESULT={result}")

main()
