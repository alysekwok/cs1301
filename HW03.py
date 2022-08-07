0"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""
import math
#########################################
"""
Function Name: movieNight()
Paramters: a caption (str)
Returns: the fixed caption (str)
"""
def movieNight(caption):
    number = "1234567890"
    fixedCaption = ""
    for ch in caption:
        if ch in number:
            continue
        else:
            fixedCaption += ch
    return fixedCaption

# print(movieNight("Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much."))  
#########################################
"""
Function Name: iceCream()
Parameters: flavor (str), number of vowels (int)
Returns: a sentence (str)
"""
def iceCream(flavor, numVowels):
    vowel = "aeiou"
    newFlavor = flavor.lower()
    numVowelsInFlavor = 0
    for letter in flavor:
        if letter in vowel:
            numVowelsInFlavor += 1
    if numVowelsInFlavor >= numVowels:
        return "Yes, {} ice cream has more than {} vowels!".format(newFlavor, numVowels)
    if numVowelsInFlavor < numVowels:
        return "No, {} ice cream doesn't have more than {} vowels!".format(newFlavor, numVowels)
"""
print(iceCream("ChoCoLaTe", 3))
print(iceCream("strawBERRY", 2))
print(iceCream("vaNillA",2))
"""

#########################################
"""
Function Name: dreamCar()
Parameters: car price (float), bank balance (float),
interest rate (float)
Returns: number of years (int)
"""

def dreamCar(carPrice, bankBalance, interestRate): # IR formula: A = P(1+r/n)^nt
    # solve for t = (log(A/P))/(log(1+r))
    r = interestRate / 100
    time = math.log(carPrice/bankBalance)//math.log(1+r)
    return math.ceil(time + 1)
"""
print(dreamCar(50000.0,10000.0, 5.0))   
print(dreamCar(100000.0, 112.15, 2.1))  
"""
    
#########################################
"""
Function Name: battleship()
Parameters: board size (int)
Returns: None (NoneType)
"""

def battleship(boardSize):
    letter = "abcdefghijklmnopqrstuvwxyz"
    for x in range(boardSize):
        s = ""
        for y in range(boardSize):
            s += str(letter[x]+str(y+1)+ " ")
        s = s.strip()
        print(s)
        
# battleship(3)

#########################################
"""
Function: tennisMatch()
Paramters: player 1 (str), player 2 (str), match record (str)
Returns: winner (str)
"""
def tennisMatch(player1, player2, matchRecord):
    score1 = 0
    score2 = 0
    match1 = 0
    match2 = 0
    score = matchRecord.split("-")
    for game in score:
        for x in game:
            if x == str(1):
                score1 += 1
            if x == str(2):
                score2 += 1
        print(score1)
        print(score2)
        print("")
        if score1 > score2:
            match1 += 1
        if score1 < score2:
            match2 += 1
        score1 = 0
        score2 = 0
    if match1 > match2:
        return "{} won! The score was {}-{}.".format(player1, match1, match2)
    if match1 < match2:
        return "{} won! The score was {}={}.".format(player2, match1, match2)
    else:
        return "It's a tie!"

# print(tennisMatch("Arvin", "Arushi", "11221-222-1111-11121-22111-"))
        
        
    
