from pathlib import Path
import numpy as np

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
p = Path(__file__).with_name("example.txt")
with p.open("r") as f:
    exlines = f.readlines()

seeds = np.array([int(i) for i in lines[0].split() if i.isdigit()])
exseeds = np.array([int(i) for i in exlines[0].split() if i.isdigit()])

locations = []
#55 13
seeds_l = []

vals = []
#for line in lines[3:]:
#    l = [int(i) for i in line.split() if i.isdigit()]
#    vals.append(l)
    
for line in lines:
    l = [int(i) for i in line.split() if i.isdigit()]
    vals.append(l)

exvals = []
for line in exlines[:29]:
    l = [int(i) for i in line.split() if i.isdigit()]
    exvals.append(l)

for line in lines[180:197]:
    l = [int(i) for i in line.split() if i.isdigit()]
    locations.append(l)

exlocations = []
for line in exlines[31:33]:
    l = [int(i) for i in line.split() if i.isdigit()]
    exlocations.append(l)

seed_list = []
for n, seed in enumerate(seeds):
    #print(seed)
    if n%2 == 0:
        x = seed
        y = seed + seeds[n+1]-1
        seed_list.append((x, y))
#print(seed_list)

def backwards():
    for i in range(0,1000000000000):
        if i%1000000 == 0:
            print(i)
        #print("new loc:", i)
        curr = i
        found = False
        done = False
        for l in vals[::-1]:
            #print(curr)
            if l == []:
                found = False
            elif len(l) == 20:
                #print(l)
                for seed in seed_list:
                    #print(seed)
                    if curr >= min(seed) and curr <=max(seed):
                        print("target acquired")
                        print("seed:", curr, "corresponds to:", i)
                        
                        print("----------------end-----------------")
                        return
            
            elif not found:
                #print("not found")
                destination = l[1]
                source = l[0]
                ranges = l[2]
                
                if curr >= source and curr < source+ranges:
                        #print("update curr")
                        new = destination + (curr-source)
                        curr = new
                        found = True
        # for n, seed in enumerate(seeds):
            #if n%2 == 0:

    #print(min(seeds_l))



                
    


if __name__ == "__main__":
    pass
    backwards()
    #print(exlocations)
   # print(exseeds)