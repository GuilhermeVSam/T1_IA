import numpy as np
import pandas as pd
import random

def won(player, matrix):
    # Check rows
    for row in matrix:
        if np.all(row == player):
            return True
    
    # Check columns
    for col in matrix.T:
        if np.all(col == player):
            return True
    
    # Check diagonals
    if np.all(np.diag(matrix) == player):
        return True
    if np.all(np.diag(np.fliplr(matrix)) == player):
        return True
    
    return False

# Initialize lists to store results
draw = []
still_playing = []

# Initialize a set to track unique results
unique_results = set()

# Initialize a counter to keep track of saved results
counter = 0

# Run until each list contains 400 unique entries
while len(still_playing) < 400:
    aX = random.randint(0, 5)
    aO = aX - 1 if aX > 0 else 0
    aB = 9 - (aX + aO)

    # Create a list with the appropriate number of X, O, and blanks
    elements = ['1'] * aX + ['-1'] * aO + ['0'] * aB

    # Shuffle the list to randomize the order
    random.shuffle(elements)

    # Reshape the list into a 3x3 matrix
    ttt = np.array(elements).reshape(3, 3)

    # Check if X or O won
    winner = '0'
    if won('1', ttt):
        winner = '1'
    elif won('-1', ttt):
        winner = '-1'
    elif aX == 5:
        winner = '2'

    # Flatten the matrix and concatenate with the winner
    flat_ttt = ttt.flatten()
    result = ';'.join(flat_ttt) + ';' + winner

    # Check if the result is unique
    if result not in unique_results:
        unique_results.add(result)
        # Store the result in the appropriate list
        if winner == '0' and len(still_playing) < 400:
            counter += 1
            print("Saved OG (",counter,"/400)")
            still_playing.append(result)
        
        # Increment the counter

# Combine all results into a single list
all_results = still_playing

# Create a DataFrame from the results
df = pd.DataFrame(all_results)

# Save the DataFrame to a CSV file
df.to_csv('tic_tac_toe_results.csv', index=False)

print(f"Results saved to tic_tac_toe_results.csv.")