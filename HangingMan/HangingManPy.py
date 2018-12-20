import random

def guessingWord(word):
    counter =
    times = 5
    charToGuess = ''
    while counter < times:
        charToGuess = input('What character do you want to guess?')
        if charToGuess in word:
            print('Correct. The word has ', word.count(charToGuess), ' instances')
        else:
            print('Incorrect. You have ', times - 1 - counter , ' chances left.')




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