"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
"""
"""
Function Name: vowelCounter()
Parameters: cities (list)
Returns: number of vowels in each city (dict)
"""
def vowelCounter(cities):
    cityVowels = {}
    for city in cities:
        vowels = 0
        for letter in city:
            if letter in "aeiouAEIOU":
                cityVowels[city] = cityVowels.get(city, 0) + 1
            else:
                cityVowels[city] = cityVowels.get(city, 0)
    return cityVowels
"""
cities = (['DXB', 'HND', 'LHR', 'BKK', 'CDG'])
print(vowelCounter(cities))
cities = ["Atlanta", "New York", "Boston", "Los Angeles"]
print(vowelCounter(cities))
cities = ["Whoville", "Thneedville", "Mount Crumpit"]
print(vowelCounter(cities))
"""

"""
Function Name: maskDetector()
Parameters: message (list)
Returns: tuple with the location of the mask (str) and the number of errors (int)
"""
def maskDetector(message):
    location = ""
    numErrors = 0
    for value in message:
        try:
            type(value) == str
            location += value
        except:
            numErrors += 1
    return (location, numErrors)
"""
message = [6, 'S', {}, 'wee', ('a',), 't', 31, ' ', ['hello'], 'H', 7, 'ut']
print(maskDetector(message))
message = [None, 32, 'P', 6, [], 'ub', 12, 'l', 6, 'ix']
print(maskDetector(message))
""" 

"""
Function Name: beautifulDay()
Parameters: dictionary of cities mapped to list of tuples (dict),
ideal weather (str), ideal temperature (int)
Returns: a list of places (list)
"""
def beautifulDay(dictCities, idealWeather, idealTemp):
    places = []
    for (key, value) in dictCities.items():
        for x in value:
            if x[0] == idealWeather and x[1] <= idealTemp <= x[2]:
                if key in places:
                    continue
                else:
                    places.append(key)
    sortPlaces = sorted(places)
    return sortPlaces
          
"""
weatherDict = {'Whoville':[('sunny', 75, 90),('snow', 28, 43),('rain', 65, 72)],
               'Mount Crumpit':[('cloudy', 68, 75), ('sunny', 54, 69), ('sunny', 66, 77)],
               'Thneedville':[('sunny', 70, 77), ('cloudy', 65, 75), ('sunny', 68, 74)] }
print(beautifulDay(weatherDict, 'sunny', 71))

weatherDict = {'Bikini Bottom':[('stormy', 65, 84),('stormy', 62, 74)],
               'Rock Bottom':[('sunny', 81, 90), ('partially cloudy', 65, 70)],
               'Jellyfish Fields':[('partially cloudy', 64, 83), ('rain', 65, 71)],
               'Tentacle Acres':[('partially cloudy', 64, 69), ('sunny', 50, 54)]}
print(beautifulDay(weatherDict, 'partially cloudy', 68))
"""

"""
Function Name: flightFinder()
Parameters: flight prices by month for different cities (dict), city (str)
Returns: the month with the cheapest flight to the customer's desired
city (str) or None
"""

def flightFinder(flightInfo, city):
    temp = 999999999999999999999999999
    month = ""
    for (key, value) in flightInfo.items():
        if key == city:
            if value == {}:
                return "No Flights"
            else:
                for x,y in value.items():
                    if y < temp:
                        temp = y
                        month = x
            return month
    if city not in flightInfo.items():
        return "No Flights"
"""

flightInfo = ( {'Lima': {'March': 250, 'June': 444, 'November': 777},
                'Nairobi': {'September': 276}})
print(flightFinder(flightInfo, "Lima"))



flightInfo = {'Boston': {'January': 100, 'March': 200},
              'Denver': {'January': 125},
              'San Francisco': {'August': 350, 'December': 125}    }
city = 'San Francisco'
print(flightFinder(flightInfo, city))

flightInfo = {'London': {'July': 430, 'April': 222},
              'Tokyo': {},
              'Perth': {'May': 989}    }
city = 'Tokyo'
print(flightFinder(flightInfo, city))
"""
"""
Function Name: courseRosters()
Parameters: student info as a list of tuples (list)
Returns: a dictionary containing course rosters (dict)
"""
def courseRosters(students):
    roster = {}
    for (name, major, schedule) in students:
        for course in schedule:
            if course not in roster:
                roster[course] = {}
            if major not in roster[course]:
                roster[course][major] = []
            if name not in roster[course][major]:
                roster[course][major].append(name)
    return roster
        
"""
students = [("Sarah","CS", ["CS1301","PHYS2211", "PSYC1101"]),
            ("Megan", "ISyE", ["PHYS2211", "MATH1553", "ENGL1102"]),
            ("Kirtana", "CS", ["CS1301", "MATH1553", "CS1100", "PSYC1101"]),
            ("Grace", "Business", ["ENGL1102", "PSYC1101"])]
print(courseRosters(students))
""" 
    
    
