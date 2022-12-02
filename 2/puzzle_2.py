def determine_response(opponent_move, strategy):
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
    lose = {
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
            }


    if strategy == 'X': #lose
        return lose[opponent_move]
    elif strategy == 'Y': #draw
        return draw[opponent_move]
    elif strategy == 'Z': #win
        return win[opponent_move]

if __name__ == "__main__":
    # file = 'small_input.txt'
    file = 'input.txt'
    score_for_round = {
            'X': 0,
            'Y': 3,
            'Z': 6,
            }

    score_for_move = {
            'X': 1,
            'Y': 2,
            'Z': 3,
            }

    total_score = 0
    with open(file) as f:
        lines = f.readlines()
        for round in lines:
            opponent_move, strategy = round.rstrip().split(' ')
            response = determine_response(opponent_move, strategy)
            score = score_for_round[strategy]
            score += score_for_move[response]
            total_score += score
    print(f"{total_score =}")
