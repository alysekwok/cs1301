"""
Georgia Institute of Technology - CS1301
HW08 - APIs
"""
import requests
"""
Function Name: meetNewPeople()
Parameters: house (str)
Returns: list of people (list)
"""
def meetNewPeople(house):
    apiKey = "$2a$10$C9yOz9bJ71sNKG/D0ZgBj.2rsxNTQIOpz6iQu5uy66pKtWPpG2J2G"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters" + "?key=" +apiKey + "&house=" + house + "&bloodStatus=pure-blood&deathEater=false"
    r = requests.get(url)
    print(r.json)
    nameList =[]
    for value in r.json():
        nameList.append(value["name"])
    return nameList
     
print(meetNewPeople("Slytherin"))
print(meetNewPeople("Hufflepuff"))
print(meetNewPeople("Ravenclaw"))
print(meetNewPeople("Gryffindor"))
  
"""
Function Name: matchingStudents()
Parameters: character name (str)
Returns: list of students (list)
"""
def matchingStudents(characterName):
    apiKey = "$2a$10$C9yOz9bJ71sNKG/D0ZgBj.2rsxNTQIOpz6iQu5uy66pKtWPpG2J2G"
    baseUrl = "https://www.potterapi.com/v1/"
    url = baseUrl + "characters?key=" + apiKey + "&name=" + characterName
    r = requests.get(url)
    jsonVersion = r.json()
    char = []
    listCharacters = []
    for entry in jsonVersion:
        char.append(entry["bloodStatus"])
        char.append(entry["house"])
    newUrl = baseUrl + "characters?key=" + apiKey + "&role=student" + "&bloodStatus=" + char[0]+ "&house=" + char[1]
    x = requests.get(newUrl)
    xjson = x.json()
    for value in xjson:
        if value["name"] == characterName:
            continue
        else:
            listCharacters.append(value["name"])
    return listCharacters

"""
print(matchingStudents("Albus Dumbledore"))
print(matchingStudents("Amelia Bones"))
"""
    
"""
Function Name: similarCharacters()
Parameters: movieID1 (str), movieID2 (str)
Returns: number of people (int)
"""
def similarCharacters(movieID1, movieID2):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "films/" + movieID1 + "/"
    r = requests.get(url)
    rjson = r.json()
    url2 = baseUrl + "films/" + movieID2 + "/"
    r2 = requests.get(url2)
    r2json = r2.json()
    numPeople = 0
    try:
        movie1 = rjson["characters"]
        movie2 = r2json["characters"]
        for char in movie1:
            if char in movie2:
                numPeople += 1
    except:
        numPeople = 0
    return numPeople

"""
print(similarCharacters('1', '2'))
print(similarCharacters('1', '7'))
"""
"""
Function Name: spaceDrifting()
Parameters: passengers(int), max price(int)
Returns: list of valid starships (list)
"""
def spaceDrifting(passengers, maxprice):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "starships/"
    r = requests.get(url)
    rjson = r.json()
    newList = []
    for ship in rjson["results"]:
        try:
            if int(ship["passengers"]) >= passengers:
                if int(ship["cost_in_credits"]) < maxprice:
                    newList.append((ship["name"], ship["manufacturer"]))
        except:
            continue
    return newList
                    
"""
print(spaceDrifting(4, 350000))
print(spaceDrifting(0, 1000000))
"""    

"""
Function Name: perfectMatch()
Parameters: list of candidates (list)
Returns: list of potential matches (list)
"""
def perfectMatch(candidates):
    baseUrl = "https://swapi.dev/api/"
    url = baseUrl + "people/"
    r = requests.get(url)
    rjson = r.json()
    listPeople = []
    for person in rjson["results"]:
        if person["name"] == "Luke Skywalker":
            continue
        if person["name"] == "Darth Vader":
            continue
        try:
            if person["name"] in candidates:
                if int(person["height"]) >= 180:
                   if person["gender"] == "male":
                       listPeople.append(person["name"])
        except:
            continue
    sortList = sorted(listPeople)
    return sortList
"""
print(perfectMatch(["C-3PO", "Darth Vader", "Biggs Darklighter"]))
print(perfectMatch(["Luke Skywalker", "Leia Organa"]))
"""
               
               
