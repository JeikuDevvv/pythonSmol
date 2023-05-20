import requests

wordLength = 3 # Minimum Value
maxGuesses = 5 

def main():
    print("\n\t\t[ Welcome to Python Worlde by Jeiku Dev ]\n")
    while True:
        modeSelect = int(input("\tSelect Mode:\n\t[1] Easy (3 Letters) \n\t[2] Intermediate (5 Lettters) \n\t[3] Hard (7 Letters) \n\t[4] Custom \n\t-> "))
    
        if modeSelect == 1:
            easyModeValue = 3
            secretWord = getSecretWord(easyModeValue)
        elif modeSelect == 2:
            easyModeValue = 5
            print(getSecretWord(easyModeValue))
            
        elif modeSelect == 3:
            easyModeValue = 7
            print(getSecretWord(easyModeValue))
            
        elif modeSelect == 4:
            print('custom')

        print('\nI have thought up a Word.\n'
            + 'You have {} guesses to get it.'.format(maxGuesses))
        
        wordGuess = 1
        while wordGuess != maxGuesses:
            guess = input('Guess {}: '.format(wordGuess))
            wordGuess += 1
    
            strFormSecretWord = secretWord[0]
            
            if guess == strFormSecretWord:
                print('You got it!')
                break
            else:
                print('BOBO!!' + secretWord)

def getSecretWord(wordLength):
    response = requests.get('https://random-word-api.vercel.app/api?length={}'.format(wordLength))
    if response.status_code == requests.codes.ok:
        return (response.text)
    else:
        print("Error:", response.status_code, response.text)

def getClues(guess, secretWord):
    if guess == secretWord:
        return 'You got it!!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            clues.append('Fermi')
        elif guess[i] in secretWord[i]:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
