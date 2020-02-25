#aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    lista = []
    for i in aList:
        if len(i)<4:
            lista.append(i)
    return lista
print(lessThan4(["apple", "cat", "dog", "banana"]))