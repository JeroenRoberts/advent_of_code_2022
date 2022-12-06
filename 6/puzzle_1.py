import numpy as np
if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'
    with open(file_name) as f:
        lines = [x.rstrip() for x in f.readlines()]
        for line in lines:
            for i in range(14, len(line)):
                chars = line[i-14:i]
                if len(set(chars)) == 14:
                    print(f"{i = }")
                    break
