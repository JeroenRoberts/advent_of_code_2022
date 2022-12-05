def print_columns(crates_by_column):
    transposed_tuples = list(zip(*crates_by_column))
    crates_by_row = [list(x) for x in transposed_tuples]
    for row in crates_by_row:
        print(f"{''.join([x.replace('[0]', '   ') for x in row])}")

if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'
    with open(file_name) as f:
        lines = f.readlines()
        index = lines.index('\n')

        crates, moves = lines[:index-1], lines[index+1:]
        c = crates[0]
        for k, c in enumerate(crates):
            if c[:4] == 4*' ':
                c = '[0] ' + c[4:]
            c = c.replace('     ', ' [0] ').replace('    [', '[0] [').replace(']    ', '] [0] ').rstrip()
            crates[k] = c.split(' ')

        transposed_tuples = list(zip(*crates))
        crates_by_column = [list(x) for x in transposed_tuples]
        print_columns(crates_by_column)

        for move in moves:
            amount_to_move, start_column, end_column = [int(x) for x in move.rstrip().split(' ')[1::2]]
            start_column -= 1 #array index from 0
            end_column -= 1 #array index from 0
            

            print(f"{crates_by_column[start_column] =}")
            start = list(filter(lambda a: a!= '[0]', crates_by_column[start_column]))
            end = list(filter(lambda a: a!= '[0]', crates_by_column[end_column]))

            print(f"{start =}")
            crates_to_move = start[:amount_to_move]
            # crates_to_move.reverse()
            print(f"{crates_to_move =}")

            crates_by_column[start_column] = start[amount_to_move:]
            crates_by_column[end_column] = crates_to_move + end

            max_column_length = max([len(c) for c in crates_by_column])
            for i in range(len(crates_by_column)):
                crates_by_column[i] = ['[0]' for i in range(max_column_length-len(crates_by_column[i]))] + crates_by_column[i]
            print(f"{move =}")
            print_columns(crates_by_column)

        crates_by_column_no_padding = [list(filter(lambda a: a!= '[0]', c)) for c in crates_by_column]
        message = [c[0] for c in crates_by_column_no_padding]
        message = ''.join(message).replace('[', '').replace(']', '')
        print(f"{message =}")
