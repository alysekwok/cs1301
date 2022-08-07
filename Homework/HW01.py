"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: listen()
Parameters: N/A
Returns: None
"""
def listen():
    amtSongs = int(input("How many songs did you listen to? "))
    amtPodcasts = int(input("How many podcasts did you listen to? "))
    lengthSongs = amtSongs * 3
    lengthPodcasts = amtPodcasts * 25
    totalHours = (lengthSongs + lengthPodcasts)//60
    remainingMinutes = (lengthSongs + lengthPodcasts)%60
    print (("By listening to {} songs and {} podcasts, you have spent {} hours and {} minutes on Spotify.").format(amtSongs, amtPodcasts, totalHours, remainingMinutes))
listen()

#########################################

"""
Function Name: dominosTime()
Parameters: N/A
Returns: None
"""
def dominosTime():
    amtPizzas = int(input("How many pizzas do you want?"))
    amtPasta = int(input("How many orders of pasta do you want?"))
    amtChicken = int(input("How many orders of chicken wings do you want?"))
    costPizza = amtPizzas * 12
    costPasta = amtPasta * 6
    costChicken = amtChicken * 8
    totalCost = costPizza + costPasta + costChicken
    print (("By ordering {} pizzas, {} orders of pasta, and {} orders of chicken wings, your order total comes to ${}.").format(amtPizzas, amtPasta, amtChicken, totalCost))
dominosTime()

#########################################

"""
Function Name: tipAndSplit()
Parameters: N/A
Returns: None
"""
def tipAndSplit():
    orderTotal = int(input("What was the order total? "))
    percentageTip = int(input("What percentage would you like to tip? "))
    amtPeople = int(input("How many people are splitting the order? "))
    totalTip = orderTotal * (percentageTip/100)
    pricePerPerson = (orderTotal+totalTip)/amtPeople
    roundedTip = round(totalTip, 2)
    roundedPerPerson = round(pricePerPerson, 2)
    print (("The driver got a tip of ${}. Each person paid ${}.").format(roundedTip, roundedPerPerson))
tipAndSplit()
    
#########################################

"""
Function Name: youtuber()
Parameters: N/A
Returns: None
"""
def youtuber():
    amtVideos = int(input("How many videos have you made? "))
    amtPaid = float(input("How much do you get paid per view? "))
    totalViews = int(input("How many views do your videos have? "))
    totalEarned = (amtVideos * totalViews) * amtPaid
    roundedTotal = round(totalEarned, 2)
    print (("You have made ${} by making YouTube videos!").format(roundedTotal))

youtuber()
#########################################

"""
Function Name: bathBomb()
Parameter: N/A
Returns: None
"""
def bathBomb():
    r = float(input("What is the radius of the bath bomb? "))
    pi = 3.14
    volume = (4/3)*(pi)*(r**3)
    roundedVolume = round(volume, 2)
    print (("The volume of a bath bomb with radius {} is {}."). format(r, roundedVolume))

bathBomb()
