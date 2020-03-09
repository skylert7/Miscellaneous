# Board example = [-1,0,1, 1,1,-1, -1,0,0]
import copy
import numpy as np
# getNameForBoard(b) isGameOver(b) getWinner(b) genNextMovesList(b)
counter_number_of_nodes_visited = 0

class node():

    def __init__(self, board):
        self.board = board  # the list of 1,-1 and 0s
        self.children = []
        self.score = None
        self.bestMove = None   # for later use

    def isEndNode(self):
        if getWinner(self.board) == 1 or getWinner(self.board) == -1 :
            return True
        if 0 not in self.board:
            return True
        # modify this code
        # True of win or tie

    def evaluate(self):
        # modify this code
        # we only call if an end node
        # return either 1, -1, or 0
        if getWinner(self.board) == None:
            return 0
        return getWinner(self.board)

    def getChildren(self):
        # use your utility function to get next boards
        # and then create nodes from the board array
        childBoards = genNextMovesList(self.board)
        for b in childBoards:
            self.children.append(node(b))
        return self.children


def minimax(node, maximizingScore):
    global counter_number_of_nodes_visited
    counter_number_of_nodes_visited = counter_number_of_nodes_visited + 1
    if node.isEndNode():
        # expect 0, 1 or -1
        value = node.evaluate()
        node.score = value
        return value

    bestScore = -999 if maximizingScore else 999
    for child in node.getChildren():
        score = minimax(child, not maximizingScore)
        if maximizingScore:
            bestScore = max(score, bestScore)
        else:
            bestScore = min(score, bestScore)

    # store score in node
    node.score = bestScore
    return bestScore

def alphaBeta(node, alpha, beta, maximizingScore):
    global counter_number_of_nodes_visited
    counter_number_of_nodes_visited = counter_number_of_nodes_visited + 1
    if node.isEndNode():
        # expect 0, 1 or -1
        value = node.evaluate()
        node.score = value
        return value

    if maximizingScore:
        bestScore = -999
    else:
        bestScore = 999

    for child in node.getChildren():
        score = alphaBeta(child, alpha, beta, not maximizingScore)
        if maximizingScore:
            bestScore = max(score, bestScore)
            alpha = max(alpha, bestScore)
        else:
            bestScore = min(score, bestScore)
            beta = min(beta, bestScore)

        # time to prune?
        if beta <= alpha:
            break  # stop evaluating

    # store score in node
    node.score = bestScore
    return bestScore

def next_turn(b):
    '''
    :param b:
    :return: 1 for player X
            -1 for player O
            or None if no more moves
    '''
    # If no elements in board is 0 (meaning no empty space)
    if 0 not in b:
        return None

    # If there exists at least one empty space in board
    if np.sum(b) == 0:
        return 1 # Player X's turn

    if np.sum(b) == -1:
        return 1 # Player X's turn

    if np.sum(b) == 1:
        return -1 # Player O's turn


def getWinner(b):
    '''
    :param b:
    :return: 1 or -1 or None :if no winner
    '''
    directions = [([0, 1], [0, -1]), ([1, 0], [-1, 0]), ([-1, 1], [1, -1]), ([1, 1], [-1, -1])]
    for direction in directions:
        continue_chess = 0
    return False


    # ------------------- Tie -------------------
    if 0 not in b:
        return None

    return

def is_legal_board(b):
    '''
    :param b:
    :return: True if a legal board otherwise return False
    legal board has 9 entries and only 0, 1, -1
    where sum of all values is either 0, -1 or 1
    '''

    # Check number of entry
    if len(b) != 9:
        return False

    # Check value of each entry
    for index in b:
        if index not in [0, 1, -1]:
            return False

    # Check sum
    if sum(b) not in [0, 1, -1]:
        return False

    # Returns True if all tests passed
    return True

def isGameOver(b):
    '''
    There is a winner OR a Tie
    '''

    #Either X or O is winner
    if getWinner(b) == 1 or getWinner(b) == -1:
        return True

    #------- This is a TIE -------
    if 0 not in b:
        return True

    return False

def getNameForBoard(b):
    charVal = '.XO'
    nameStr = ""
    for idx, val in enumerate(b):
        nameStr= nameStr + charVal[val]
        if idx == 2 or idx == 5:
            nameStr = nameStr + '|'
    nameStr = nameStr + '|'
    return nameStr

def genNextMovesList(b):
    '''

    :param b:
    :return: a list of lists of boards for some board

    '''
    next_moves_list = np.zeroes((1,3), dtype=int)

    #If there is a next turn for Player O => generating boards for Player O
    if next_turn(b) == -1:
        for row in range(len(b)):
            for col in range(len(b[row])):
                if b[row][col] == 0:
                    deep_copy_of_b = copy.deepcopy(b)
                    deep_copy_of_b[row][col]  = -1
                    next_moves_list.append(deep_copy_of_b)

    #If there is a next turn for Player X => generating boards for Player X
    if next_turn(b) == 1:
        for row in range(len(b)):
            for col in range(len(b[row])):
                if b[row][col] == 0:
                    deep_copy_of_b = copy.deepcopy(b)
                    deep_copy_of_b[row][col]  = 1
                    next_moves_list.append(deep_copy_of_b)

    return next_moves_list

test_arr = np.zeros((1,3), dtype= int)

print(np.append(test_arr, [1, 2, 3]))