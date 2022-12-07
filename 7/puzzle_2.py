from puzzle_1 import split_into_commands
from puzzle_1 import print_list
from puzzle_1 import get_parent_dir
from puzzle_1 import recurse_total_file_size

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

