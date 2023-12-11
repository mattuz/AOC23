from pathlib import Path
import re
import math
import numpy as np

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
p = Path(__file__).with_name("example.txt")
with p.open("r") as f:
    examples = f.readlines()


sequences = []
exsequences = []
hseq = {}
for line in lines:
    sequences.append([int(i.strip("\n")) for i in line.split(" ")])
for example in examples:
    exsequences.append([int(i.strip("\n")) for i in example.split(" ")])

def loop():
    histories = {} 
    tot_sum = 0
    for n, seq in enumerate(sequences):
        history = []
        history_recurse(seq, history)
        histories[n] = history[::-1]
        histories[n].append(seq)
    for n, seq in enumerate(sequences):
        for k, history in enumerate(histories[n]):
            #print(history)
            if k == 0:
                history.append(0)
            else:
                prev = histories[n][k-1][-1]
                new_val = prev + history[-1]
                history.append(new_val)   
        tot_sum += history[-1]
    print(tot_sum)

def loop_prev():
    histories = {} 
    tot_sum = 0
    for n, seq in enumerate(sequences):
        #print(seq)
        history = []
        history_recurse(seq, history)
        histories[n] = history[::-1]
        histories[n].append(seq)
    for n, seq in enumerate(sequences):
        for k, history in enumerate(histories[n]):
            if k == 0:
                history.insert(0, 0)
            else:
                prev = histories[n][k-1][0]
                new_val = history[0] - prev
                history.insert(0, new_val)   
        tot_sum += history[0]
    print(tot_sum)

def history_recurse(sequence, list):
    if sequence.count(0) == len(sequence):
        return sequence
    else:
        difflist = []
        for n, number in enumerate(sequence):
            if n == 0:
                continue
            else:
                prev = sequence[n-1]
                diff = number - prev
                difflist.append(diff)
        list.append(difflist)
        return history_recurse(difflist, list)


    




if __name__ == '__main__':
    loop()
    loop_prev()
    pass