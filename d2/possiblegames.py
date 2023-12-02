from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

#max no. of cubes possible
RED = 12
GREEN = 13
BLUE = 14

test = "Game 7: 16 blue, 4 green, 9 red; 6 red, 2 blue, 12 green; 2 red, 5 green, 14 blue; 11 blue, 13 red; 10 blue, 3 red, 17 green; 1 green, 12 blue"


def calc():
    possible = True
    tot = 0
    for game, line in enumerate(lines):
        game = game+1
        print(game)
        for index, char in enumerate(line):
            #print(index, char)
            if char == "b":
                blue = line[index-3:index-1]
                if int(blue) > BLUE:
                    possible = False
                #print(blue)
                pass
            if char == "r":
                red = line[index-3:index-1]
                if int(red) > RED:
                    possible = False
                pass
            if char == "g":
                green = line[index-3:index-1]
                if int(green) > GREEN:
                    possible = False
                pass
        if possible:
            tot += game
            #print("total value is now: ",tot)
        else:
            possible = True
    return tot


for index, char in enumerate(test):
    #print(index, char)
    if char == "b":
        blue = test[index-3:index-1]
        #print(blue)
        pass
    if char == "r":
        red = test[index-3:index-1]
        pass
    if char == "g":
        green = test[index-3:index-1]
        pass



if __name__ == "__main__":
    print(calc())   

