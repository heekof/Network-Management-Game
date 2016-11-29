
# Python Network Simulation for Q-Learning
# Now you need a UML Diagram

import numpy as np


# This is the skeleton of the Network
class Network:

    totalTime = 1
    Score = 0 # can be negative or positive
    SLO = ''
    Sessions = 0

    def __init__(self, name, numberRouter, numberServer, budget):
        self.name = name
        self.numberRouter = numberRouter
        self.numberServer = numberServer
        self.budget = budget

    def getname(self):
        return '{}'.format(self.name)

    def getnumberrouter(self):
        return '{}'.format(self.numberRouter)

    def getnumberserver(self):
        return '{}'.format(self.numberServer)

    def updateScore(self):
        return self.Score + 1

    class Server:
        serverInstantiationTime = 8
        serverUpdateNonAvailability = 3
    class Router:
        routerInstantiationTime = 12
        routerUpdateNonAvailability = 7

    class Link:
        linkInstantiationTime = 5
        linkUpdateNonAvailability = 3

class SLA:
    def __init__(self):
        pass

    class SLO:
        def __init__(self):
            pass

# This is the service on top of the network
class Service:
    def __init__(self):
        pass


class Resource:
    delay = 2
    def __init__(self):
        pass

class CPU1(Resource):
    price = 1
    performance = 1

    def __init__(self):
        pass

class CPU2(Resource):
    price = 2
    performance = 2
    def __init__(self):
        pass

class CPU3(Resource):
    price = 3
    performance = 3
    def __init__(self):
        pass
class Flow:
    sessionNumber = 0
    def __init__(self,difficulty):
        if difficulty == "easy":
            pass
        elif difficulty == "normal":
            pass
        else:
            True


    def flowGenerator(self):
        pass

class NetGame:

    level = ""

    def __init__(self):
        pass

    def setDifficultyLevel(self,level):
        self.level = level
        print(self.level)


if __name__ == '__main__':
    print('This is the main program')


# Instanciate the Network with a name, a number of router, a number of servers and a budget

MyNet = Network('Network 1', 3, 5, 100)
MyFlow = Flow("easy");

Game = NetGame()

Game.setDifficultyLevel("easy")

print(Network.__dict__)

print(MyNet.__dict__)

print(Game.__dict__)

