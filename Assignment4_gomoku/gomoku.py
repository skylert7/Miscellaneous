import minimaxUtilsNumPy as util
import numpy as np
# Use between -1000 (O) and 1000 (X)
# 2 in a row -200 and 200
# 3 in a row -300 and 300
# 4 in a row -400 and 400
# 5 in a row -1000 and 1000


# Modify initial config for game here
XWIN = "X"*3
OWIN = "O"*3
BOARD_SIZE = 4 # 19x19

# End ---- Modify initial config for game here

if __name__ == '__main__':
    my_board = np.random.randint(-1, 2, size=(BOARD_SIZE, BOARD_SIZE))
    for i in my_board:
        print(util.convertToString(i))
    # my_board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    util.getWinner(my_board)





