import numpy as np
def checkPlindrome():
    name = "madam"
    newString = ''
    Larray = np.array(list(name))
    x = 0
    for i in range(len(Larray)-1):
        if i != len(Larray)-1-x:
            temp = Larray[i]
            Larray[i] = Larray[len(Larray)-1-x]
            Larray[len(Larray) - 1 - x] = temp
        x = x + 1
    for i in range(len(Larray)):
        newString = newString+Larray[i]




checkPlindrome()