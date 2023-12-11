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



    

#letter :[
# [up]
# [right]
# [down]
# [left]
# ]
allowed = {
    "S": [
        ["|", "7", "F"], 
        ["-", "J", "7"],
        ["|", "L", "J"],
        ["-", "L", "F"]
    ],
    "|": [
        ["|", "7", "F", "S"], 
        [],
        ["|", "L", "J", "S"],
        []
    ],
    "-": [
        [], 
        ["-", "J", "7", "S"],
        [],
        ["-", "L", "F", "S"]
    ],
    "L": [
        ["|", "7", "F", "S"], 
        ["-", "J", "7", "S"],
        [],
        []
    ],
    "J": [
        ["|", "7", "F", "S"], 
        [],
        [],
        ["-", "L", "F", "S"]
    ],
    "7": [
        [], 
        [],
        ["|", "L", "J", "S"],
        ["-", "L", "F", "S"]
    ],
    "F": [
        [], 
        ["-", "J", "7", "S"],
        ["|", "L", "J", "S"],
        []
    ]
}

olist = []
for line in lines:
    n = []
    for ch in line:
        n.append("O")
    olist.append(n)



def pipecalc():
    for row, line in enumerate(lines):
        for column, c in enumerate(line):
            if c == "S":
                x, y = row, column
    pipe("S", x, y)

    pass

def pipe(pipe, x, y):
    pipe = None
    start = x, y
    curr = start
    prev = None
    depth = 0
    while pipe != "S":
        if pipe == None:
            pipe = "S"
        for dir in range(4):
            x, y = curr
            if dir == 0 and x-1 >= 0:
                next = x-1, y
                if lines[x-1][y] in allowed[pipe][dir] and next != prev:
                    #print("up")
                    pipe = lines[x-1][y]
                    prev = curr
                    curr = next
                    depth += 1
                    olist[x-1][y] = pipe
                    break
                pass
            elif dir == 1 and y+1 <= len(lines[x])-1:
                next = x, y+1
                if lines[x][y+1] in allowed[pipe][dir] and next != prev:
                    
                    pipe = lines[x][y+1]
                    prev = curr
                    curr = next
                    #print("right")
                    depth += 1
                    olist[x][y+1] = pipe
                    break
                pass
            elif dir == 2 and x+1 <= len(lines)-1:
                next = x+1, y
                if lines[x+1][y] in allowed[pipe][dir] and next != prev:
                    #print("down")
                    pipe = lines[x+1][y]
                    prev = curr
                    curr = next
                    depth += 1
                    olist[x+1][y] = pipe
                    break
                pass
            elif dir == 3 and y-1 >= 0:
                next = x, y-1
                if lines[x][y-1] in allowed[pipe][dir] and next != prev:
                    pipe = lines[x][y-1]
                    prev = curr
                    curr = next
                    depth += 1
                    olist[x][y-1] = pipe
                    break
                pass
        #print(pipe, depth)
    print("ans:", round(depth/2))
    pass

if __name__ == "__main__":
    pipecalc()
    #print(olist)
    for row, line in enumerate(olist):
        for col, c in enumerate(line):
            if c == "J":
                olist[row][col] = "╝"
            elif c == "7":
                olist[row][col] = "╗"
            elif c == "F":
                olist[row][col] = "╔"
            elif c == "L":
                olist[row][col] = "╚"
            elif c == "|":
                olist[row][col] ="║"
            elif c == "-":
                olist[row][col] = "═"
            elif c == "S":
                olist[row][col] = "═"
    for line in olist:
        n = ""
        for c in line:
            n = n + c
        line = n
        #print(line)
    #print("╚╗╔╝═║")
    RE_VERTICAL_BORDER = re.compile("╚═*╗|╔═*╝|║")
    #kollar basically allt som "är en vägg"
    inside = 0
    for line in olist:
        n = ""
        for c in line:
            n = n + c
        line = n
        for column, c in enumerate(line):
            if c not in "╚╗╔╝═║":
                #print(line)
                matches = RE_VERTICAL_BORDER.findall(line[:column])
                if line == "OOOOOOOOOOOOO╚╗╚╗╔╗╔╗║║╔╝╚╝╚╝╔╗║╔╗╔═════╝╚╝╚════╝╔╗╚╝╔╗╔╝╔══╝OOOOOOOOOOOOO╚═╗╔╗╔╝╚╗╔╗╚╝╚╝╔═╝╚═╗║╚═╗║╚╗╚╝╔═╗║║╔╝║║║║╚═══╗║╔╝╔╗╔╗╔══╗OOOOOOOOOO":
                    print(matches)
                if len(matches) % 2 == 1:
                    inside += 1
    print(inside)
    

    """print(
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO║║OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO║╚═╗╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO║║╔═╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╗╔╝║║OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO╔╗╔══╝║║╔╝╔╗OOOOOOOOOOOOOOO╔╗OOOOOOOOOOOOOOO╔═╝║╔╝╚╗OOOOO╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO║║╚╗╔═╝║║╔╝╚╗OOOOOOOOOOOOOO║║OOOOOOOOOOOOO╔╗╚╗╔╝╚═╗╚╗╔╗OO║╚╗╔═══╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO║║O║║╔╗║╚╝╔═╝OOOOOO╔╗OOOOO╔╝║OOOOOOOOOOO╔═╝║╔╝╚═╗O╚╗║║╚╗O╚╗║╚═╗╔╝OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO║╚═╝║║║╚╗╔╝O╔╗OOOO╔╝╚╗OOOO║╔╝OOOOOO╔══╗O╚═╗║╚╗╔═╝╔═╝║║╔╝╔═╝╚╗O║║OOO╔╗╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO╚══╗║║╚═╝╚╗O║╚╗OOO║╔═╝╔╗O╔╝║OOOOOOO╚╗╔╝O╔═╝╚╗║║OO╚═╗║║╚╗╚══╗╚╗║║╔╗╔╝║║╚═╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOO╔═╗╔╗║║║╔╗╔╗╚╗╚╗╚╗O╔╝╚══╝║O╚╗╚╗OOOOOO╔╝╚═╗╚══╗║║║╔╗╔╗║║║╔╝O╔╗║╔╝║╚╝║╚╗║║╔═╝OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOO╚╗║║║║║║║╚╝╚═╝O║╔╝╔╝╔════╝OO╚╗║OOO╔╗O╚═╗╔╝╔══╝╚╝║║╚╝║║╚╝╚═╗║║║║╔╝╔═╝╔╝╚╝╚╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOO╔═╝╚╝╚╝║║╚═══╗╔═╝║╔╝╔╝╔╗O╔╗OO╔╝╚╗╔╗║╚═╗O║╚╗║╔══╗╔╝╚═╗║║╔═══╝║╚╝╚╝╔╝╔╗╚╗╔╗╔╝OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO╔╝╔═══╗╔╝║╔╗╔═╝╚═╗║╚╗║O║║O║║╔╗║╔═╝║║╚═╗╚╗╚╗║╚╝O╔╝║╔╗╔╝╚╝╚╗O╔╗╚╗╔══╝O║║╔╝║╚╝OOOO╔╗╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO╚═╝╔══╝╚╗║║║║╔═╗╔╝║╔╝╚╗║║╔╝║║╚╝║╔╗║║OO╚╗║╔╝╚╗╔╗╚╗╚╝╚╝╔╗╔╗║╔╝╚╗║║╔╗O╔╝║╚╗╚╗OO╔═╗║║║║OOOOOOO╔══╗OOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO╔╗╔╝╔╗╔╗║║║╚╝╚╗║║╔╝╚╗╔╝║║║╔╝╚═╗║║║║╚╗╔═╝║╚═╗║║╚╗╚═╗╔═╝║║╚╝╚═╗║║║║║╔╝╔╝╔╝╔╝╔╗║╔╝║║║╚╗OOOOOO╚╗╔╝OOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOO╔╗║║╚═╝╚╝║║║╚═╗╔╝║║╚╗╔╝╚═╝║║╚╗╔╗║║║╚╝╔╝╚═╗╚══╝╚╝╔╝╔═╝╚═╗║╚═╗╔╗║╚╝╚╝║╚╗╚╗║╔╝O║║║╚╗║║║╔╝╔╗OOO╔═╝║╔╗OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO╔╝╚╝║O╔╗O╔╝╚╝╔═╝║╔╝╚╗║╚═══╗║║╔╝║╚╝╚╝╔═╝O╔═╝╔╗╔╗╔╗╚╗╚╗╔══╝╚══╝║╚╝╔╗╔╗╚╗║╔╝║╚═╗║║║╔╝║║║╚═╝║╔╗O╚═╗║║╚╗╔═╗╔╗OOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO╚══╗╚═╝╚═╝╔═╗║╔╗║║O╔╝╚═╗╔╗║║║║O╚╗╔══╝O╔╗╚═╗║║║╚╝║╔╝╔╝╚══╗╔══╗╚══╝╚╝╚╗║║╚═╝╔╗╚╝╚╝╚╗║╚╝╔╗╔╝║║O╔╗║╚╝╔╝╚╗╚╝╚╗OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOO╔╗OO╔╗O╔╗╚═════╗╚╗║║║╚╝╚╗╚═╗╔╝║║║║║║╔═╝╚╗╔══╝╚╗O╚╝╚╝╔═╝╚═╝╔╗╔═╝║╔═╝╔═╗╔══╗║║║╔══╝║╔╗╔══╝╚╗╔╝╚╝╔╝╚╗║║╚╗╔╝╔╗╚╗╔═╝OOOOOOOOOOOOOOOO
OOOOOOOOOOOOO╔╝╚╗╔╝║╔╝╚╗╔═══╗╚═╝║║╚══╗╚═╗║╚╗║╚╝╚╝╚╝╔╗╔╝║╔═══╝╔══╗O╚════╗║╚╝O╔╝╚╗O╚╗║║╔╗╚╝╚╝╚══╗║║╚╝╔╗╔╗║║╔╗O╚═╗║║║╔╝║╔╝╚═╝╚═══╗OOOOOOOOOOOOOO
OOOOOOOOOOOOO╚╗╔╝║╔╝╚═╗╚╝╔═╗╚═══╝╚╗╔═╝╔═╝╚╗║╚═╗╔═══╝╚╝╔╝╚═══╗║╔╗╚╗╔╗╔╗╔╝╚═╗╔╝╔═╝OO║║╚╝╚══╗╔═══╝╚╝O╔╝╚╝╚╝╚╝╚╗╔╗║║║║╚╗╚╝╔══╗╔╗╔╗║OOOOOOOOOOOOOO
OOOOOOOOOOOO╔═╝╚═╝╚╗╔╗╚═╗╚╗╚═════╗║╚╗╔╝O╔╗║║╔═╝╚══╗O╔╗╚╗╔═══╝╚╝╚╗║║╚╝║╚═╗╔╝╚╗╚══╗╔╝║O╔╗O╔╝╚╗╔╗╔╗╔╗╚╗╔═╗╔═══╝║╚╝╚╝║O╚═╗╚═╗╚╝╚╝╚╝OOOOOOOOOOOOOO
OOOOOOOOOOOO╚═════╗║║║╔╗╚═╝╔═════╝║╔╝╚═╗║╚╝║╚═╗╔══╝╔╝╚╗║╚╗╔╗╔═╗O║║╚═╗║╔╗║║╔╗║╔══╝╚╗║╔╝╚╗╚╗╔╝║╚╝║║║╔╝╚╗╚╝╔═╗O╚═╗╔═╝╔╗╔╝╔╗╚╗╔═══╗OOOOOOOOOOOOOO
OOOOOOOOOOO╔╗╔════╝║║║║╚══╗║╔╗╔══╗║╚╗╔═╝╚╗╔╝╔╗║║O╔╗║╔═╝║╔╝║║║╔╝╔╝║╔═╝╚╝╚╝╚╝║║║╔╗O╔╝║╚═╗╚═╝╚╗╚╗╔╝║╚╝╔╗║╔╗╚╗╚╗╔╗║╚╗╔╝║║╔╝╚╗║║╔══╝OOOOOOOOOOOOOO
OOOOOOOOOO╔╝║╚╗╔══╗╚╝║╚═╗╔╝╚╝╚╝╔═╝║╔╝╚═╗O║╚╗║║║╚═╝╚╝╚╗╔╝╚╗║║║║╔╝╔╝╚═════╗╔╗║║╚╝╚╗╚╗║╔╗╚═══╗╚╗║║╔╝╔╗║╚╝║╚╗║╔╝║║║╔╝╚╗║║╚╗╔╝╚╝╚══╗OOOOOOOOOOOOOO
OOOOOOOOOO╚╗╚╗╚╝╔═╝╔╗╚═╗║║╔╗╔╗O╚═╗║╚══╗╚═╝╔╝║║║╔══╗╔═╝╚═╗║║║║║║╔╝O╔╗O╔╗O║║╚╝╚═╗╔╝╔╝║║╚╗╔══╝╔╝║║║╔╝╚╝╔╗╚╗║║║╔╝║║║╔╗║║║╔╝╚══════╝╔╗OOOOOOOOOOOO
OOOOOOOOOOO╚╗║╔╗╚══╝╚═╗╚╝║║║║╚═╗╔╝╚╗╔╗╚══╗║O║║║╚╗O║║╔╗╔╗║║║╚╝╚╝╚╗╔╝║╔╝║╔╝╚╗╔╗╔╝║╔╝╔╝╚╗║╚══╗╚═╝║║║╔╗O║║╔╝╚╝║║╔╝║║║╚╝╚╝╚╗O╔═╗O╔╗O║╚═╗OOOOOOOOOO
OOOOOOOOOOO╔╝╚╝║O╔╗O╔╗╚═╗║║║╚═╗║║╔═╝║║╔══╝╚╗║║╚╗╚╗╚╝║║║║║║║╔════╝╚╗║╚╗║╚═╗║║║╚╗║╚╗║╔╗║║╔╗O║╔══╝║╚╝╚╗║║║╔══╝║╚═╝╚╝╔═╗╔╗╚╗╚╗║╔╝╚╗║╔═╝OOOOOOOOOO
OOOOOOOOOOO╚══╗╚═╝╚═╝╚╗╔╝║║║╔═╝╚╝╚╗╔╝║║╔═╗╔╝║║╔╝╔╝╔╗║╚╝║║║║║╔╗O╔╗╔╝╚╗║║╔═╝║║║O║║╔╝╚╝╚╝╚╝╚╗║║O╔╗║╔══╝║║║║O╔╗╚╗╔═╗╔╝O╚╝╚╗╚═╝╚╝╔╗╚╝╚═╗OOOOOOOOOO
OOOOOOOOOOOO╔╗╚══════╗║║╔╝║║╚════╗║║╔╝╚╝╔╝╚╗║║╚╗║╔╝║╚═╗║║╚╝║║╚╗║║╚═╗╚╝║╚╗╔╝║║╔╝║╚═══╗╔╗╔═╝║╚╗║║║║╔╗O║║║║╔╝╚╗║╚╗╚╝╔╗╔═╗╚╗╔╗╔═╝╚═╗╔═╝OOOOOOOOOO
OOOOOOOOOOO╔╝╚════╗O╔╝╚╝╚═╝║╔╗O╔═╝╚╝║╔═╗╚╗╔╝║╚═╝║║╔╝O╔╝╚╝╔═╝║╔╝║╚╗O╚═╗║╔╝╚╗║╚╝╔╝O╔═╗╚╝║╚╗O╚╗║║╚╝║║║╔╝╚╝║╚╗╔╝║╔╝╔═╝║║╔╝O║║║╚═══╗║║OOOOOOOOOOOO
OOOOOOOOO╔═╝╔╗╔══╗╚═╝╔════╗║║╚╗╚═╗╔═╝║╔╝╔╝╚╗╚══╗╚╝║╔╗╚══╗╚╗╔╝╚═╝╔╝╔╗╔╝║║╔═╝║╔╗║╔╗║╔╝╔╗╚╗╚═╗║║╚╗╔╝║║║╔══╝╔╝║╔╝╚═╝╔╗╚╝╚═╗╚╝╚╗╔══╝╚╝OOOOOOOOOOOO
OOOOOOOOO╚══╝╚╝╔═╝╔╗╔╝╔═══╝║╚╗║╔═╝║╔╗║║╔╝╔═╝O╔╗║╔═╝║║O╔╗║╔╝║╔═══╝╔╝║╚╗║║║╔╗║║╚╝║║║║╔╝╚═╝╔═╝║║╔╝╚╗║╚╝║╔═╗║╔╝║╔═══╝║╔╗╔╗║O╔╗╚╝╔╗╔╗OOOOOOOOOOOOO
OOOOOOOOOOO╔╗╔╗╚═╗║╚╝╔╝╔╗╔╗╚═╝╚╝╔╗║║║║║╚╗╚═╗╔╝║║║╔╗║║╔╝║║╚╗║╚╗╔═╗╚╗╚╗║║║║║║║╚╗╔╝╚╝║╚═══╗║╔╗║╚╝╔═╝╚═╗║║╔╝║╚═╝╚═╗╔╗╚╝║║║╚╗║╚═╗║║║╚╗OOOO╔╗OOOOOO
OOOOOOOOOOO║║║║╔╗╚╝╔╗╚╗║╚╝╚═════╝║║║║║║O║╔═╝╚╗║║║║║║║╚╗║║╔╝║╔╝║╔╝O╚╗║║║║║║║╚╗║╚═╗╔╝╔╗╔╗║║║║╚╗╔╝O╔╗O║║║║O║╔════╝║║╔╗╚╝╚═╝║╔═╝║║║╔╝╔╗OO║║OOOOOO
OOOOOOOOO╔╗║║║║║╚╗╔╝╚═╝║╔════╗╔╗╔╝╚╝║║║╔╝║╔╗╔╝║║║║║║╚╗║║║║╔╝╚╗║╚╗╔╗║║║║║║║║╔╝╚╗╔╝║╔╝╚╝║║║║╚╗║╚╗╔╝╚╗║║║╚╗║╚╗╔═══╝╚╝╚═╗╔══╝╚╗O║║║╚╗║║╔═╝╚╗OOOOO
OOOOOOOOO║╚╝╚╝║║╔╝╚══╗╔╝║╔╗╔╗╚╝╚╝╔═╗╚╝╚╝O╚╝║╚╗║║║║║╚╗║║╚╝║╚╗╔╝║╔╝║╚╝║║║║║║╚╝O╔╝╚╗╚╝╔╗O║║║║╔╝║╔╝╚╗╔╝║║╚╗║║╔╝║╔══════╗║╚═╗╔╗╚═╝╚╝╔╝║╚╝╔╗╔╝OOOOO
OOOOOOOO╔╝╔══╗╚╝║╔╗O╔╝╚╗╚╝╚╝╚╗╔╗╔╝O╚════╗╔═╝╔╝║║║║║╔╝║║╔═╝╔╝╚═╝╚╗╚═╗║║║║╚╝╔══╝╔╗╚══╝╚╗╚╝║║║╔╝║╔╗║╚╗║╚═╝╚╝╚═╝╚═╗╔╗╔╗╚╝╔╗╚╝║╔════╝O║╔═╝╚╝OOOOOO
OOOOOOOO╚╗║╔╗╚═╗╚╝╚═╝╔═╝O╔╗╔╗╚╝╚╝╔╗╔╗╔══╝╚══╝╔╝║╚╝║╚╗║║║╔╗╚═╗╔══╝╔╗║║║╚╝╔═╝╔═╗║╚╗╔═══╝O╔╝║║╚╗╚╝║╚╗║║╔═══╗╔═╗╔═╝║╚╝╚═╗║║╔╗║║╔╗╔╗╔╗║║O╔═╗OOOOOO
OOOOOOOO╔╝║║╚══╝╔╗╔══╝O╔╗║╚╝╚════╝╚╝╚╝╔╗╔╗╔═╗╚╗╚═╗╚╗║║║║║║╔╗║╚╗╔╗║╚╝║║╔═╝╔╗║╔╝║╔╝║╔╗O╔═╝╔╝║╔╝╔═╝╔╝║║╚╗╔╗║║O╚╝╔╗║╔═══╝║║║╚╝╚╝╚╝╚╝╚╝╚╗║╔╝OOOOOO
OOOOOOOO╚═╝╚═╗╔╗║╚╝O╔══╝╚╝╔╗╔══════╗╔═╝╚╝╚╝╔╝╔╝╔╗╚╗╚╝╚╝║║║║║║O║║║╚═╗╚╝║╔═╝║║║╔╝╚╗║║╚╗║╔╗╚╗║╚╗╚╗╔╝╔╝╚╗╚╝║╚╝╔══╝╚╝╚══╗╔╝╚╝╔╗╔╗╔══════╝║╚═╗OOOOO
OOOOOOOOOOO╔═╝║║║╔═╗╚═══╗╔╝╚╝╔═════╝║╔═══╗╔╝O╚╗║╚╗╚══╗O║║╚╝╚╝╔╝║╚╗╔╝╔╗║║╔═╝║║║╔═╝╚╝╔╝║║╚╗║║╔╝O║╚╗║╔═╝╔═╝╔╗║╔═══════╝╚══╗║╚╝║╚═══════╝╔═╝OOOOO
OOOOOOOOOOO╚══╝╚╝╚╗╚════╝║╔╗╔╝╔═════╝║╔═╗║║╔╗O║╚╗║╔══╝╔╝╚╗╔══╝╔╝O║╚═╝║╚╝╚╗╔╝║║╚═╗╔═╝O║║╔╝║║║╔═╝╔╝╚╝╔╗╚══╝╚╝╚═══════╗╔╗╔╝╚═╗╚═╗╔══╗╔╗╔╝OOOOOOO
OOOOOOOOOO╔╗╔╗OO╔═╝╔═╗╔═╗║║╚╝╔╝╔════╗║║╔╝║╚╝║╔╝╔╝║╚══╗╚═╗║╚╗╔╗║╔═╝╔═╗╚╗╔═╝╚╗║║╔═╝╚══╗║║║╔╝║║║╔╗║╔╗╔╝╚════════╗╔═╗╔╗╚╝╚╝╔╗╔╝O╔╝╚═╗║║║╚══╗OOOOO
OOOOOOOOOO║╚╝╚╗╔╝╔╗║O╚╝O╚╝╚═╗╚╗║╔╗╔╗╚╝║║O╚══╝╚╗╚╗╚╗╔╗╚╗╔╝╚╗║║║║║╔═╝O╚═╝╚═╗╔╝╚╝║╔══╗╔╝╚╝╚╝O╚╝║║║║║║╚═╗╔═════╗O╚╝O╚╝╚═══╗║║╚═╗║╔╗╔╝║║║╔══╝OOOOO
OOOOOOOOOO╚══╗║╚═╝║║╔╗╔╗╔═╗O╚═╝║║║║╚══╝╚═════╗║╔╝O╚╝╚╗║╚═╗║║║║║║╚══╗╔════╝╚╗╔═╝║O╔╝╚═══════╗║║║║║╚╗╔╝║O╔══╗║╔╗╔╗╔═╗O╔╗╚╝╚╗╔╝╚╝╚╝O╚╝║╚╗OOOOOOO
OOOOOOOOOO╔══╝╚═══╝║║║║║╚╗╚═╗╔╗╚╝╚╝╔╗╔╗╔╗╔══╗║╚╝╔╗O╔╗║║╔═╝║║║║║║╔══╝║╔╗╔═╗╔╝╚╗╔╝╔╝╔═╗╔═╗╔╗╔╝║║║║╚╗╚╝╔╝╔╝╔╗╚╝║║║╚╝╔╝╔╝╚╗╔╗╚╝╔╗╔════╗╚═╝OOOOOOO
OOOOOOOOOO║╔╗╔═╗╔═╗║║║║║O╚═╗╚╝╚╗╔╗╔╝╚╝╚╝╚╝O╔╝╚══╝╚═╝║╚╝║╔╗║║║║║║╚══╗╚╝╚╝╔╝╚╗O╚╝O╚╗╚╗║║╔╝║║╚╗╚╝╚╝O╚╗╔╝O╚═╝╚══╝╚╝╔╗╚═╝╔╗╚╝╚══╝╚╝╔╗╔╗║OOOOOOOOOO
OOOOOOOOOO╚╝╚╝O╚╝O╚╝║║║║╔╗O╚═╗╔╝║║╚══╗╔═══╗╚═╗╔═╗╔╗╔╝╔═╝║╚╝║║╚╝║╔══╝╔═══╝╔╗║╔════╝╔╝║║╚╗║╚═╝O╔╗╔══╝║╔═════╗╔╗╔╗║╚══╗║╚══╗╔══╗╔╝╚╝║╚╗OOOOOOOOO
OOOOOOOOOO╔═════╗╔═╗║║║╚╝║╔╗╔╝╚═╝╚═══╝║╔══╝╔╗║╚╗╚╝╚╝╔╝╔╗║╔╗║╚╗O║╚══╗╚═══╗║╚╝╚╗╔╗╔╗╚╗╚╝╔╝╚╗╔═╗║║╚═══╝╚════╗╚╝║║║╚══╗║║O╔╗╚╝╔╗║╚══╗║╔╝OOOOOOOOO
OOOOOOOOO╔╝╔╗╔═╗║╚╗╚╝║╚═╗║║║╚═════════╝╚═╗O║║╚═╝╔═╗╔╝╔╝║║║╚╝╔╝╔╝╔╗╔╝╔═══╝║O╔═╝║║║╚╗╚═╗╚══╝╚╗╚╝║╔═════════╝╔╗╚╝║╔══╝║║╔╝║╔╗║║╚══╗║╚╝OOOOOOOOOO
OOOOOOOOO╚═╝║║╔╝╚╗╚═╗╚╗╔╝╚╝╚══════════╗╔╗╚═╝╚═══╝╔╝╚═╝╔╝║║╔╗║O╚╗║║║╔╝╔╗╔╗╚╗║╔╗║╚╝O║╔═╝╔╗╔╗O╚═╗║╚══════╗╔══╝╚═╗║║╔═╗║╚╝╔╝║║║║╔═╗╚╝OOOOOOOOOOOO
OOOOOOOOOOOO╚╝╚╗╔╝╔╗╚╗║╚╗╔╗╔╗╔══╗╔═══╗╚╝║╔╗╔╗╔═══╝╔╗╔╗╚═╝╚╝║╚═╗║║║║║╔╝╚╝╚╗║╚╝╚╝╔══╝╚══╝╚╝║╔══╝╚═══════╝║O╔═══╝╚╝║╔╝║╔╗╚═╝╚╝╚╝╔╝╔╗OOOOOOOOOOOO
OOOOOOOO╔══╗╔╗╔╝╚╗║╚═╝║O║║║║╚╝╔╗╚╝O╔╗╚═╗║║║║╚╝╔╗╔╗║╚╝╚═╗╔╗╔╝╔╗║║║║║╚╝O╔══╝║O╔═╗╚╗╔╗╔╗╔═╗╔╝╚═╗╔╗╔╗╔╗╔╗╔═╝╔╝╔╗╔╗O╔╝╚╗╚╝╚══╗╔══╗╚═╝║OOOOOOOOOOOO
OOOOOOOO╚═╗║║║╚═╗║╚══╗╚═╝║╚╝╔═╝║╔══╝╚══╝║║║╚══╝╚╝╚╝╔═╗╔╝║╚╝╔╝║║║║╚╝O╔═╝╔═╗╚╗╚╗╚═╝║║║╚╝O╚╝O╔╗╚╝╚╝╚╝╚╝╚╝╔╗╚═╝╚╝╚╗╚╗╔╝╔╗O╔╗╚╝╔╗╚═══╝OOOOOOOOOOOO
OOOOOOOO╔═╝║║║╔╗║║O╔═╝╔═╗╚╗O╚═╗║╚══╗╔══╗╚╝╚═══╗╔═╗╔╝O╚╝╔╝╔╗╚╗╚╝║║╔══╝╔╗╚╗║╔╝O╚══╗║║╚╗O╔══╗║╚╗O╔═════╗╔╝╚══╗╔═╗╚═╝╚═╝╚═╝╚╗O║╚═══╗OOOOOOOOOOOOO
OOOOOO╔═╝╔╗╚╝╚╝╚╝╚═╝╔╗║O║╔╝╔╗O║║╔╗O╚╝╔╗╚╗O╔══╗║╚╗╚╝O╔╗O╚╗║║╔╝╔╗╚╝╚╗╔╗║║╔╝║║O╔═══╝║╚╗╚═╝╔═╝╚╗╚╗╚════╗║╚═══╗║╚╗╚═╗╔═════╗╔╝╔╝╔═══╝OOOOOOOOOOOOO
OOOOOO╚╗╔╝║╔═══╗╔╗╔╗║║║╔╝║╔╝╚═╝╚╝╚╗╔═╝╚╗╚╗╚╗╔╝╚═╝O╔╗║╚═╗║║║╚═╝║╔╗O╚╝║║║║╔╝╚╗╚╗╔═╗╚╗╚╗╔═╝╔╗O╚╗║O╔╗╔╗║║╔═══╝╚═╝╔╗║╚════╗║║O╚╗╚═══╗OOOOOOOOOOOOO
OOOOOOO╚╝╔╝║╔══╝║╚╝║║║║╚╗║╚══════╗║╚═╗╔╝╔╝O║╚════╗║╚╝╔═╝║║║╔══╝║║O╔═╝║║║╚╗╔╝O╚╝O╚╗║╔╝║╔═╝╚══╝╚═╝╚╝╚╝║╚══════╗║║╚═════╝║╚══╝╔╗╔═╝╔╗OOOOOOOOOOO
OOOOOOOOO╚═╝╚╗╔╗║╔═╝║║╚╗╚╝O╔╗╔╗╔╗║║╔╗║╚╗║╔╗║╔════╝║╔═╝╔╗╚╝║╚═══╝╚╗╚═╗║║║╔╝║OO╔═══╝║╚╗║║╔═╗╔══╗╔════╗║O╔════╗╚╝╚══╗╔══╗║╔╗╔═╝╚╝╔╗║║╔═╗OOOOOOOO
OOOOOOOOOOOO╔╝║║║╚══╝╚═╝╔╗╔╝╚╝╚╝╚╝╚╝╚╝╔╝╚╝║║╚═╗╔╗╔╝╚══╝╚╗O╚╗╔══╗╔╝╔═╝║║║╚╗║O╔╝╔╗╔╗╚╗╚╝║║O╚╝╔═╝║╔═══╝╚╗╚══╗O╚══╗╔╗╚╝╔═╝╚╝║╚════╝╚╝║║╔╝OOOOOOOO
OOOOOOOOOOOO╚═╝╚╝╔════╗╔╝║╚═══╗╔╗╔═╗╔╗╚══╗╚╝╔═╝║╚╝╔╗╔╗╔═╝╔╗╚╝O╔╝║O╚═╗║╚╝O╚╝O╚═╝║║╚═╝╔╗╚╝╔╗O╚══╝╚════╗║O╔╗╚═══╗║║║╔╗╚═══╗╚══╗╔═╗╔╗╚╝╚╗OOOOOOOO
OOOOOOOOOOOOO╔═╗O╚═══╗║╚╗║╔╗╔═╝║╚╝O╚╝╚══╗║╔╗╚══╝╔═╝║║╚╝O╔╝╚═╗O╚═╝OOO╚╝OOOO╔════╝║╔══╝║╔╗║╚═╗╔══╗╔══╗║╚╗║╚══╗╔╝║║║║║╔═══╝╔═╗╚╝O╚╝╚═══╝OOOOOOOO
OOOOOOOOOOOOO╚╗╚╗╔╗╔╗║║╔╝╚╝╚╝╔╗║╔╗╔═════╝╚╝╚════╝╔╗╚╝╔╗╔╝╔══╝OOOOOOOOOOOOO╚═╗╔╗╔╝╚╗╔╗╚╝╚╝╔═╝╚═╗║╚═╗║╚╗╚╝╔═╗║║╔╝║║║║╚═══╗║╔╝╔╗╔╗╔══╗OOOOOOOOOO
OOOOOOOOOOOOOO╚╗╚╝╚╝╚╝║╚═╗╔══╝╚╝║║╚═════════╗O╔╗O║║╔╗║║║╔╝O╔╗╔══╗OOOOOOOOOOO╚╝║║╔╗╚╝╚═══╗║╔╗╔╗║║O╔╝╚═╝╔╗║╔╝╚╝║╔╝╚╝╚═╗╔═╝║║O║╚╝╚╝╔╗╚╗OOOOOOOOO
OOOOOOOOOOOOOOO╚═════╗║╔═╝║╔╗╔══╝║╔══╗╔═╗╔═╗╚═╝╚╗║╚╝║║╚╝╚╗╔╝╚╝╔═╝OOOOOOOOOOOO╔╝║║╚══════╝╚╝╚╝╚╝╚═╝╔╗╔╗║║║║O╔╗╚╝╔═══╗║║O╔╝╚╗║╔═╗╔╝╚═╝OOOOOOOOO
OOOOOOOOOOO╔══╗╔═════╝║╚══╝║║╚══╗║╚╗O╚╝O║╚╗╚╗╔╗╔╝║╔╗║║╔══╝║╔══╝O╔╗OOOOOOOOOO╔╝╔╝╚════╗╔╗╔═══╗╔╗╔╗╔╝╚╝║║╚╝╚═╝╚╗O║╔╗╔╝║╚═╝╔╗╚╝╚╗║║╔═══╗OOOOOOOO
OOOOOOOOO╔╗╚═╗║╚╗╔═══╗╚╗╔╗╔╝╚╗╔═╝╚╗╚═══╗╚╗╚╗║║║╚═╝║╚╝║╚═╗O║╚════╝╚╗OOOOOOOOO║╔╝O╔════╝║║║╔╗╔╝║║║║║╔══╝║╔═════╝╔╝║╚╝O║╔══╝║╔╗╔╝╚╝╚╗╔═╝OOOOOOOO
OOOOOOO╔═╝╚══╝╚╗╚╝╔═╗╚╗║║║╚╗╔╝╚══╗╚════╝O╚╗║╚╝╚═══╝╔╗║╔╗╚═╝╔╗╔╗╔╗╔╝OOOOOOOOO╚╝OO╚╗╔╗╔╗║║║║╚╝╔╝╚╝╚╝╚═══╝╚════╗╔╝╔╝╔╗╔╝╚══╗╚╝╚╝O╔═╗║║╔╗OOOOOOOO
OOOOOOO╚══╗╔══╗║╔╗╚╗║O║╚╝╚═╝╚╗╔╗O╚═════╗╔╗╚╝╔╗╔══╗O║╚╝║║╔╗╔╝║║╚╝╚╝OOOOOOOOOOOOOOO╚╝╚╝║║║║╚╗╔╝╔╗╔╗╔╗O╔╗╔╗╔═══╝║╔╝╔╝║║╔╗╔╗╚════╗║╔╝║╚╝║OOOOOOOO
OOOOOOOOOO╚╝╔═╝╚╝╚═╝║╔╝╔════╗║║║╔════╗╔╝║╚═╗║║║╔═╝╔╝╔╗║╚╝╚╝╔╝╚══╗OOOOOOOOOOOOOOOOO╔╗O╚╝║║O╚╝╔╝║║║║║╔╝║║║╚════╝╚═╝╔╝╚╝╚╝║╔════╝║╚═╝╔╗║OOOOOOOO
OOOOOOOOOOOO║╔╗╔═══╗║╚╗║╔╗╔═╝╚╝║╚═══╗╚╝O║╔═╝║╚╝╚══╝╔╝║╚══╗O╚═╗╔═╝OOOOOOOOOOOOOO╔══╝╚═══╝║╔╗O╚╗╚╝╚╝║╚╗╚╝╚══╗╔╗╔═╗╔╝╔╗O╔╗╚╝╔═╗╔╗║╔═╗║╚╝OOOOOOOO
OOOOOOO╔╗OOO╚╝╚╝╔══╝╚═╝║║╚╝╔╗╔╗╚════╝O╔╗║║O╔╝╔╗╔═╗╔╝O╚╗╔╗╚═╗╔╝╚╗OOOOOOOOOOOOOOO╚═══════╗║║╚══╝╔╗╔╗╚═╝╔═══╗╚╝╚╝O║╚═╝╚═╝╚═╗║╔╝║║║║O║╚╗OOOOOOOOO
OOOOOOO║║╔╗O╔╗╔═╝╔═╗╔╗╔╝╚═╗║╚╝╚╗╔╗╔═══╝╚╝╚═╝╔╝║╚╗║╚══╗║║╚╗╔╝║╔═╝OOOOOOOOOOOOOOOOOO╔════╝║╚════╝╚╝╚╗╔═╝O╔╗╚═══╗╔╝╔╗╔═════╝║╚═╝╚╝╚╗║╔╝OOOOOOOOO
OOOOOOO║╚╝╚╗║║╚══╝╔╝║║║╔══╝║╔══╝║╚╝╔═══╗╔══╗╚╗║╔╝║╔══╝╚╝O╚╝O╚╝╔╗OOOOOOOOOOOOOOOOOO╚╗╔╗╔═╝╔═════╗╔╗╚╝O╔╗║╚══╗╔╝╚═╝║╚╗╔╗╔╗O╚╗╔╗╔╗╔╝╚╝OOOOOOOOOO
OOOOOOO╚══╗╚╝╚═╗╔╗╚═╝╚╝╚══╗║║╔═╗╚╗╔╝O╔╗╚╝╔╗╚═╝╚╝╔╝╚══════╗OO╔═╝║OOOOOOOOOOOOOOOOOOO╚╝╚╝╔═╝╔═╗╔╗╚╝╚═══╝╚╝╔═╗║╚╗O╔╗╚═╝║║║║╔═╝║║║║╚═╗╔════╗OOOOO
OOOOOOOOOO║╔╗╔╗╚╝╚════════╝║║╚╗║╔╝╚══╝╚═╗║╚═╗╔╗O╚═╗╔╗╔═══╝OO╚═╗╚╗OOOOOOOOOOOOOOOO╔════╗╚══╝╔╝║╚╗╔═══════╝╔╝╚═╝╔╝╚═╗O║╚╝╚╝╔═╝╚╝╚══╝╚═══╗║OOOOO
OOOOOOOOOO╚╝╚╝╚═══════════╗║║╔╝╚╝╔╗╔╗╔══╝║╔═╝║╚══╗╚╝║╚════╗O╔╗║╔╝╔═══╗OOOOOOOOOOO╚═══╗║╔╗╔╗╚╗║O╚╝╔═══╗╔╗╔╝╔╗╔╗║╔══╝╔╝╔══╗╚══╗╔════╗╔╗╔╝║OOOOO
OOOOOOOOOOO╔══════════════╝║║╚╗╔═╝╚╝║║╔═╗║║╔═╝╔══╝╔╗║╔═╗╔═╝╔╝║║╚╗║╔══╝OOOOOOOOOOO╔══╗║║║║║║O╚╝╔╗╔╝╔═╗║║║╚═╝║║║║╚╗╔╗║╔╝╔╗╚═══╝║╔═╗╔╝║║╚╗║╔╗OOO
OOOOOOOOOOO╚════╗╔═╗╔╗╔╗╔═╗║╚═╝╚═══╗║╚╝╔╝║║║╔═╝O╔╗║║╚╝O╚╝╔═╝╔╝╚╗║║║╔═╗O╔╗OOOO╔═╗O╚═╗║║║║║║║╔══╝║╚═╝╔╝╚╝╚═══╝║║║╔╝║║║╚╗║║╔════╝╚╗║║O║║O║╚╝╚╗OO
OOOOOOOOOOOOO╔═╗╚╝O╚╝║║╚╝O╚╝O╔═╗╔══╝╚═╗╚═╝╚╝╚╗O╔╝╚╝╚═══╗O╚═╗╚╗╔╝║║╚╝╔╝╔╝║OOOO║╔╝╔╗╔╝╚╝╚╝║║║╚══╗║╔══╝╔═╗╔════╝╚╝╚═╝╚╝╔╝║╚╝╔═════╝╚╝╔╝║╔╝╔══╝OO
OOOOOOOOOOO╔╗╚╗║O╔╗╔╗║║╔══╗╔╗╚╗║╚╗╔══╗╚══╗╔═╗╚╗║╔══╗╔══╝╔╗╔╝╔╝╚╗║║╔═╝╔╝╔╝OOO╔╝║╔╝╚╝╔═══╗╚╝╚╗╔═╝╚╝╔═╗║╔╝║O╔╗╔╗╔╗╔╗╔═╗╚═╝╔╗╚══╗O╔═╗O║╔╝╚╗║╔╗OOO
OOOOOOOOOOO║║╔╝║╔╝╚╝║╚╝║╔═╝║║╔╝║O╚╝╔═╝╔═╗║║O╚╗╚╝╚═╗║╚══╗║║╚╗║╔═╝║║╚═╗╚╗╚╗O╔╗╚╗║╚═══╝╔═╗╚══╗║╚═╗╔╗╚╗║║║╔╝╔╝║║║║╚╝║╚╗╚╗╔╗║║╔═╗╚╗║╔╝╔╝╚══╝╚╝╚╗OO
OOOOOOOOOO╔╝║╚╗║║╔═╗╚══╝╚══╝║╚╗║╔══╝╔╗║╔╝╚╝╔╗╚════╝║╔═╗╚╝║╔╝║╚═╗║║╔═╝╔╝╔╝O║╚╗║║O╔╗╔═╝╔╝╔══╝║╔═╝║╚═╝╚╝║║O╚╗╚╝║╚═╗╚═╝╔╝║║║║╚╗╚╗╚╝╚═╝╔═╗╔╗╔╗╔╝OO
OOOOOOOOOO╚╗╚═╝╚╝║╔╝╔╗╔╗╔╗╔╗╚═╝║╚═══╝╚╝╚╗╔╗║╚══╗╔═╗║╚╗╚══╝╚╗╚╗╔╝╚╝╚═╗╚╗║╔╗╚╗║║║╔╝║╚═╗║O╚══╗║╚══╝╔══╗╔╝║╔╗╚═╗╚══╝╔╗O╚╗║╚╝╚═╝╔╝╔══╗╔╝╔╝║║║║║OOO
OOOOOOOOOOO╚╗╔╗╔╗║╚╗║╚╝╚╝╚╝╚══╗║╔╗O╔╗╔═╗╚╝╚╝╔══╝║╔╝╚═╝O╔═╗O╚╗║║╔═══╗╚╗║║║╚╗║║║╚╝╔╝O╔╝║╔═══╝╚═══╗╚═╗║╚═╝║╚═╗╚══╗╔╝║╔╗║╚════╗╚╗╚╗╔╝╚╗╚═╝╚╝╚╝OOO
OOOOOOOOOOOO║║╚╝╚╝╔╝║╔════════╝╚╝╚═╝╚╝O╚╗╔══╝╔══╝╚════╗║╔╝╔╗║║║╚═╗O╚═╝║║║╔╝║║╚═╗╚╗╔╝╔╝╚══S═══╗╔╝╔╗║║╔══╝╔╗╚══╗╚╝╔╝║║╚╗╔═══╝O╚╗║║╔╗╚╗O╔═══╗OOO
OOOOOOOOOOO╔╝║╔══╗╚═╝╚══╗╔═════╗╔══════╗║╚═══╝╔═╗╔════╝║║╔╝╚╝╚╝╔═╝╔╗╔═╝║║║O║║╔╗╚╗║║╔╝╔═════╗O║║╔╝╚╝║╚═══╝╚══╗╚═╗╚═╝╚╗║╚═════╗║║║║╚╗╚═╝╔═╗╚═╗O
OOOOOOOOOOO╚╗║╚═╗╚══════╝║╔════╝║╔═════╝║╔╗╔═╗╚╗║║╔╗╔═╗║║║╔══╗╔╝O╔╝║╚═╗║║╚╗║║║║╔╝║║║O║╔╗╔═╗║╔╝║╚══╗╚╗╔══════╝O╔╝╔╗╔═╝║╔═══╗╔╝║║║╚╗║╔╗╔╝O╚═╗║O
OOOOOOOOOOOO║║╔╗╚═══╗╔╗╔╗║║╔╗╔═╗║╚══╗╔═╗║║╚╝O║╔╝║╚╝║╚╗║║║╚╝╔═╝║╔╗╚╗║╔╗║╚╝╔╝║║║║╚╗╚╝╚╗╚╝╚╝O║║╚╗╚═╗O║╔╝╚═══════╗╚╗║║╚═╗║╚╗╔╗╚╝O║║╚═╝╚╝║║OOOO╚╝O
OOOOOOOOOOOO╚╝║║╔╗╔═╝║║║║║║║║║╔╝║╔══╝║╔╝╚╝╔═╗╚╝╔╝╔╗╚╗║║║║╔╗╚═╗╚╝╚╗║║║║║╔═╝╔╝║║╚╗╚╗╔╗╚╗O╔╗╔╝╚═╝╔╗╚═╝║╔╗╔═══╗╔╗║╔╝║║╔╗║╚╗╚╝╚╗OO╚╝O╔═══╝╚═╗OOOOO
OOOOOOOOOOO╔╗O║╚╝╚╝╔╗║╚╝╚╝╚╝╚╝╚╗║╚═══╝╚╗╔╗╚╗║╔╗╚═╝╚═╝║║║╚╝║╔═╝╔╗╔╝║║║╚╝╚══╝╔╝╚╗╚═╝║╚═╝╔╝╚╝╔╗╔═╝╚══╗╚╝╚╝╔═╗╚╝╚╝╚╗║╚╝║║╔╝╔═╗╚╗╔═╗O║╔══╗╔═╝OOOOO
OOOOOOOOOOO║╚╗╚╗╔╗╔╝║║╔══╗╔═╗╔╗╚╝╔╗╔══╗╚╝╚═╝║║║╔╗╔╗╔═╝║╚═╗║╚╗╔╝║║O║║╚╗╔════╝╔╗╚═╗╔╝O╔╗╚═╗╔╝║║O╔═══╝╔╗╔╗║╔╝╔╗╔═╗║╚╗O╚╝╚═╝O╚═╝║╔╝O╚╝╔═╝╚╗OOOOOO
OOOOOOOOOOO╚╗╚═╝║║╚╗║║╚═╗║╚╗╚╝╚══╝╚╝╔╗╚═╗╔═╗║║╚╝║║║║╔═╝╔╗║║╔╝║O╚╝╔╝╚═╝╚═══╗╔╝╚══╝╚╗╔╝╚══╝╚╗╚╝╔╝╔╗╔╗║║║╚╝╚═╝╚╝╔╝╚╗╚═════════╗║║OOOO║╔═╗║OOOOOO
OOOOOOOOOOOO╚═══╝║╔╝╚╝╔═╝╚╗╚═════╗╔═╝╚═╗╚╝O╚╝║╔╗╚╝║║║╔═╝╚╝║║╔╝╔╗O╚═╗╔═════╝╚╗╔═╗╔═╝╚══════╝╔═╝╔╝║║║║║║╔══════╝╔╗║╔╗╔═╗╔════╝║║O╔╗O╚╝O╚╝OOOOOO
OOOOOOOOOOOOO╔═══╝╚╗╔═╝╔╗╔╝╔╗O╔╗O╚╝╔═══╝╔╗O╔╗╚╝╚═╗║║║╚═══╗║║╚╗║║╔═╗║║╔═════╗╚╝╔╝╚╗╔═╗O╔╗O╔╗╚═╗╚╗║║╚╝║║╚╗╔═════╝║║║╚╝O║╚═╗╔╗O║║╔╝╚═╗OOOOOOOOOO
OOOOOOOOOOOOO╚═╗╔══╝╚══╝║║O║║╔╝╚═╗╔╝O╔══╝╚╗║╚╗╔══╝╚╝╚╗╔══╝║║╔╝║║╚╗╚╝╚╝╔════╝╔═╝╔═╝║╔╝╔╝╚═╝║╔╗║╔╝║║╔═╝╚╗╚╝╔═════╝║╚══╗╚═╗╚╝╚═╝╚╝╔══╝OOOOOOOOOO
OOOOOOOOOOOOOOO╚╝O╔╗╔╗╔═╝╚═╝║╚══╗║╚══╝╔╗╔╗╚╝╔╝╚═══╗╔═╝╚══╗╚╝╚╗║║O╚══╗╔╝O╔╗╔╗╚═╗║╔╗║╚╗╚═╗╔╗╚╝║╚╝O║║╚═══╝╔╗╚═════╗║╔═╗╚╗╔╝╔╗╔═══╗╚═══╗OOOOOOOOO
OOOOOOOOOOOOOO╔═══╝╚╝╚╝╔╗╔═╗╚═══╝╚════╝╚╝╚══╝╔═╗╔═╝║╔╗O╔╗║╔══╝║╚╗╔═╗║╚══╝║║╚╗╔╝╚╝╚╝╔╝╔╗╚╝╚═╗║╔═╗╚╝╔╗O╔═╝║╔╗╔═╗╔╝╚╝O╚═╝╚╗║║╚══╗║╔═══╝OOOOOOOOO
OOOOOOOOOOOOOO╚═══╗╔╗╔═╝╚╝O╚═══════╗╔╗╔╗O╔═╗O║╔╝╚═╗║║║╔╝║║╚╗╔╗║╔╝╚╗╚╝╔═══╝╚╗╚╝╔═╗╔═╝╔╝╚╗╔╗╔╝║╚╗╚╗╔╝╚╗║╔╗╚╝║╚╗╚╝╔╗O╔╗╔═╗║║╚╗╔═╝╚╝OO╔╗OOOOOOOOO
OOOOOOOOOOOOO╔╗O╔╗╚╝╚╝O╔════════╗╔═╝║║║╚╗╚╗║╔╝╚╗╔═╝║║║╚╗║║╔╝║║║╚╗╔╝╔╗║O╔╗O╔╝╔═╝O╚╝O╔╝╔═╝║║╚╗╚╗║╔╝║╔═╝╚╝╚═╗╚═╝O╔╝╚╗║║║╔╝╚╝O╚╝╔═════╝║OOOOOOOOO
OOOOOOOOOOOO╔╝╚═╝╚═════╝╔═╗╔═══╗║╚══╝║║╔╝╔╝╚╝╔═╝╚═╗║║╚╗║╚╝╚╗║║║╔╝╚═╝║║╔╝╚╗║╔╝╔═╗O╔╗╚╗╚╗O║║O╚╗║║╚╗║║╔═╗O╔╗╚═══╗╚╗╔╝║║║╚═╗O╔╗O║╔═╗╔══╝OOOOOOOOO
OOOOOOOOOOOO║╔════╗╔╗╔═╗║╔╝║╔══╝║╔╗╔═╝║╚╗╚═╗╔╝╔╗╔╗║║║╔╝╚══╗║║║║║╔╗O╔╝╚╝╔═╝║║O║╔╝╔╝╚╗║╔╝╔╝╚╗╔╝║║╔╝║║╚╗╚═╝╚════╝╔╝║O║╚╝╔═╝╔╝╚═╝╚╗║║OOOOOOOOOOOO
OOOOOOOOOOOO╚╝╔═══╝║╚╝╔╝║╚╗║╚╗╔╗╚╝╚╝╔═╝╔╝O╔╝╚╗║║║╚╝║║║╔╗╔═╝║║║║╚╝║╔╝╔══╝╔═╝╚╗║╚╗║╔╗║║╚╗╚╗╔╝╚╗║║║╔╝╚╗╚════╗╔╗╔╗╚╗╚═╝╔═╝╔═╝╔════╝╚╝OOOOOOOOOOOO
OOOOOOOOOOOOO╔╝╔═╗╔╝╔═╝╔╝╔╝║╔╝║╚╗╔═╗╚╗╔╝╔╗╚═╗║║║║╔═╝║║║║╚═╗║║║║╔═╝╚╗║O╔╗╚═╗╔╝║╔╝╚╝║║║╔╝O║║╔╗║║║║║╔═╝O╔╗╔╗╚╝╚╝╚╗╚╗╔═╝╔╗║╔═╝╔════╗OOOOOOOOOOOOO
OOOOOOOOOOOOO╚═╝╔╝║O╚═╗║╔╝╔╝╚╗║╔╝╚╗╚╗║╚╗║║╔╗║║║║║║╔╗║║║╚╗╔╝║║║║║╔═╗║╚╗║╚╗╔╝║╔╝╚╗╔╗║║║╚═╗║║║║║║║║║║╔═╗║╚╝║╔════╝╔╝╚═╗║║║╚══╝╔══╗╚══╗OOOOOOOOOO
OOOOOOOOOOOOOOOO╚╗╚╗O╔╝║╚╗║╔╗╚╝╚╗╔╝╔╝║O║║║║║║║║║║║║║║║╚╗║║O╚╝║║╚╝╔╝╚╗╚╝╔╝╚╗║║╔╗║║║║║╚╗╔╝║║║╚╝╚╝║║╚╝╔╝╚╗╔╝╚═════╝╔═╗╚╝╚╝╔╗╔╗╚═╗║╔══╝OOOOOOOOOO
OOOOOOOOOOOOOOO╔═╝╔╝O╚═╝O╚╝║╚═══╝╚╗╚╗║╔╝║╚╝║║║║╚╝╚╝║║║╔╝║╚═╗O║╚═╗╚══╝O╔╝╔═╝║╚╝║╚╝║║╚╗║║╔╝║║╔═══╝╚═╗╚╗╔╝║╔╗╔╗╔═╗╔╝╔╝╔═══╝║║║╔═╝╚╝╔╗OOOOOOOOOOO
OOOOOOOOOOOOOOO╚═╗║OOO╔════╝╔══╗╔╗║╔╝║╚╗║╔═╝║╚╝╔═══╝║║║╔╝╔╗╚╗╚═╗║╔════╝╔╝╔═╝╔═╝╔╗║║O╚╝║╚╗║║║╔╗╔══╗╚╗║║╔╝║║║║╚╗║║O╚╗╚═══╗╚╝║╚═╗O╔╝║OOOOOOOOOOO
OOOOOOOOOOOOOOOOO╚╝OOO╚═╗╔═╗║╔═╝║╚╝╚╗║╔╝║║╔╗╚═╗╚═╗╔╗║║║╚╗║╚╗╚═╗║║║╔═══╗║O║╔╗║O╔╝╚╝║╔═╗╚╗║╚╝║║║║╔═╝╔╝╚╝╚╗║║║║╔╝║╚═╗║╔╗╔╗╚═╗╚═╗╚═╝╔╝OOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO╔╗║║O╚╝╚╗╔╝O╔╗╚╝╚╗║╚╝╚╗╔╝╔═╝║║║║║O║║╔╝╔╗║╚╝╚╝╔══╝╚╗╚╝║╚╗╚══╗╚╝╔╝O╚╝╔═╝║╚╝╚═╗║O╔╗O║║║║║║╔╝╔╗║║║║║╚╗╔╝╔╗╚╗╔╗║OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO╔═╝╚╝╚╗╔╗O╚╝╔═╝╚═══╝╚══╗║║O╚═╗║║║╚╝╔╝║║╔╝║║O╔═╗╚══╗╔╝╔═╝╔╝╔══╝╔╗╚═══╗║╔╗║╔═╗╔╝╚═╝╚╗╚╝║║╚╝║╔╝║║║║╚╝╔╝╚╗║║O╚╝╚╝OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO╚═════╝║╚═══╝╔╗╔╗╔╗╔╗╔╗║║╚╗╔═╝║╚╝╔╗╚╗║║╚╗║╚╗╚╗║╔╗╔╝╚╗╚╗╔╝O╚══╗║╚═╗╔╗║║║║║╚╗║╚╗╔══╗╚╗O╚╝╔╗║║╔╝║║╚╗╔╝╔╗╚╝║╔╗╔╗OOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO╔╗╔════╝╔═╗╔╗║║║║║║║╚╝╚╝║╔╝╚╗╔╝O╔╝╚═╝║╚═╝║╔╝O║║║╚╝╔╗╚╗║╚╗O╔══╝╚╗╔╝║║║║║╚╝╔╝╚═╝╚═╗╚╗╚═══╝║║║╚╗║╚═╝║╔╝║╔╗║║║║║O╔╗OOOOOOOOOO
OOOOOOOOOOOOOOOOO╔══╝║╚═══╗╔╝╔╝║║║║║║║╚╝O╔══╝╚═╗║╚╗╔╝╔╗╔╗╚══╗╚╝╔═╝║╚╗╔╝║╔╝╚╗╚╗╚╗╔╗╔╝╚╗║║║║╚╗O╚══╗╔══╝O║╔╗╔╗╔╝║║O║╚═╗╔╝╚╗║║║╚╝╚╝╚╗║║OOOOOOOOOO
OOOOOOOOOOOOOOOOO╚══╗╚════╝║O╚═╝╚╝║║║║╔══╝╔═╗╔═╝╚═╝╚╗║╚╝╚╗╔═╝╔╗╚═╗╚═╝╚╗║║╔═╝╔╝╔╝║║╚═╗╚╝║║║╔╝╔═══╝╚═══╗╚╝╚╝║╚╗║╚╗║╔═╝╚╗╔╝╚╝╚╗╔╗╔╗╚╝╚═╗OOOOOOOO
OOOOOOOOOOOOOOOOOOOO║╔╗╔═══╝╔═════╝║║║╚══╗║O║╚══╗O╔╗║╚╗╔╗║║╔╗║║╔═╝╔╗╔═╝╚╝╚═╗║O╚═╝║╔╗╚╗╔╝║║║O║╔═══╗╔══╝╔══╗╚═╝╚╗║║╚═╗╔╝║╔╗O╔╝║║║╚═╗╔═╝OOOOOOOO
OOOOOOOOOOOOOOOOOOOO║║╚╝╔╗╔═╝╔╗╔╗╔═╝║╚╗╔═╝╚╗╚╗╔╗╚═╝║║╔╝║╚╝╚╝║║╚╝╔╗║║╚══╗╔══╝╚══╗O║║║╔╝╚╗║║║╔╝║╔══╝║O╔═╝╔╗╚═══╗║║║╔╗║╚╗╚╝╚╗╚╗║║╚╗O║╚═╗OOOOOOOO
OOOOOOOOOOOOOOOOOOOO╚╝O╔╝╚╝╔═╝╚╝║║O╔╝╔╝╚═╗╔╝O║║║╔╗╔╝║║O╚══╗╔╝╚═╗║║║╚╗╔═╝║╔═╗╔══╝╔╝║║╚═╗║║║║║╔╝╚╗╔╗╚═╝╔═╝╚╗╔╗╔╝║║║║╚╝╔╝╔═╗╚╗║║╚╗╚╗╚══╝OOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO║╔╗╔╝╔═══╝╚╗╚╗║╔══╝║O╔╝║║║╚╝╔╝║╔═══╝╚╗╔═╝║╚╝╔╝╚═╗╚╝╔╝╚═╗╔╝╔╝║╔╗║╚╝╚╝║╚╗O╚╝║╔══╝O╔╗╚╝╚╝O╚╝║╚╗O╚╗║O╚╗║║╚╗║╔╝OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO║║║║O╚╗╔═╗╔╝╔╝║╚═╗╔╝╔╝╔╝║╚╗O╚═╝╚═══╗╔╝╚═╗║╔═╝╔══╝╔═╝╔╗╔╝╚╗╚╗║║║║╔═╗╔╝╔╝╔══╝╚═══╗║╚═══╗╔╗O╚╗╚╗╔╝╚═╗╚╝║╔╝║╚╗OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO║║╚╝╔═╝║╔╝╚╗║╔╝╔═╝║O╚╗║O╚╗╚══╗╔╗╔══╝╚══╗║║╚═╗║╔═╗╚═╗║║║╔═╝╔╝║║╚╝╚╗╚╝╔╝╔╝╔═╗╔╗╔╗╚╝╔╗╔╗╚╝╚═╗║╔╝║╔╗╔╝OO╚╝O╚═╝OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO║╚╗O╚═╗║╚╗╔╝║║O╚╗╔╝╔═╝╚═╗╚╗╔╗╚╝║╚══╗╔══╝╚╝O╔╝╚╝╔╝╔═╝║╚╝╚╗╔╝O╚╝╔══╝╔╗║O╚╗╚╗╚╝╚╝║╔╗║╚╝╚════╝║╚╗╚╝║║OOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO╚═╝O╔═╝╚╗║╚╗╚╝╔═╝╚╗╚═╗╔═╝╔╝║║╔╗╚╗╔═╝╚╗O╔╗O╔╝╔╗╔╝O║╔╗╚╗OO║╚═══╗╚══╗║║╚╗╔╝╔╝O╔╗╔╝║║╚╗╔╗╔╗╔╗O╚═╝╔╗╚╝OOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO║╔╗╔╝║╔╝╔═╝╔═╗║╔═╝╚═╗║╔╝║║║╔╝║╔═╗║╔╝╚═╝╔╝║╚═╗║║╚╗╚╗╔╝╔╗╔╗║╔══╝║║╔╝╚╗║╔═╝╚╝╔╝╚╗║║║║╚╝╚════╝╚╗OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO║║║╚╗║║O║╔╗╚╗╚╝╚═╗╔═╝║╚╗║║║║╔╝║O║║║╔═╗╔╝╔╝╔═╝║╚╗╚╗║╚╗║╚╝╚╝╚╗╔╗║║╚╗╔╝║╚╗╔═╗║O╔╝╚╝╚╝╔═════╗╔╗║OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOO╚╝╚═╝║║╔╝║║╔╝╔═══╝╚═╗║╔╝║║╚╝╚╗╚╗╚╝╚╝╔╝╚╗╚╗╚═╗╚═╝╔╝║╔╝╚═╗╔══╝║║║║╔╝║╔╝O╚╝╔╝╚╗╚═╗╔═╗║╔╗O╔╗║║╚╝OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╝║╔╝╚╝O╚═╗╔╗╔═╝║║O║║╔══╝╔╝O╔╗O║╔═╝O║╔╗╚══╗╚╗║╚╗╔═╝╚╗╔╗║║║║║╔╝║O╔╗╔╝╔╗╚═╗║╚╗║╚╝╚═╝║║║OOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╝OOO╔══╝║║╚═╗║╚╗╚╝╚╗╔╗║╔═╝║╔╝╚══╗║║╚╗╔╗║O╚╝O║╚╗╔═╝║╚╝╚╝║║╚╗║╔╝╚╝╔╝║╔═╝╚═╝╚═╗╔══╝╚╝OOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚══╗║║╔╗║╚╗╚╗OO║║╚╝╚═╗╚╝╔╗╔╗║║╚╗║║║║╔═══╝╔╝║╔╗╚═╗╔═╝║╔╝║╚╗╔╗║O║║╔════╗O║╚═╗OOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔══╝║╚╝║╚╗╚╗║OO╚╝O╔╗O╚═╗║╚╝║║║╔╝╚╝║║╚══╗╔╝O║║║╔═╝╚═╗║║╔╝O║║╚╝╔╝╚╝╔╗╔╗╚╗╚╗╔╝OOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚═══╝OO╚╗║O╚╝OOOO╔╝╚═══╝╚═╗║║║╚═╗O╚╝╔══╝╚╗O╚╝║║╔═══╝║╚╝╔═╝╚╗╔╝╔═╗║║║╚╗╚╗║║OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╝OOOOOOO╚════╗╔══╝║║║╔╗╚╗OO╚╗╔╗╔╝╔══╝║║╔══╗╚╗O╚╗╔═╝╚╗║O║║╚╝O╚═╝║║OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔═╗╔══╝╚══╗║║║║║╔╝OOO╚╝║╚╗║╔╗╔╝╚╝╔═╝╔╝╔═╝║╔══╝║╔╝╚════╗O╚╝OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╗║╚╗╔╗╔╗╔╝║║║║╚╝OOOOOO╚╗║╚╝║║OO╔╝╔═╝╔╝╔╗║╚═╗╔╝║╔╗╔╗╔╗╚╗╔╗OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔══╝╚═╝║╚╝╚╝O╚╝║║OOOOOOOOO╚╝OO║║OO╚╗║OO╚╗║║║╔═╝║╔╝║║║╚╝╚╗║║║OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO║╔══╗╔╗╚══╗OOOO║║OOOOOOOOOOOOO╚╝OOO╚╝OO╔╝║║║╚╗╔╝║╔╝║╚══╗║╚╝╚╗OOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚╝╔═╝║║╔╗╔╝OOOO╚╝OOOOOOOOOOOOOOOOOOOOOO╚╗║╚╝O╚╝O╚╝O║╔══╝╚══╗╚╗OOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔═╝╔╗║║║║║OOOOOOOOOOOOOOOOOOOOOOOOOOOOO╔╝╚╗O╔══════╝╚═════╗╚╗║OOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚══╝╚╝╚╝╚╝OOOOOOOOOOOOOOOOOOOOOOOOOOOOO╚══╝O╚═════════════╝O╚╝OOOOOOOOOOOOOOOOOOOOOOOOO
          )"""
