import itertools
import numpy as np
import pandas as pd

def won(player, matrix):
    for row in matrix:
        if np.all(row == player):
            return True
    
    for col in matrix.T:
        if np.all(col == player):
            return True
    
    if np.all(np.diag(matrix) == player):
            return True
    if np.all(np.diag(np.fliplr(matrix)) == player):
            return True
    
    return False


symbols = ['1', '-1']
all_boards = list(itertools.product(symbols, repeat=9))


draw_boards = []
for board in all_boards:
    ttt = np.array(board).reshape(3, 3)
    if not won('1', ttt) and not won('-1', ttt):
        # Ensure the number of X and O are balanced
        if board.count('1') == 5 and board.count('-1') == 4:
            draw_boards.append(board)
        elif board.count('1') == 4 and board.count('-1') == 5:
            draw_boards.append(board)

draw_results = [';'.join(board) + ';2' for board in draw_boards]
df = pd.DataFrame(draw_results)
df.to_csv('tic_tac_toe_draws.csv', index=False)

print("Draw possibilities saved to tic_tac_toe_draws.csv")