from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

hands = {}
i_hands = []
cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


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
        #print("new hand")
        jokers = hand.count("J")
        house = False
        two_pair = False
        if all(c == hand[0] for c in hand):
            types["five"].append(hand)
            pass
        else:
            for c in hand:
                if hand.count(c) == 4:
                    if jokers == 1 or jokers == 4:
                        types["five"].append(hand)
                        #print("test")
                        break

                    types["four"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 3 and hand not in types["four"] and hand not in types["five"]:
                    for n in hand:
                        if hand.count(n) == 2 and n != c:
                            if n == "J":
                                pass
                                house = True
                                types["five"].append(hand)
                                break
                            elif jokers == 3:
                                house = True
                                types["five"].append(hand)
                                break
                            types["house"].append(hand)
                            house = True
                            break
                    if not house:
                        if jokers == 1 or c == "J":
                            types["four"].append(hand)
                            break
                        elif jokers == 2:
                            types["five"].append(hand)
                            break
                        
                        types["three"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 2 and hand not in types["house"] and hand not in types["five"]:
                    for n in hand:
                        if hand.count(n) == 2 and n != c:
                            if jokers == 1:
                                two_pair = True
                                types["house"].append(hand)
                                break
                            elif jokers == 2:
                                two_pair = True
                                types["four"].append(hand)
                                break
                            
                            types["two-pair"].append(hand)
                            two_pair = True
                            break
                    if not two_pair:
                        if jokers == 1:
                            types["three"].append(hand)
                            break
                        elif jokers == 2:
                            types["three"].append(hand)
                            break
                        types["pair"].append(hand)
                    break
            for c in hand:
                if hand.count(c) == 1 and hand not in types["two-pair"] and hand not in types["pair"] and hand not in types["four"] and hand not in types["three"] and hand not in types["five"] and hand not in types["house"]:
                    if jokers == 1: 
                        types["pair"].append(hand)
                        break
                    elif jokers == 2:
                        types["three"].append(hand)
                        break
                    types["high"].append(hand)
                    break
        pass  

def rank():
    score = 1
    rank = {}
    tot = 0
    for type in reversed(types):
        print(type)
        types[type].sort(key=cardSort)
        for hand in types[type]:
            rank[hand] = score
            score += 1
            tot += rank[hand] * hands[hand]
            print(hand, rank[hand], hands[hand], tot, hand.count("J"))
            #if hand == "AJAJA":
                #print("Y")
    print(tot)

if __name__ == "__main__":
    hand_strength()
    rank()
    pass