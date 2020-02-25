def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    dictio=[]
    val = aDict.values()
    myset=set(val)

    for i,j in aDict.items():
        if j in myset:
            dictio.append(i)
    return dictio

aDict={1:1, 3:2, 4:5, 6:2}
#val=aDict.values()
print(uniqueValues(aDict))
