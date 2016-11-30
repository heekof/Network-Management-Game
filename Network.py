
# Python Network Simulation for Q-Learning
# Now you need a UML Diagram

import numpy as np
from Util import *

# This is the skeleton of the Network
class Network:


    Sessions = 0
    actionId = 0

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

    def netwotkMnagementAction(self,actionId):
        self.actionId = actionId



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














