from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

for line in lines:
    print(line)
    if "Time" in line:
        times = [int(i) for i in line.split() if i.isdigit()]
        time = int(''.join(map(str, times)))
    else:
        distances = [int(i) for i in line.split() if i.isdigit()]
        distance = int(''.join(map(str, distances)))

print(time)
print(distance)

def hold():
    tot = 1
    for n, time in enumerate(times):
        ways = 0
        for hold in range(0, time):
            movetime = time-hold
            speed = hold
            if movetime*speed > distances[n]:
                ways += 1
        #print(ways)
        tot *= ways
    print(tot)


def hold_large():
    tot = 1
    ways = 0
    for hold in range(0, time):
        movetime = time-hold
        speed = hold
        if movetime*speed > distance:
            ways += 1
    #print(ways)
    tot *= ways
    print(tot)
                
            

if __name__ == "__main__":
    #part 1
    hold()
    hold_large()