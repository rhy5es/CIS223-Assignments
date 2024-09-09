"""
code to reverse a string
"""
def stringReverse(string):
    stringList = stringToList(string) #converts to mutable list
    reverseList = []
    return ''.join(stringReverseHelper(stringList, reverseList))


def stringToList(string):
    stringList = []
    for letter in string:
        stringList.append(letter)
    return stringList

def stringReverseHelper(stringList, reverseList):
    if len(stringList) == 0:
        return reverseList
    else:
        reverseList.append(stringList[len(stringList) - 1])
        stringList.pop()

        return stringReverseHelper(stringList, reverseList)
    
print(stringReverse("pots&pans"))

