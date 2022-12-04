if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'
    n_subsets = 0
    with open(file_name) as f:
        lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            one, two = line.split(',')
            one_start, one_end = [int(x) for x in one.split('-')]
            two_start, two_end = [int(x) for x in two.split('-')]
            if one_start < two_start:
                if one_end >= two_end:
                    n_subsets += 1
            elif two_start < one_start:
                if two_end >= one_end:
                    n_subsets += 1
            elif one_start == two_start:
                n_subsets += 1

        print(f"{n_subsets =}")

