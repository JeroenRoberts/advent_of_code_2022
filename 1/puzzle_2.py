import numpy as np
if __name__ == "__main__":
    # file = 'small_input.txt'
    file = 'input.txt'
    with open(file) as f:
        lines = f.readlines()
        lines_string = ''.join(lines)
        lines_string_split = lines_string.split('\n\n')
        lines_string_split[-1] = lines_string_split[-1].rstrip()
        counts = [x.split('\n') for x in lines_string_split]
        N_elfs = len(counts)
        total = np.zeros(N_elfs)
        for n_elf in range(N_elfs):
            counts[n_elf] = np.array([int(i) for i in counts[n_elf]])
            total[n_elf] = np.sum(counts[n_elf])

        sorted = np.argsort(total)
        top_three = sorted[-3:]
        print(f"{top_three =}")
        calories_top_three = np.sum(total[top_three])
        print(f"{calories_top_three =}")

