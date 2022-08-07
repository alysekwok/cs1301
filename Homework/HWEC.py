"""
Georgia Institute of Technology - CS1301
HWEC - Extra Credit Problems
"""
"""
Function Name: validParentheses()
Parameters: a string with parentheses (str)
Returns: valid or not (bool)
"""
def validParentheses(string):
    alist = []
    for x in string:
        if x == "[":
            alist.append(x)
        if x == "(":
            alist.append(x)
        if x == ")":
            alist.append(x)
        if x == "]":
            alist.append(x)
    if alist[0] == "(":
        if alist[1] == "]":
            return False
        else:
            for z in alist[1::2]:
                if z == "]":
                    return False
    if alist[0] == "[":
        if alist[1] == ")":
            return False
        else:
            for z in alist[1::2]:
                if z == ")":
                    return False            
    return True
"""
print(validParentheses("[('peter', 'han'), ('colin', 'tam')]" ))
print(validParentheses("[3, 2, (1])"))
"""
"""
for num in range(9):
    if num +1== 2:
        print("two!")
    elif num == 3:
        print("san")
    if num / 1 == 1:
        break

def traceMe(param):
    if param[-1] == param[1]:
        print("doot")
    elif param[:3]==param[2:5]:
        print("dat")
    else:
        pass
traceMe("ahahaha")
"""
"""
b = 2
for a in range(4):
    if a == b + 1:
        print(a)
    elif 1 -2 == b:
        print(a)
    else:
        pass
"""
"""
def doThings(stuff):
    for i in stuff:
        if i % 5 == 4:
            print("ay")
        elif i % 6 == 2 and i - 4 % 6 == 4:
            print("hey")
        if i % 8 == 0:
            return 3
stuff = [1,8,9]
doThings(stuff)
"""
"""
aTup = ()
y = 6
x = 10
while y <= x:
    if x % y == 0:
        y += 2
        aTup += y,
    elif x // y == 1:
        print(y)
        y += 4
        aTup += y,
    else:
        y += 1

print(aTup)
"""

item1 = [1, 3, [1, 4]]
item2 = item1[:]
item2[2][1] = "blop"
item3 = [1,2]
item1.append(item3)
print(item1)
print(item2)
print(item3)
"""
aTup = (1, 21, 30, 5)
count = 5
for i in aTup:
    for x in range(i):
        count += 1
print(count)
"""
"""
Function Name: bubbleSort()
Parameters: a list (list), the list's length (int)
Returns: None (NoneType)
"""
def bubbleSort(alist, length):
    pass
"""
Function Name: groupAnagrams()
Parameters: list of strings (list)
Returns: grouped anagrams (dict)
"""
def groupAnagrams(liststr):
    pass
"""
Problem Name: Winter Break
"""
class Friend:
    def __init__(self):
        pass
class Planner:
    def __init__(self):
        pass
