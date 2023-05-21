import requests

wordLength = 5
maxGuesses = 10


def main():
    secretWord = getSecretWord(wordLength)
    print("\n[ Welcome to Python Worlde by Jeiku Dev ]\n")

    numberGuesses = 1
    while numberGuesses <= maxGuesses:
        guess = ""
        while len(guess) != wordLength or not guess.isdecimal():
            print("")
            guess = input("Guess {}: ".format(numberGuesses))

            clues = getClues(guess, secretWord)
            print("Clue: " + clues)
            numberGuesses += 1

        if guess == secretWord:
            break
        if numberGuesses > maxGuesses:
            print(
                "\nYou ran our of guesses\n" + "The Answer was {}.".format(secretWord)
            )

        if not input("\nDo you want to play again? (y/n): ").lower().startswith("y"):
            break
    print("\nThanks for Playing <3.")


def getSecretWord(wordLength):
    response = requests.get(
        "https://random-word-api.vercel.app/api?length={}".format(wordLength)
    )
    if response.status_code == requests.codes.ok:
        secretWord = "".join(ch for ch in response.text if ch.isalnum())
        return secretWord
    else:
        print("Error:", response.status_code, response.text)


def getClues(guess, secretWord):
    if guess == secretWord:
        return "\n\tYou got it!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            clues.append("Letter Found in place!")
        elif guess[i] in secretWord:
            clues.append("Letter Found!")

    if len(clues) == 0:
        return "No Letter Found!"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
