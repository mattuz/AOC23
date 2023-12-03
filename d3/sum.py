from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

symbols = []
gears = []
new_num = True
numdict = {}


def calc():
    temp = ""
    tot = 0
    adjacent = []
    for y, line in enumerate(lines):
        print(line)
        for x, c in enumerate(line):
            if c.isdigit():
                temp += c
                adjacent.append((x-1,y))
                adjacent.append((x+1,y))
                adjacent.append((x,y-1))
                adjacent.append((x,y+1))
                adjacent.append((x-1,y-1))
                adjacent.append((x-1,y+1))
                adjacent.append((x+1,y-1))
                adjacent.append((x+1,y+1))
            
            else:
                if temp != "":
                    print(temp)
                    for coordinate in adjacent:
                        if coordinate in symbols:
                            #print("yes! add:", temp)
                            tot += int(temp)
                            break
                temp = ""
                adjacent = []
    print(tot)

                
                

def symbol_pos():
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if not c.isdigit() and c != "." and c != "\n":
                print(c)
                symbols.append((x, y))

def gear_pos():
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                gears.append((x, y))

def num_pos():
    temp = ""
    tot = 0
    coord = []
    for y, line in enumerate(lines):
        #print(line)
        for x, c in enumerate(line):
            if c.isdigit():
                temp += c
                coord.append((x, y))
            
            else:
                if temp != "":
                    #print(temp)
                    #print("yes! add:", temp)
                    #tot += int(temp)
                    for pair in coord:
                        numdict.update({pair: temp})
                coord = []
                temp = ""
    #print(tot)
    #print(numdict)
    #if (64,133) in numdict:
        #print("yes")
        #print(numdict[(65,133)])

def gear_calc():
    tot = 0
    for gear in gears:
        numbers = 0
        neighbour = []
        x, y = gear
        neighbour.append((x+1,y))
        neighbour.append((x-1,y))
        neighbour.append((x+1,y+1))
        neighbour.append((x+1,y-1))
        neighbour.append((x-1,y+1))
        neighbour.append((x-1,y-1))
        neighbour.append((x,y+1))
        neighbour.append((x,y-1))

        for pos in neighbour:
            if pos in numdict:
                if numbers == 0:
                    n1 = int(numdict[(pos)])
                    numbers += 1
                else:
                    n2 = int(numdict[(pos)])
                    if n1 != n2: #bad practice but it works in this assignment :)
                        tot += n1*n2
                        print("found pair!", n1, "and", n2)
                        break
    print(tot)

                



if __name__ == "__main__":
    #symbol_pos()
    gear_pos()
    num_pos()
    gear_calc()
    #print(symbols)
    #calc()
    #print(symbols)
    pass