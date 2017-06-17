
def dictionaryV2(x, y):
    a = x
    b = y
    if len(y)>len(x):
        a = y
        b = x

    d = {}
    for i in range(0, len(x)):
        key = a[i]
        value = b[i]
        d[key] = value

    print d


dictionaryV2(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],
            ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "penguins"])
