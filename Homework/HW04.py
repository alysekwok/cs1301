"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing, and Lists
"""
#########################################
"""
Function Name: findMax()
Parameters: a captions list of numbers (list), start index (int), stop index (int)
Returns: highest number (int)
"""
def findMax(numList, startIndex, stopIndex):
    temp = numList[startIndex]
    for num in numList[startIndex:stopIndex + 1]:
        if num > temp:
            temp = num
    return temp
print(findMax([1, 8,3,2,-4], 2, 4))
print(findMax([3, 0, 7, 3, 2], 0, 4))

#########################################
"""
Function Name: fruitPie()
Parameters: list of fruits (list), minimum quantity (int)
Returns: list of fruits (list)
"""
def fruitPie(fruits, minQuantity):
    fruitType = fruits[::2]
    amtFruit = fruits[1::2]
    listOfFruits = []
    for x in range(len(amtFruit)):
        if amtFruit[x] >= minQuantity:
            listOfFruits.append(fruitType[x])
    return listOfFruits
"""

print(fruitPie(["rambutan", 1, "blackberry", 2, "lychee", 2], 1))

print(fruitPie(["apple", 2, "cherry", 10, "watermelon", 5], 4))
print(fruitPie(["peach", 55, "orange", 32, "pineapple", 2], 50))
"""

#########################################
"""
Function Name: replaceWord()
Parameters: initial sentence (str), replacement word (str)
Returns: corrected sentence (str)
"""
def replaceWord(sentence, replacement):
    splitSentence = sentence.split()
    correctSentence = ""
    for item in splitSentence:
        if len(item) >= 5:
            correctSentence += (replacement + " ")
        else:
           correctSentence += (item + " ")
    correctSentence = correctSentence.strip()
    return correctSentence

"""    
print(replaceWord("I used to rule the world","seas"))
print(replaceWord("I miss the old Kanye","coding"))
"""
    
#########################################
"""
Function Name: highestSum()
Parameters: list of strings (strings)
Returns: index of string with the highest sum (int)
"""

def highestSum(listStrings):
    newList = []
    valString = 0
    num = "0123456789"
    for x in listStrings:
        subList = 0
        for y in x:
            if y in num:
                subList += int(y)
        newList.append(subList)
    positionSum = newList.index(max(newList))
    return positionSum
"""    
myList = ["3lf", "bg_73e", "001!0", "gg9./"]
print(highestSum(myList))

myList = ["py1h0n", "1s", "v3ry", "fun!!11!!!111"]
print(highestSum(myList))
"""

#########################################
"""
Function: sublist()
Parameters: alist (list), blist (list)
Returns: True or False (`boolean`)
"""
def sublist(alist, blist):
    if len(alist) < len(blist):
        alist, blist = blist, alist
    listRange = (len(blist))
    startIndex = 0
    for x in range(len(alist)):
        #for y in alist[startIndex:listRange]:
            if blist == alist[startIndex:listRange]:
                return True
            if listRange < len(alist)+1:
                startIndex += 1
                listRange += 1
    if alist == []:
        return True
    if blist == []:
        return True
    return False


alist = [6, 2, 3, 4, 5]
blist = [6, 3]
print(sublist(alist, blist))

alist = ['a', 'b', 'd', 'e', 't']
blist = ['b', 'd', 'e']
print(sublist(alist, blist))

alist = ["The", "Houston", "Astros", "are", "cheaters"]
blist = ["The", "Houston", "Astros", "are", "cheaters"]
print(sublist(alist,blist))


"""

def sublist(alist, blist):
    if len(alist) < len(blist):
        alist, blist = blist, alist
    for x in range(len(alist) - len(blist) + 1):
        if blist == alist[x:len(blist)+1]:
            return True
    if len(alist) == 0 or len(blist) == 0:
        return True
    return False
alist = [6, 2, 3, 4, 5]
blist = [6, 3]
print(sublist(alist, blist))

alist = ['a', 'b', 'd', 'e', 't']
blist = ['b', 'd', 'e']
print(sublist(alist, blist))

alist = ["The", "Houston", "Astros", "are", "cheaters"]
blist = ["The", "Houston", "Astros", "are", "cheaters"]
print(sublist(alist,blist))
"""
