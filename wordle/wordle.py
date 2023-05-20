import requests

wordLength = 3 # Minimum Value
maxGuesses = 5 

def main():
    print("\n\t\t[ Welcome to Python Worlde by Jeiku Dev ]\n")
    
    modeSelect = int(input("\tSelect Mode:\n\t[1] Easy (3 Letters) \n\t[2] Intermediate (5 Lettters) \n\t[3] Hard (7 Letters) \n\t[4] Custom \n\t-> "))
    if modeSelect == 1:
        easyModeValue = 3
        secretWord = getSecretWord(easyModeValue)
        strFormSecretWord = "".join(ch for ch in secretWord if ch.isalnum())
            
    elif modeSelect == 2:
        easyModeValue = 5
        print(getSecretWord(easyModeValue))
            
    elif modeSelect == 3:
        easyModeValue = 7
        print(getSecretWord(easyModeValue))
            
    elif modeSelect == 4:
            print('custom')
    while True:
        print('\nI have thought up a Word.\n'
            + 'You have {} guesses to get it.'.format(maxGuesses))
        
        wordGuess = 1
        while wordGuess != maxGuesses:
            guess = input('\nGuess {}: '.format(wordGuess))
                        
            clues = getClues(guess, strFormSecretWord)
            print('Clue: ' + clues)
            wordGuess += 1
                        
            if guess == strFormSecretWord:
                break
            if wordGuess > maxGuesses:
                print('\nYou ran our of guesses\n'
                    + 'The Answer was {}.'.format(strFormSecretWord))

        if not input('\nDo you want to play again? (y/n/r): ').lower().startswith('y'):
            break
    print('\nThanks for Playing <3.\n')



def getSecretWord(wordLength):
    response = requests.get('https://random-word-api.vercel.app/api?length={}'.format(wordLength))
    if response.status_code == requests.codes.ok:
        return (response.text)
    else:
        print("Error:", response.status_code, response.text)


def getClues(guess, strFormSecretWord):
    if guess == strFormSecretWord:
        return 'You got it!!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == strFormSecretWord[i]:
            clues.append('Fermi')
        elif guess[i] in strFormSecretWord[i]:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
