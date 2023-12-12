from pathlib import Path
import re
import math
import numpy as np

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
p = Path(__file__).with_name("example.txt")
with p.open("r") as f:
    exlines = f.readlines()

def expand():
    cols = []
    rows = []
    for col, char in enumerate(lines[0]):
        char = char.strip("\n")
        i = 0
        while char == ".":
            char = lines[i][col]
            if i == len(lines)-1:
                if char != ".":
                    break
                cols.append(col)
                break
            i += 1   
    
    for col in cols[::-1]:
        for row, line in enumerate(lines):
            for c, char in enumerate(line):
                if c == int(col):
                    new = line[:c] + "." + line[c:]
                    lines[row] = new
    for row, line in enumerate(lines):
        line = line.strip("\n")
        re.findall(r"\.", line)
        if len(re.findall(r"\.", line)) == len(line):
            addline = line.strip("\n")
            rows.append(row)
            pass
    for row in rows:
        lines.insert(row+1, addline+"\n")
    print("cols",cols)
    print("rows",rows)

def manhattan(pointa, pointb):
    return abs(pointb[0]-pointa[0]) + abs(pointb[1]-pointa[1])




if __name__ == "__main__":
    expand()
    done = []
    tot = 0
    i = 0
    for ys, sline in enumerate(lines):
        print(sline)
        for xs, schar in enumerate(sline):
            if schar == "#" and (xs, ys) not in done:
                done.append((xs, ys))
                for y, line in enumerate(lines):
                    for x, char in enumerate(line):
                        if char == "#" and (x, y) not in done:
                            i += 1
                            tot += manhattan((xs, ys), (x, y))
    
    print(i)
    print(tot)

                

    