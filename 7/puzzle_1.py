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
                        if lines[j][0] == '$':
                            if j == i+1:
                                u = lines[j]
                            else:
                                u = r'\n'.join(lines[i+1:j])
                            break
                        elif j == len(lines)-1:
                            if j == i +1:
                                u = lines[j]
                            else:
                                u = r'\n'.join(lines[i+1:j+1])
                            break
                    output.append(u)
            N_cmds += 1
    return N_cmds, cmds, args, output

def print_list(l):
    for k in range(len(l)):
        print(f"{l[k]}")

def get_parent_dir(current_dir):
    indices = [i for i, x in enumerate(current_dir) if x == '/']
    if len(indices) > 1:
        last = indices[-1]
        parent_dir = current_dir[:last]
    else:
        parent_dir = '/'
    return parent_dir

def recurse_total_file_size(info_dirs, info):
    total_file_size = info['local_file_size']
    for sub_folder in info['sub_folders']:
        total_file_size += recurse_total_file_size(info_dirs, info_dirs[sub_folder])
    return total_file_size

if __name__ == "__main__":
    # file_name = 'small_input.txt'
    file_name = 'input.txt'
    info_dirs = {}
    current_dir = ''
    with open(file_name) as f:
        lines = [l.rstrip() for l in f.readlines()]
        N_cmds, cmds, args, output = split_into_commands(lines)
        for i in range(N_cmds):
            if cmds[i] == 'cd':
                if args[i] == '/':
                    current_dir = '/'
                elif args[i] == '..':
                    current_dir = get_parent_dir(current_dir)
                else:
                    if current_dir != '/':
                        current_dir += '/' + args[i]
                    else:
                        current_dir += args[i]
            if cmds[i] == 'ls':
                info = {'sub_folders': [], 'local_file_size': 0, 'parent_folder': get_parent_dir(current_dir)}
                if current_dir == '/trtl/vmjljc/zcwpb':
                    print(f"{output[i] =}")

                if output[i] != '':
                    for x, y in [x.split(' ') for x in output[i].split(r'\n')]:
                        if x == 'dir':
                            if current_dir == '/':
                                info['sub_folders'] += [current_dir + y]
                            else:
                                info['sub_folders'] += [current_dir + '/' + y]
                        else:
                            info['local_file_size'] += int(x)
                info_dirs[current_dir] = info

    # for k, v in info_dirs.items():
    #     print(f"{k =} {v =}")
    for k, v in info_dirs.items():
        v['total_file_size'] = recurse_total_file_size(info_dirs, v)

    answer = 0
    for k, v in info_dirs.items():
        if v['total_file_size'] < 100000:
            answer += v['total_file_size']
    print(f"{answer =}")

