def priority(letter):
    if letter.isupper():
        priority = ord(letter) -76+38
    else:
        priority = ord(letter) - 96
    return priority

if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'

    total = 0
    with open(file_name) as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]
        groups = [lines[3*i:3*(i+1)] for i in range(len(lines)//3)]
        for group in groups:
            line1, line2, line3 = group
            intersect = set(line1).intersection(line2).intersection(line3)
            letter = intersect.pop()
            total += priority(letter)
    print(f"{total =}")
