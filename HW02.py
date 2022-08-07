"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""
#########################################
"""
Function Name: skillLevel()
Parameters: passRate (int)
Returns: "Beginner" or "Moderate" or "Advanced" (str)
"""
def skillLevel(passRate):
    if passRate <= 25:
        return "Beginner"
    elif passRate > 25 and passRate <= 75:
        return "Moderate"
    else:
        return "Advanced"
"""
print (skillLevel(20))
print (skillLevel(69))
print (skillLevel(97))
"""

#########################################
"""
Function Name: bookStore()
Parameters: item (str), walletAmount (float), quantity (int)
Returns: moneyLeftOver (float)
"""
def bookStore(item, walletAmount, quantity):
    if item == "Shirt":
        cost = 15.50
    elif item =="Lanyard":
        cost = 4.25
    elif item == "Sweatshirt":
        cost = 25.00
    else:
        cost = 10.50
    totalCost = cost * quantity
    roundCost = round(totalCost, 2)
    moneyLeftOver = round((walletAmount - roundCost), 2)
    if walletAmount >= roundCost:
        return moneyLeftOver
    else:
        return "Not enough money!"

# print(bookStore("Lanyard", 200.0, 70))


#########################################
"""
Function Name: dinnerPlans()
Parameters: distance (int), hungerLevel(str)
Returns: transportMode (str)
"""
def dinnerPlans(distance, hungerLevel):
    if hungerLevel == "Not Hungry" and distance <= 7:
        transportMode = "Walk"
    elif hungerLevel == "Slightly Hungry" and distance <= 5:
        transportMode = "Walk"
    elif hungerLevel == "Hungry" and distance <= 3:
        transportMode = "Walk"
    elif hungerLevel == "Very Hungry" and distance <= 1:
        transportMode = "Walk"
    elif hungerLevel == "Not Hungry" and distance > 7:
        transportMode = "Uber"
    elif hungerLevel == "Slightly Hungry" and distance > 5:
        transportMode = "Uber"
    elif hungerLevel == "Hungry" and distance > 3:
        transportMode = "Uber"
    elif hungerLevel == "Very Hungry" and distance > 1:
        transportMode = "Uber"
    else:
        transportMode = "Uber"
    return transportMode

# print (dinnerPlans(4, "Slightly Hungry"))
 
    

#########################################
"""
Function Name: weekendTrip()
Parameters: distance (float), speed (float), freeTime (float)
returns: transportMode (str)
"""
def weekendTrip(distance, speed, freeTime):
    travelTime = distance / speed
    percentOfFreeTime = travelTime / freeTime
    if percentOfFreeTime >= .20:
        transportMode = "Going to this destination would take too much time."
    else:
        if 2.5 <= speed <= 15 and percentOfFreeTime <= .20:
            transportMode = "walking"
        elif 15 < speed <= 20 and percentOfFreeTime <= .20 :
            transportMode = "biking"
        elif 20 < speed and percentOfFreeTime <= .20 :
            transportMode = "driving"
    return transportMode

# print (weekendTrip(7.0, 46.66, 1.0))


#########################################
"""
Function Name: textFriends()
Parameters: distance (float), speed (float), freeTime(float), numSnacks (int),
numFriends (int)
Returns: textMsg (str)
"""
def textFriends(distance, speed, freeTime, numSnacks, numFriends):
    returnValue = weekendTrip(distance, speed, freeTime)
    snacksPerPerson = numSnacks // numFriends
    leftOverSnacks = numSnacks % numFriends
    if returnValue == "walking":
        textMsg = ("If each of us gets {} snack(s), there will be {} left. I will be walking, who else is doing the same?".format(snacksPerPerson,leftOverSnacks))
    elif returnValue == "biking":
        textMsg = ("If each of us gets {} snack(s), there will be {} left. I will be biking, who else is doing the same?".format(snacksPerPerson,leftOverSnacks))
    elif returnValue == "driving":
        textMsg = ("If each of us gets {} snack(s), there will be {} left. I will be driving, who else is doing the same?".format(snacksPerPerson,leftOverSnacks))
    else:
        textMsg = "Going to this destination would take too much time."
    return textMsg

# print (textFriends (1.5, 2.5 , 3.0, 13, 7))
