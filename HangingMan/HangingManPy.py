
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
    guessedChar = []
    charToGuess = ''
    while counter < times:
        charToGuess = input('What character do you want to guess?')
        if charToGuess in word and charToGuess not in guessedChar:
            print('Correct. The word has ', word.count(charToGuess), ' instances')
        elif charToGuess in word and charToGuess in guessedChar:
            print('This character has been approved.')
        else:
            print('Incorrect. You have ', times - 1 - counter , ' chances left.')
        counter+=1




def guessChar(c):
    return 0


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