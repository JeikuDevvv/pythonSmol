import requests

wordLength = 5


def main():
    secretWord = getSecretWord()
    print(secretWord)


def getSecretWord():
    response = requests.get('https://random-word-api.vercel.app/api?length={}'.format(wordLength))
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)
        
        
if __name__ == '__main__':
    main()
    
    

