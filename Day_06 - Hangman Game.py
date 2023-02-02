# TITLE: Hangman Game
# DESCRIPTION: Interactive hangman game with given word list of various animals.
# DATE: 02Feb2023

from rescBin import hangmanAscii # retrieve ASCII art from resource bin
import random
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

randWord = list(random.choice(words))
blank = list('_'*len(randWord))
wordBank = []
lives = 0

print('Word:',''.join(blank))
#print(''.join(randWord)) # answer

while "_" in blank:
    
    answerLetter = input('Guess a Letter:\n')
    if len(answerLetter) == 1: wordBank.append(answerLetter)
    wrongAnswer = True

    for i in range(len(randWord)):
        if answerLetter == randWord[i]:
            blank[i] = randWord[i]
            wrongAnswer = False
    
    if wrongAnswer==True: lives +=1

    print(hangmanAscii(lives),'\n\n')    
    print('Word:',''.join(blank))
    print('Word Bank: ',' '.join(wordBank))

    if lives == 6:
        print('You Lose!')
        exit()
    
print('You Win!')

    


