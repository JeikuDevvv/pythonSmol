import random

numberDigits = 3
maxGuesses = 10

def main():
    
    print("\nI am thinking of a {} number. Try to guess what it is.\n\n".format(numberDigits)
        + "When I say:   |  That's means:\n"
        + "Pico          |  One digit is correct but in the wrong position.\n"
        + "Fermi         |  One digit is correct and in the right position.\n"
        + "Bagels        |  No digit is correct.\n\n")
    
    while True:
        secretNumber = getSecretNumber()
        print('\nI have thought up a number.\n'
            + 'You have {} guesses to get it.'.format(maxGuesses))
        
        numberGuesses = 1
        while numberGuesses <= maxGuesses:
            guess = ''
            while len(guess) != numberDigits or not guess.isdecimal():
                print('')
                guess = input('Guess {}: '.format(numberGuesses))
                
            clues = getClues(guess, secretNumber)
            print('Clue: ' + clues)
            numberGuesses += 1
            
            if guess == secretNumber:
                break
            if numberGuesses > maxGuesses:
                print('\nYou ran our of guesses\n'
                    + 'The Answer was {}.'.format(secretNumber))

        if not input('\nDo you want to play again? (y/n): ').lower().startswith('y'):
            break
        print('\nThanks for Playing <3.')

def getSecretNumber():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNumber = ''
    for i in range(numberDigits):
        secretNumber += str(numbers[i])    
    return secretNumber

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return 'You got it!!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Fermi')
        elif guess[i] in secretNumber[i]:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()