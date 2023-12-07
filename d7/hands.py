from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

hands = {}
i_hands = []
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


for line in lines:
    hand, bid = [i for i in line.split(" ")]
    bid = int(bid)
    hands[hand] = bid
    i_hands.append(hand)

value = {}
val = 0
for card in cards[::-1]:
    val += 1
    value[card] = val


def cardSort(card):
    #print(card)
    return [value.get(char, 0) for char in card]
#print(value["2"])

types = {"five": [], "four": [], "house": [], 
         "three": [], "two-pair": [], 
         "pair": [], "high": []}

def hand_strength():
    for hand in i_hands:
        house = False
        two_pair = False
        if all(c == hand[0] for c in hand):
            types["five"].append(hand)
        else:
            for c in hand:
                if hand.count(c) == 4:
                    types["four"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 3:
                    for n in hand:
                        if hand.count(n) == 2 and n != c:
                            types["house"].append(hand)
                            house = True
                            break
                    if not house:
                        types["three"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 2 and hand not in types["house"]:
                    for n in hand:
                        if hand.count(n) == 2 and n != c:
                            types["two-pair"].append(hand)
                            two_pair = True
                            break
                    if not two_pair:
                        types["pair"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 1 and hand not in types["two-pair"] and hand not in types["pair"] and hand not in types["four"] and hand not in types["three"]:
                    types["high"].append(hand)
                    break
        pass  

def rank():
    score = 1
    rank = {}
    tot = 0
    for type in reversed(types):
        #print(type)
        types[type].sort(key=cardSort)
        for hand in types[type]:
            #print(hand)
            rank[hand] = score
            score += 1
            
        #print(type)
            tot += rank[hand] * hands[hand]
            print(hand, rank[hand], hands[hand], tot)
    print(tot)

if __name__ == "__main__":
    hand_strength()
    rank()
    #print(types)
    #print(value)
    pass