if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'
    n_overlaps = 0
    with open(file_name) as f:
        lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            one, two = line.split(',')
            one_start, one_end = [int(x) for x in one.split('-')]
            two_start, two_end = [int(x) for x in two.split('-')]
            if one_start <= two_start:
                if one_end >= two_start:
                    n_overlaps += 1
            else:
                if two_end >= one_start:
                    n_overlaps += 1

        print(f"{n_overlaps =}")

