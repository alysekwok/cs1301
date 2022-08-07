"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""
import calendar
"""
Function Name: maskOrders()
Parameters: list organizations (list), list of members (list), mask price (int)
Returns: list of tuples (list)
"""
def maskOrders(listOrgs, numMems, maskPrice):
    totalCost = []
    for num in numMems:
        maskTotal = maskPrice * num
        totalCost.append(maskTotal) 
    tupList = []
    for org in listOrgs:
        cost = listOrgs.index(org)
        tup = (org, totalCost[cost])
        tupList.append(tup)
    return tupList
"""
organizations = ["FTK", "Soccer", "SCPC"]
members = [200, 50, 100]
print(maskOrders(organizations, members, 2))
"""

"""
Function Name: coffeeBreak()
Parameters: list of drinks (list), budget (float)
Returns: name of drink (str)
"""
def coffeeBreak(listDrinks, budget):
    nameDrink = ""
    caffiene = 0
    for tup in listDrinks:
        if tup[2] <= budget:
            if tup[1] >= caffiene:
                nameDrink = tup[0]
                caffiene = tup[1]
    if nameDrink == "":
        return None
    return nameDrink

"""
drinks = [  ("Frappuchino", 20, 3.5),
            ("Dark Roast", 35, 4.0),
            ("Espresso", 75, 5.5) ]
budget = 5.0
print(coffeeBreak(drinks, budget))

drinks = [
    ("Cold Brew", 50, 5.0),
    ("Dark Roast", 35, 4.0),
    ("Green Tea", 30, 3.5)    ]
budget = 4.0
print(coffeeBreak(drinks, budget))
"""

"""
Function Name: myBirthday()
Parameters: gifts (list)
Returns: total balance and gifts (tuple)
"""
def conversion(money):
    if type(money) == str:
        return float(money[1:])
    else:
        if type(money) == int:
            return '$' + str(money) + '.00'
        else:
            return '$' + str(money) + '0' * (2 - len(str(money).split('.')[1]))

def myBirthday(gifts):
    totalBal = 0
    otherGifts = []
    for x in gifts:
        if "$" in x:
            money = conversion(x)
            totalBal += money
        else:
            otherGifts.append(x)
    convertedTotal = conversion(totalBal)
    finalBalance = (convertedTotal,)
    return tuple(finalBalance + tuple(otherGifts))
"""
gifts = ["$25.0", "$10.0", "iPhone", "$35.50", "$2.50", "$20.0"]
print(myBirthday(gifts))

gifts = ["$0.05", "Xbox", "Socks", "$100.0"]
print(myBirthday(gifts))
"""

"""
Function Name: roadTrip()
Parameters: state (str), list of tuples (list)
Returns: list of cities (list)
"""
def roadTrip(state, cities):
    listCities = []
    for tup in cities:
        (city, cityState) = tup
        if cityState == state:
            if city in listCities:
                continue
            else:
                listCities.append(city)
    return listCities
"""
state = "GA"
cities = [
    ("Atlanta", "GA"),
    ("Charleston", "SC"),
    ("Macon", "GA")    ]
print(roadTrip(state, cities))
state = "CO"
cities = [
    ("Vail", "CO"),
    ("Denver", "CO"),
    ("Nashville", "TN"),
    ("Fort Collins", "CO")    ]
print(roadTrip(state, cities))

state = "AK"
cities= [
    ("Skagway", "AK"),
    ("Juneau","AK"),
    ("Boise", "ID"),
    ("Juneau","AK")]
print(roadTrip(state, cities))
"""
"""
Function Name: safeLocation()
Parameters: list of tuples (list)
Returns: safe locations (list)
"""
def safeLocation(location):
    safePlaces = []
    for tup in location:
        (room, current, total) = tup
        safeCap = total // 2
        if current == total:
            continue
        if current <= safeCap:
            safePlaces.append(room)
    return safePlaces
"""
places = [
    ("Jakob's Room", 25, 30),
    ("Help Desk", 100, 100),
    ("West Village", 20, 200),
    ("CRC", 50, 250)    ]
print(safeLocation(places))
places = [
    ("Movie Theater", 2, 200),
    ("Grocery Store", 100, 150),
    ("Sublime Donuts", 20, 20)    ]
print(safeLocation(places))
"""
"""
Function Name: eventScheduler()
Parameters: list of tuples (list)
Returns: events (list)
"""
def eventScheduler(events):
    listEvents = []
    for eventDay in events:
        (eventName, month, day) = eventDay
        dayofWeek = calendar.weekday(2020, month, day)
        if dayofWeek == 5 or dayofWeek == 6:
            listEvents.append(eventName)
    return listEvents
"""
events = [
    ("Kirtana's Birthday", 11, 16),
    ("Drake Album Drop", 12, 26),
    ("Fyre Festival", 10, 10)    ]
print(eventScheduler(events))

events = [
    ("Arvin & Anthony teach lecture", 10, 18),
    ("NBA Finals Game 7", 10, 13),
    ("Crossfit Games", 9, 25)    ]
print(eventScheduler(events))
"""
