import random

def guessingWord(word):
    charToGuess = input('What character do you want to guess?')
    if charToGuess in word:

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