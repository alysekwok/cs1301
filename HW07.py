"""
Georgia Institute of Technology - CS1301
HW07 - File I/0 & CSV
"""
"""
Function Name: findCuisine()
Parameters: filename (str), cuisine (str)
Returns: list of restaurants (list)
"""
def findCuisine(filename, cuisine):
    myfile = open(filename, "r")
    f = myfile.readlines()
    myfile.close()
    newList = []
    finalList = []
    for item in f:
        newStr = item.strip()
        if newStr == "":
            continue
        else:
            newList.append(newStr)
    for x,y in enumerate(newList):
        if y == cuisine:
            restaurant = x- 1
            finalList.append(newList[restaurant])  
    return finalList
            
"""
print(findCuisine('restaurants.txt', 'American'))
print(findCuisine('restaurants.txt', 'NotACuisine'))
"""

"""
Function Name: restaurantFilter()
Parameters: filname (str)
Returns: dictionary that maps cuisine type (str) to a list of
restaurants of the same suisine type (list)
"""
def restaurantFilter(filename):
    myfile = open(filename, "r")
    f = myfile.readlines()
    myfile.close()
    newDict = {}
    newList = []
    finalList = []
    for item in f:
        newStr = item.strip()
        if newStr == "" or newStr == "Sit-down" or newStr =="Fast Food":
            continue
        else:
            newList.append(newStr)
    name = newList[::2]
    cuisine = newList[1::2]
    for x,y in enumerate(cuisine):
        secondList = []
        secondList.append(y)
        secondList.append(name[x])
        newTup = tuple(secondList)
        finalList.append(newTup)
    for value in finalList:
        (typeFood, restName) = value
        if typeFood not in newDict:
            newDict[typeFood] = []
        if restName not in newDict[typeFood]:
            newDict[typeFood].append(restName)
    return newDict
"""
print(restaurantFilter('restaurants.txt'))
"""
"""
Function Name: createDictionary()
Parameters: filename (str), output filename (str)
Returns: None (NoneType)
"""
def createDirectory(fileName, outputName):
    myfile = open(fileName, "r")
    f = myfile.readlines()
    myfile.close()
    newList = []
    newDict = {}
    finalList = []
    for item in f:
        newStr = item.strip()
        if newStr == "":
            continue
        else:
            newList.append(newStr)
    name = newList[::3]
    cuisine = newList[1::3]
    method = newList[2::3]
    for x,y in enumerate(cuisine):
        secondList = []
        secondList.append(y)
        secondList.append(name[x])
        secondList.append(method[x])
        newTup = tuple(secondList)
        finalList.append(newTup)
    for value in finalList:
        (typeFood, restName, method) = value
        if method not in newDict:
            newDict[method] = []
        if restName not in newDict[method]:
            newDict[method].append((restName, typeFood))
    newFile = open(outputName, "w")
    newFile.write("Restaurant Directory\n")
    newFile.write("\nFast Food\n")
    for num, entry in enumerate(sorted(newDict["Fast Food"]),1):
        (restaurantName, restaurantType) = entry
        newFile.write(str(num))
        newFile.write(". " + restaurantName + " - " + restaurantType + "\n")
    newFile.write("\nSit-down")
    for num2, entry2 in enumerate(sorted(newDict["Sit-down"]),1):
        (restaurantName2, restaurantType2) = entry2
        newFile.write("\n")
        newFile.write(str(num2))
        newFile.write(". " + restaurantName2 + " - " + restaurantType2)
    """
    newFile.close()
    finalFile = open(outputName, "r")
    f = finalFile.read()
    print(f)
    finalFile.close()  
createDirectory('restaurants.txt', 'directory.txt')
"""
"""
Function Name: infectedPercentage()
Paramters: country list(list), filename(str)
returns: country and percentage (tuple)
"""

def infectedPercentage(listCountries, fileName):
    myfile = open(fileName, "r")
    f = myfile.readlines()
    myfile.close()
    newList = []
    finalList = []
    temp = 0
    del f[0]
    for item in f:
        newStr = item.strip()
        string = newStr.split(",")
        if string == "":
            continue
        else:
            newList.append(string)
    for entry in newList:
        percentInfected = (int(entry[2])/int(entry[1]))*100
        roundedPercentage = round(percentInfected, 2)
        finalList.append((entry[0], roundedPercentage))
    for country in finalList:
        (name, percentage) = country
        if name in listCountries:
            if percentage > temp:
                temp = percentage
    for country in finalList:
        (name, percentage) = country
        if percentage == temp:
            return (name, percentage)
"""
def infectedPercentage(country_list, filename):
    country_info = open(filename,"r")
    text = country_info.readlines()
    country_info.close
    highest_percentage = 0
    newList = []
    final_tup = ()
    for x in text:
        eachline = x.strip()
        newline = eachline.split(",")
        newList.append(newline)
    for country_name in country_list:
        if country_name in newList:
            percentage = int(eachline[2])/int(eachline[1])
            if percentage > highest_percentage:
                highest_percentage = percentage
                final_country = country_name
                final_tup = (final_country, highest_percentage)
        return final_tup
                              
                                  
"""
print(infectedPercentage(["Belgium", "Belarus", "Bermuda"], 'covid.csv'))
print(infectedPercentage(["Sweden", "Turkey", "Ukraine"], 'covid.csv'))

"""
Function Name: countryStatus()
Parameters: country list (list), filename(str)
Returns: risk dictionary (dict)
"""
def countryStatus(countryList, fileName):
    myfile = open(fileName, "r")
    f = myfile.readlines()
    myfile.close()
    newList = []
    finalList = []
    newDict = {"Low risk": [], "Medium risk": [], "High risk": []}
    del f[0]
    for item in f:
        newStr = item.strip()
        string = newStr.split(",")
        if string == "":
            continue
        else:
            newList.append(string)
    for entry in newList:
        percentInfected = (int(entry[2])/int(entry[1]))*100
        roundedPercentage = round(percentInfected, 2)
        finalList.append((entry[0], roundedPercentage))
    for country in finalList:
        (name, percentage) = country
        if name in countryList:
            if percentage <= 25:
                newDict["Low risk"].append(name)
            if 25 < percentage <= 65:
                newDict["Medium risk"].append(name)
            if percentage > 65:
                newDict["High risk"].append(name)
    return newDict
"""
countryList = ["United States", "Tonga", "Poland", "New Zealand", "Norway"]
print(countryStatus(countryList, 'covid.csv'))
countryList = ["Belgium", "Bangladesh", "Belarus", "Bermuda"]
print(countryStatus(countryList, 'covid.csv'))
"""      
        
"""
Function Name: compareRisk()
Parameters: country to compare (str), country list (list),
filename(str)
Returns: compared countries (list)
"""
def compareRisk(countryToCompare, countryList, fileName):
    myfile = open(fileName, "r")
    f = myfile.readlines()
    myfile.close()
    newList = []
    finalList = []
    compare = []
    returnValue = []
    del f[0]
    for item in f:
        newStr = item.strip()
        string = newStr.split(",")
        print(string)
        if string == "":
            continue
        else:
            newList.append(string)
    for entry in newList:
        newPop = int(entry[1])
        newInf = int(entry[2])
        finalList.append((entry[0], newPop, newInf))
    for value in finalList:
        (name, population, infected) = value
        if name == countryToCompare:
            compare.append(value)
    for country in finalList:
        (name, population, infected) = country
        if name in countryList:
            if population < compare[0][1]:
                if infected > compare[0][2]:
                    returnValue.append(name)
    if returnValue == []:
        return "No countries"
    else:
        return returnValue

countryList = ["Belgium", "Bangladesh", "Belarus", "Bermuda"]
print(compareRisk("Tunisia", countryList, 'covid.csv'))
countryList = ["Turkmenistan", "Norway", "Netherlands", "Philippines"]
print(compareRisk("Tuvalu", countryList, 'covid.csv'))

