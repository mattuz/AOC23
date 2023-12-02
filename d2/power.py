from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

#max no. of cubes possible
RED = 12
GREEN = 13
BLUE = 14

def calc():
    tot = 0
    for game, line in enumerate(lines):
        #print(line)
        high_b = 0
        high_r = 0
        high_g = 0
        for index, char in enumerate(line):
            if char == "b":
                blue = line[index-3:index-1]
                if int(blue) >= high_b:
                    high_b = int(blue)
                
            if char == "r" and line[index-1] != "g":
                red = line[index-3:index-1]
                if int(red) >= high_r:
                    high_r = int(red)
            if char == "g":
                green = line[index-3:index-1]
                if int(green) >= high_g:
                    high_g = int(green)
        #print("b:", high_b)
        #print("g:", high_g)
        #print("r:", high_r)
        power = high_r*high_b*high_g
        #print("power:",power)
        tot += power
    return tot


if __name__ == "__main__":
    print(calc())   

