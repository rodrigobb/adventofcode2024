
class Calibration:
    def __init__(self, raw:str):
        self.solved = False
        result, operands = raw.split(': ')
        self.result = int(result)
        self.operands = [int(x) for x in operands.split() if x != '\n']
    
    def validate(self, extended:bool):
        results = calculate_results(self.operands, extended)
        self.solved = self.result in results
        #print(f"{self.solved} because for {self.operands}, {self.result} in {results}")
    
def calculate_results(input:list, extended:bool):
    if len(input) == 1:
        return input
    
    results = []
    b = input[-1]
    for a in calculate_results(input[:-1], extended):
        results.append(a+b)
        results.append(a*b)
        if extended:
            results.append(int(str(a) + str(b)))

    return results

def load_map(filename:str) -> list:
    calibrations = []
    with open(filename, 'r') as file:
        for line in file:
            calibrations.append(Calibration(line))
    return calibrations


