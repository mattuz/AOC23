from pathlib import Path
import re
import math
import numpy as np
from functools import reduce

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
p = Path(__file__).with_name("example.txt")
with p.open("r") as f:
    exlines = f.readlines()


def combinations(input, instructions):
    combinations = []
    if input.count("#") == len(input):
        return [input]
    for i in range(2**len(input)):
        combination = []
        for j in range(len(input)):
            if input[j] == "#":
                combination.append("#")
            else:
                replacement = "#" if (i & (1 << j)) else "."
                combination.append(replacement)
        if "".join(combination) not in combinations:
            combinations.append("".join(combination))
    return combinations

def possible_springs(gears, instructions):
    #2^amount of "?"
    unknowns = re.findall(r'[#?]+', gears)
    
    
    instr = [int(i) for i in re.findall(r'\d+', instructions)]
    #print(unknowns)
    combos = []
    for unknown in unknowns:
        #print(unknown)
        print(combinations(unknown, instr))
        
        #print(unknown)
        #print(combinations("?#?#"))
        #print(combinations(unknown))
        pass


if __name__ == "__main__":
    input = exlines
    allowed = [".", "#", "?"]
    for line in input:
        inpt = [part for part in line.split()]
        gears, amount = inpt

        #print(gears,amount)
        possible_springs(gears,amount)

    #print(exlines)
    pass