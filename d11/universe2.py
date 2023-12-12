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

def expand1(input, m):
    lines = [l.strip() for l in input]

    lines = np.array([[c for c in x] for x in lines])

    rows_idx = np.array(np.where(np.all(lines == ".", axis = 1))).flatten()
    cols_idx = np.array(np.where(np.all(lines == ".", axis = 0))).flatten()
    
    #for i in range(0, r):
    #lines = np.insert(lines, rows_idx, '.', axis = 0)
    #lines = np.insert(lines, cols_idx, '.', axis = 1)

    #print(len(lines[0]))
    galaxy_idx = np.transpose((lines == "#").nonzero())
    #print(galaxy_idx)
    #print(cols_idx)
    glx = []
    row_passed = 0
    for r, line in enumerate(lines):
        col_passed = 0
        if r in rows_idx:
            row_passed += 1
        for c, char in enumerate(line):
            if c in cols_idx:
                col_passed += 1
            if char == "#":
                #print(row_passed)
                glx.append([r+(row_passed*(m-1)), c+(col_passed*(m-1))])

                #print(galaxy_idx[0])
    glx = np.array(glx)
    #print(glx)


    total_distance = reduce(lambda x,y: np.sum(x)+np.sum(y), 
                            [np.array([manhattan(galaxy_idx[i], galaxy_idx[j]) for j in range(i+1, len(galaxy_idx))]) for i in range(len(galaxy_idx)-1)])
    pt2 = reduce(lambda x,y: np.sum(x)+np.sum(y), 
                            [np.array([manhattan(glx[i], glx[j]) for j in range(i+1, len(glx))]) for i in range(len(glx)-1)])
    print(pt2)
    #print(total_distance)
    return total_distance

if __name__ == "__main__":
    print(expand1(lines, 1000000))