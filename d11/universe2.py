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

def manhattan(pointa, pointb):
    return abs(pointb[0]-pointa[0]) + abs(pointb[1]-pointa[1])

def expand1(input):
    lines = [l.strip() for l in input]

    lines = np.array([[c for c in x] for x in lines])

    rows_idx = np.array(np.where(np.all(lines == ".", axis = 1))).flatten()
    cols_idx = np.array(np.where(np.all(lines == ".", axis = 0))).flatten()

    lines = np.insert(lines, rows_idx, '.', axis = 0)
    lines = np.insert(lines, cols_idx, '.', axis = 1)

    galaxy_idx = np.transpose((lines == "#").nonzero())
    #print(galaxy_idx)

    total_distance = reduce(lambda x,y: np.sum(x)+np.sum(y), 
                            [np.array([manhattan(galaxy_idx[i], galaxy_idx[j]) for j in range(i+1, len(galaxy_idx))]) for i in range(len(galaxy_idx)-1)])
    print(total_distance)
    return total_distance

def expand2(input):
    lines = [l.strip() for l in input]

    lines = np.array([[c for c in x] for x in lines])

    rows_idx = np.array(np.where(np.all(lines == ".", axis = 1))).flatten()
    cols_idx = np.array(np.where(np.all(lines == ".", axis = 0))).flatten()
    for i in range(0,2):
        lines = np.insert(lines, rows_idx, '.', axis = 0)
        lines = np.insert(lines, cols_idx, '.', axis = 1)

    galaxy_idx = np.transpose((lines == "#").nonzero())
    #print(galaxy_idx)

    total_distance = reduce(lambda x,y: np.sum(x)+np.sum(y), 
                            [np.array([manhattan(galaxy_idx[i], galaxy_idx[j]) for j in range(i+1, len(galaxy_idx))]) for i in range(len(galaxy_idx)-1)])
    
    print(total_distance)
    return total_distance

if __name__ == "__main__":
    one = expand1(lines)
    two = expand2(lines)
    print(one + ((9999998)*(two-one)))    