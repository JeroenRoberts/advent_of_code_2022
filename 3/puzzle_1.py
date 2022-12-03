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
        for line in lines:
            rucksack_1, rucksack_2 = line[:len(line)//2] , line[len(line)//2:]
            intersect = set(rucksack_1).intersection(rucksack_2)
            letter = intersect.pop()
            total += priority(letter)
    print(f"{total =}")
