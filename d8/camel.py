from pathlib import Path
import re
import math
import numpy as np

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

instructions = lines[0]

nodes = {}

for line in lines[2:]:
    node = [c.strip("\n") for c in line.split(" = ")]
    result_list = [c.strip("\n") if i == 0 else tuple(map(str.strip, re.search(r'\((.*?)\)', c).group(1).split(','))) for i, c in enumerate(line.split(" = "))]
    nodes[result_list[0]] = result_list[1]

#print(instructions[0])

def recurse(i, node, key, times):
    if i == 277:
            print("restart")
            i = 0
    print("instruction:", instructions[i], "key:", key, "tuple:", node, "times:", times, "i:",i)
    if key == "MHG":
        print("done")
        return times
    else:
        if instructions[i] == "R":
            new_node = node[1]
            #do right
            return(recurse(i+1, nodes[new_node], new_node, times+1))
        elif instructions[i] == "L":
            #do left
            new_node = node[0]
            return(recurse(i+1, nodes[new_node], new_node, times+1))   
    pass

def iterative(node):
    times = 0
    iteration = 0
    while node != "ZZZ":
        if iteration == 277:
            iteration = 0
        if instructions[iteration] == "R":
            node = nodes[node][1]
            iteration += 1
        elif instructions[iteration] == "L":
            node = nodes[node][0]
            iteration += 1
        times += 1
    return times


def ghostwalk():
    ghoststart = []
    ghoststop = []
    for node in nodes:
        if node[2] == "A":
            ghoststart.append(node)
        elif node[2] == "Z":
            ghoststop.append(node)
    i = 0
    lengths = []
    for node in ghoststart:
        pathlength = 0

        while node[2] != "Z":
            if i == 277:
                i = 0
            if instructions[i] == "R":
                node = nodes[node][1]
                pathlength += 1
            elif instructions[i] == "L":
                node = nodes[node][0]
                pathlength += 1
            i += 1
        lengths.append(pathlength)
        
    return lengths
        


if __name__ == "__main__":
    #recurse(0, nodes["AAA"], "AAA", 0)
    print(iterative("AAA"))
    ans = ghostwalk()
    print(ans)
    print(math.lcm(*ans))
    pass