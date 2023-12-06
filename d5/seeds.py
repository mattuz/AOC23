from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
p = Path(__file__).with_name("example.txt")
with p.open("r") as f:
    example = f.readlines()

seeds = [int(i) for i in lines[0].split() if i.isdigit()]
exseeds = [int(i) for i in example[0].split() if i.isdigit()]

#destination, source, range
#exseeds = [1]
locations = []

def main():
    for seed in seeds:
        print("seed:",seed)
        curr = seed
        found = False
        for line in lines[3:]:
            l = [int(i) for i in line.split() if i.isdigit()]
            #print(l)
            #print(l)
            #print(l)
            if l == []:
                found = False
                pass
            elif not found:
                #print("test")
                destination = l[0]
                source = l[1]
                range = l[2]
                if curr >= source and curr < source+range:
                    new = destination + (curr-source)
                    curr = new
                    found = True
        #print("done!",curr)
        locations.append(curr)
    print(min(locations))


                


def map(curr, destination, source, length):
    dst = []
    src = []
    pass
    


if __name__ == "__main__":
    main()