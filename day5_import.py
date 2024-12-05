from functools import cmp_to_key

def process_input(filename:str):
    rules = []
    orders = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            if line.find('|') > 0:
                rules.append(tuple([int(x) for x in line.split('|')]))

            if line.find(',') > 0:
                orders.append([int(x) for x in line.split(',')])
    return rules, orders

def custom_order(x, y):
    if x < y:
        return -1
    if x > y:
        return 1    
    return 0

def is_valid_order(order:list, rules:list) -> bool:
    for i in range(0, len(order)):
        for j in range(i+1,len(order)):
            if (order[j], order[i]) in rules:
                return False
    return True