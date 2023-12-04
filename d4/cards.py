from pathlib import Path
import re

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def points():
    tot_cards = 0
    iterations = [1]*(len(lines))
    for i, line in enumerate(lines):
        start = line.index(":")
        stop = line.index("|")
        winning_lines = line[start:stop]
        rest = line[stop:-1]
        winning = [int(i) for i in winning_lines.split() if i.isdigit()]
        our_num = [int(i) for i in rest.split() if i.isdigit()]
        correct = set(winning).intersection(our_num)
        
        for times in range(iterations[i]):
            tot_cards+=1
            if correct:
                new_cards = len(correct)

                for n in range(new_cards):
                    iterations[i+1+n] += 1
    print(tot_cards)




if __name__ == "__main__":
    points()