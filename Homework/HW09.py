"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""
"""
Function Name: pickyEater()
Parameters: food list (list)
Returns: number of food items that can be eaten (int)
"""
def pickyEater(foodList):
    if len(foodList) <= 0:
        return 0
    else:
        if len(foodList[0])%2 == 1:
            return pickyEater(foodList[1:])
        if len(foodList[0]) == 0:
            return pickyEater(foodList[1:])
        else:
            return 1 + pickyEater(foodList[1:])
""" 
print(pickyEater(["Apple Pie", "Turkey", "Cranberry Sauce", "Mac and cheese"]))
print(pickyEater(["Pumpkin Pie", "Casserole", "Mashed Potato", "Pecan Pie"]))
"""
"""
Function Name: inviteFriends()
Parameters: list of invitees (list)
Returns: flattened list of all invitees (list)
"""
def inviteFriends(inviteList):
    if len(inviteList) <= 0:
        return []
    if inviteList[0] == []:
        return inviteFriends(inviteList[1:])
    if type(inviteList[0]) == list:
        if type(inviteList[0][0]) == list:
            alist = inviteFriends(inviteList[0][0])+ inviteFriends(inviteList[0][1:]) + inviteFriends(inviteList[1:])
            return alist
        else:
            alist = inviteFriends(inviteList[0][1:])
            alist.insert(0, inviteList[0][0])
            if len(inviteList[1:]) > 0:
                alist += inviteFriends(inviteList[1:])
            return alist
    if type(inviteList[0]) == str:
        alist = (inviteFriends(inviteList[1:]))
        alist.insert(0, inviteList[0])
        return alist
"""
print(inviteFriends([[['Spongebob']],[['Patrick'],'Plankton', [], []]]))


friendsList = ['Parul','Megan',
               ['Arvin', 'Anthony', 'Arushi', ['Jasmine', 'Josh', 'Yara']]]
print(inviteFriends(friendsList))

friendsList = ['Alexa',     [],
               ['Craig', 'Michael', 'Rajit'],
               ['Jakob', 'Damian']   ]
print(inviteFriends(friendsList))
"""

"""
Function Name: friendsgiving()
Parameters: stores (list), budget (float), maxDistance (int)
Returns: price of sauce at each store (dict)
"""
def friendsgiving(stores, budget, maxDistance):
    if len(stores) == 0:
        return {}
    else:
        if stores[0][1] < budget and stores[0][2] < maxDistance:
            newdict = friendsgiving(stores[1:], budget, maxDistance)
            newdict[stores[0][0]] = stores[0][1]
            return newdict
        else:
            return friendsgiving(stores[1:], budget, maxDistance)
    
"""
stores = [('Whole Foods', 2.79, 4), ('Kroger', 6.99, 5)]
budget = 4.99
maxDistance = 6
print(friendsgiving(stores, budget, maxDistance))

stores = [        ('Sprouts', 3.45, 2),
                  ('ALDI', 3.69, 6),
                  ('Walgreens', 1.99, 1),
                  ('Kroger', 2.79, 4)    ]
budget = 3.50
maxDistance = 5
print(friendsgiving(stores, budget, maxDistance))
"""

"""
Function Name: palindrome()
Parameters: string (str), guess (int)
Returns: Whether the string contains a number of palindromes (bool)
"""

def palindrome(string, guess):
    if len(string) == 0:
        if guess == 0:
            return True
        else:
            return False
    else:
        if string == string[::-1]:
            string = ""
            return palindrome(string, guess-1)
        if string[0:3] == string[0:3:-1]:
            return palindrome(string[1:], guess-1)
        else:
            return palindrome(string[1:], guess)
"""
print(palindrome('arvin was here', 0))

palinstring = "tacocat"
print(palindrome(palinstring, 1))

palinstring = "cdecec"
print(palindrome(palinstring, 3))
"""
"""
   if type(inviteList[0][0]) == list:
        alist = (inviteFriends(inviteList[0][0][1:]))
        print(alist)
        alist.insert(0, inviteList[0][0][0])
        return alist
"""
