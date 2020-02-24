
def getGuessedWord(secretWord, lettersGuessed):

    # FILL IN YOUR CODE HERE...
    lista=""
    for i in secretWord:
        lista2=""
        for k in lettersGuessed:

            if i==k:
                lista+=i
                lista2+=i

        if lista2=="":
            lista+="_"

    return lista

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
