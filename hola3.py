def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return print(result)

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, max, int], -3)