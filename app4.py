import string
def getAvailableLetters(lettersGuessed):
    lista=[]
    # FILL IN YOUR CODE HERE...
    for i in string.ascii_lowercase:
        lista.append(i)
        for k in lettersGuessed:

            if i==k:
                del lista[-1]
    lista2=""
    for m in lista:
        lista2+=m
    return lista2

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
