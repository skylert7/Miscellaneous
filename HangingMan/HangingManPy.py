
#    _    _                   _               __  __                #
#   | |  | |                 (_)             |  \/  |               #
#   | |__| | __ _ _ __   __ _ _ _ __   __ _  | \  / | __ _ _ __     #
#   |  __  |/ _` | '_ \ / _` | | '_ \ / _` | | |\/| |/ _` | '_ \    #
#   | |  | | (_| | | | | (_| | | | | | (_| | | |  | | (_| | | | |   #
#   |_|  |_|\__,_|_| |_|\__, |_|_| |_|\__, | |_|  |_|\__,_|_| |_|   #
#                        __/ |         __/ |                        #
#                       |___/         |___/                         #
########### AND SOMETIMES I AM READY TO HANG MYSELF, LMAO ###########


import random

def guessingWord(word):
    counter = 0
    times = 5
    underScoreOfWord = underScore(word) # Underscore = '_ _ _ _ _ _ _ _ _ _ _ '
    guessedChar = []
    charToGuess = ''
    while counter < times:
        if counter == times - 1:
            print('Warning!! The man is about to die. Choose your next character carefully!')
        charToGuess = input('What character do you want to guess?')
        if charToGuess in word and charToGuess not in guessedChar:
            print('Correct. The word has ', word.count(charToGuess), ' instances')

        elif charToGuess in word and charToGuess in guessedChar:
            print('This character has been approved.')
        else:
            counter += 1
            print('Incorrect. You have ', times - counter , ' chances left.')


def underScore(word):
    underScore = ''
    for i in range(len(word)):
        underScore += '_'
        underScore += ' '
    return underScore



# This is main
fileName = '3000WordList.txt'
inFile = open(fileName, 'r')

word = [i[:-1] for i in inFile]
wantToPlay = True
while wantToPlay:
    randomPos = random.randint(1,len(word))
    guessingWord(word[randomPos])
    choice = input('Continue?')
    if choice[0] == 'n' or choice[0] == 'N':
        wantToPlay = False
print (word)