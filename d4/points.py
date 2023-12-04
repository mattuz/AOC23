from pathlib import Path
import re

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def points():
    points = 0
    for line in lines:
        start = line.index(":")
        stop = line.index("|")
        winning_lines = line[start:stop]
        rest = line[stop:-1]
        winning = [int(i) for i in winning_lines.split() if i.isdigit()]
        our_num = [int(i) for i in rest.split() if i.isdigit()]
        #print(winning)
        #print(our_num)
        correct = set(winning).intersection(our_num)
        if correct:
            #print(len(correct))
            points += 2**(len(correct)-1)
    print(points)




if __name__ == "__main__":
    points()