import numpy as np
import random
import matplotlib.pyplot as plt

N = 10

def count_attacking_pairs(board):
    attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacking_pairs += 1
    return attacking_pairs

def queens(tau):
    board = np.random.randint(N, size = N)
    curr_att_pairs = count_attacking_pairs(board)
    num_sideway_moves = 0
    steps = 0
    while True:
        steps += 1
        sideways_moves = {} 
        strictly_better_moves = {}
        for col in range(N):
            for row in range(N):
                if board[col] != row:
                    newboard = board.copy()
                    newboard[col] = row
                    att_pairs = count_attacking_pairs(newboard)
                    if att_pairs < curr_att_pairs:
                        strictly_better_moves[(col,row)] = att_pairs
                    elif att_pairs == curr_att_pairs:
                        sideways_moves[(col,row)] = att_pairs
        if strictly_better_moves:
            move = min(strictly_better_moves,key = strictly_better_moves.get)
            board[move[0]] = move[1]
            curr_att_pairs = strictly_better_moves[move]
            if strictly_better_moves[move] == 0:
                break
        elif sideways_moves and num_sideway_moves < tau:
            move = random.choice(list(sideways_moves.keys()))
            board[move[0]] = move[1]
            curr_att_pairs = sideways_moves[move]
            num_sideway_moves += 1
        else:
            break
    
    if curr_att_pairs == 0:
        return "SUCCESS", steps
    else:
        return "FAIL", steps
 


success_count = {tau: 0 for tau in [1, 10, 20, 50, 100]}
success_steps = {tau: [] for tau in [1, 10, 20, 50, 100]}

for tau in [1,10,20,50,100]:
    for run in range(1,101):
        result, steps = queens(tau)
        if result == "SUCCESS":
            success_count[tau] += 1
            success_steps[tau].append(steps)

success_rate = [success_count[tau] for tau in [1, 10, 20, 50, 100]]
average_steps = [np.mean(success_steps[tau]) if success_steps[tau] else 0 for tau in [1, 10, 20, 50, 100]]

plt.figure(figsize=(8, 6))
plt.plot([1, 10, 20, 50, 100], success_rate, marker='o')
plt.title('Success Rate vs Tau')
plt.xlabel('Tau')
plt.ylabel('Number of Successful Runs in 100 Runs')
plt.show()

plt.figure(figsize=(8, 6))
plt.plot([1, 10, 20, 50, 100], average_steps, marker='o')
plt.title('Average Steps vs Tau')
plt.xlabel('Tau')
plt.ylabel('Average Steps Taken')
plt.show()

