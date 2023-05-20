import requests

wordLength = 3

def main():
    print("\n[ Welcome to Python Worlde by Jeiku Dev ]\n")
    
    while True:
        return print('huhu')

    
    
def getSecretWord(wordLength):
    response = requests.get('https://random-word-api.vercel.app/api?length={}'.format(wordLength))
    if response.status_code == requests.codes.ok:
        secretWord = "".join(ch for ch in response.text if ch.isalnum())
        return secretWord
    else:
        print("Error:", response.status_code, response.text)


def getClues(guess, secretWord):
    if guess == secretWord:
        return '\n\tYou got it!!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretWord[i]:
            clues.append('Letter Found in place!')
        elif guess[i] in secretWord[i]:
            clues.append('Letter Found!')
            
    if len(clues) == 0:
        return 'No Letter Found!'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
