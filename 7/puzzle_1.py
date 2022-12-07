# def store_info(current_dir, list, dictionary):
#     dictionary['current_dir'] = 


# def parse(command, current_directory, prev_dictionary):
#     if command[2:4] == 'cd':
#         arg = command.split(' ')[-1]
#         if arg = '..'
#         current_dir = arg
#         prev_dictionary
#     elif command[2:4] == 'ls':
#         store_list(current_dir, prev_dictionary)

def split_into_commands(lines):
    N_cmds = 0
    cmds = []
    args = []
    output = []
    for i, line in enumerate(lines):
        if line[0] == '$':
            cmds.append(line[2:4])
            bin = line[2:4]
            if bin == 'cd':
                args.append(line.split(' ')[-1])
                output.append('')
            elif bin == 'ls':
                args.append('')
                if i < len(lines) - 1: 
                    for j in range(i+1, len(lines)):
                        if (lines[j][0] == '$') or (j == len(lines)-1):
                            u = r'\n'.join(lines[i+1:j])
                            output.append(u)
                            break
            N_cmds += 1
    return N_cmds, cmds, args, output
def print_list(l):
    for k in range(len(l)):
        print(f"{l[k]}")

if __name__ == "__main__":
    file_name = 'small_input.txt'
    top_level_dirs = {}
    current_dir = ''
    with open(file_name) as f:
        lines = [l.rstrip() for l in f.readlines()]
        N_cmds, cmds, args, output = split_into_commands(lines)
        for i in range(N_cmds):
            print(f"\n\n{i=}")
            print(f"{cmds[i] =}")
            print(f"{args[i] =}")
            print_list(output[i].split(r'\n'))
