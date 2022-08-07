"""
Georgia Institute of Technology - CS1301
HW10 - Object Oriented Programming
"""
class Room: # entire class provided
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __repr__(self):
        return "Room(name: {})".format(self.name)

class Task:
    def __init__(self, name):
        self.name = name
        self.isCompleted = False
    def __eq__(self, other):
        return self.name == other.name and self.isCompleted == other.isCompleted
    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)

class Crewmate:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.isAlive = True
        self.accessories = accessories
        self.tasksDone = 0
    def doTask(self, t):
        if t.isCompleted == False:
            self.tasksDone += 1
        else:
            return "Nothing to do here."
    def vote(self, v):
        newList = v.crewmates + v.impostors
        for player in newList:
            string = str(player.name)
            if string != self.name and player.isAlive == True:
                if string[0] == self.name[0]:
                    return player
    def callMeeting(self, c):
        tally = {}
        temp = 0
        newList = c.crewmates + c.impostors
        for player in newList:
            n = player.vote(c)
            if n.name in tally:
                tally[n.name] += 1
            else:
                tally[n.name] = 1
        mostVotes = max(tally, key = tally.get)
        for x in c.crewmates:
            if mostVotes == x.name:
                x.isAlive = False
                return str(mostVotes) + " was not An Impostor,"
        for y in c.impostors:
            if mostVotes == y.name:
                y.isAlive = False
                return str(mostVotes) + " was An Impostor."
    def __repr__(self): # provided
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)
    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.isAlive = True
        self.accessories = accessories
        self.eliminateCount = 0
    def eliminate(self, x):
        if type(x) == Impostor:
            return "They're on your team -_-"
        if type(x) == Crewmate:
            x.isAlive = False
            self.eliminateCount += 1
    def vote(self, v):
        newList = v.crewmates + v.impostors
        for player in newList:
            string = str(player.name)
            if string != self.name and player.isAlive == True:
                if string[0] == self.name[0]:
                    return player
    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)
    def __str__(self):
        return "My name is " + self.name + " and I'm an impostor."
    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)
    
class AmongUs:
    def __init__(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.rooms = {}
        self.crewmates = []
        self.impostors = []
    def registerPlayer(self, r):
        totalPlayers = len(self.crewmates) + len(self.impostors)
        if totalPlayers == self.maxPlayers:
            return "Lobby is full."
        if r in self.crewmates:
            return "Player with name: " + str(r.name) + " exists."
        if r in self.impostors:
            return "Player with name: " + str(r.name) + " exists."
        else:
            if type(r) == Crewmate:
                self.crewmates.append(r)
            if type(r) == Impostor:
                self.impostors.append(r)
    def registerTask(self, task, room):
        newList = []
        for item in self.rooms.values():
            for x in item:
                newList.append(x)
        if task in newList:
            return "This task has already been registered."
        else:
            self.rooms[room.name] = []
            self.rooms[room.name].append(task)
    def gameOver(self):
        if len(self.crewmates) == 0:
            return "Defeat! All crewmates have been eliminated."
        if len(self.impostors) == 0:
            return "Victory! All impostors have been eliminated."
        else:
            return "Game is not over yet!"
    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)


    

