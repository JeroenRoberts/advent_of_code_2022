def determine_winner(opponent_move, response):
    win = {
            'A': 'Y',
            'B': 'Z',
            'C': 'X',
            }
    draw = {
            'A': 'X',
            'B': 'Y',
            'C': 'Z',
            }

    if draw[opponent_move] == response:
        return 3
    elif win[opponent_move] == response:
        return 6
    else:
        return 0

if __name__ == "__main__":
    # file = 'small_input.txt'
    file = 'input.txt'
    score_for_move = {
            'X': 1,
            'Y': 2,
            'Z': 3,
            }
    total_score = 0
    with open(file) as f:
        lines = f.readlines()
        for round in lines:
            opponent_move, response = round.rstrip().split(' ')
            score = determine_winner(opponent_move, response)
            score += score_for_move[response]
            total_score += score
    print(f"{total_score =}")
