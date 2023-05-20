import requests

wordLength = 3 # Minimum Value
maxGuesses = 5

def main():
    print("\n\t\t[ Welcome to Python Worlde by Jeiku Dev ]\n")
    
    modeSelect = int(input("\tSelect Mode:\n\t[1] Easy (3 Letters) \n\t[2] Intermediate (5 Lettters) \n\t[3] Hard (7 Letters) \n\t[4] Custom \n\t-> "))
    if modeSelect == 1:
        modeValue = 3
        secretWord = getSecretWord(modeValue)
        
    elif modeSelect == 2:
        modeValue = 5
        print(getSecretWord(modeValue))
            
    elif modeSelect == 3:
        modeValue = 7
        print(getSecretWord(modeValue))
            
    elif modeSelect == 4:
            print('custom')
    while True:
        strFormSecretWord = "".join(ch for ch in secretWord if ch.isalnum())
        print('\n\tI have thought up a Word.\n\t'
            + 'You have {} guesses to get it.'.format(modeValue))
            
        wordGuesses = 1
        while wordGuesses <= maxGuesses:
            guess = ''
            while len(guess) != modeValue or not guess.isdecimal():
                guess = input("\n\tGuess #{} ".format(wordGuesses))
            
                clues = getClues(guess, strFormSecretWord)
                print("\tClues: {}".format(clues))
                wordGuesses += 1
            wordGuesses += 1
            
            if guess == strFormSecretWord:
                break
            if wordGuesses > modeValue:
                print("\n\tYou run out of guesses! The Answer was {} ".format(strFormSecretWord))
        
        response = input("\n\tDo you wanna play Again? (y/n/r) : ").lower()
        if response == 'n':
            break
        if response == 'r':
            main()
    
    print("\n\tTHANK YOU FOR PLAYING!!!")

def getSecretWord(wordLength):
    response = requests.get('https://random-word-api.vercel.app/api?length={}'.format(wordLength))
    if response.status_code == requests.codes.ok:
        return (response.text)
    else:
        print("Error:", response.status_code, response.text)


def getClues(guess, strFormSecretWord):
    if guess == strFormSecretWord:
        return '\n\tYou got it!!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == strFormSecretWord[i]:
            clues.append('Letter Found in place!')
        elif guess[i] in strFormSecretWord[i]:
            clues.append('Letter Found!')
            
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
