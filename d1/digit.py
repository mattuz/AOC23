from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()


def calc():
    sum = 0
    for line in lines:
        print(line)
        line = change_line(line)
        print(line)
        first = 0
        second = 0
        first_num = True
        for char in line:
            if char.isdigit():
                if first_num:
                    first = char
                    first_num = False
                    second = char
                else:
                    second = char
        conc_num=first+second
        print("To be added: ", conc_num)
        sum += int(conc_num)
    print(sum)


def change_line(line):
    #due to overlaps keep "necessary" letters
    if "one" in line:
        line = line.replace("one","o1e")
    if "two" in line:
        line = line.replace("two","t2o")
    if "three" in line:
        line = line.replace("three","th3e")
    if "four" in line:
        line = line.replace("four","4")
    if "five" in line:
        line = line.replace("five","5e")
    if "six" in line:
        line = line.replace("six","6")
    if "seven" in line:
        line = line.replace("seven","7n")
    if "eight" in line:
        line = line.replace("eight","e8t")
    if "nine" in line:
        line = line.replace("nine","9e")
    return line
#overlaps:
#oneight, twone, twoneight, twoneighthree, threeight, fiveight, sevenine, sevenineight.......


if __name__ == "__main__":
    calc()
    #new_lines = change_line(lines)
    #calc(new_lines)

