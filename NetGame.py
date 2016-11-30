from Util import jaafar
from Flow import Flow
from Network import Network
from Manager import Manager
# Class Network Game

class NetGame:

    Score = 0  # can be negative or positive
    level = ""
    totalTime = 0
    localNet = Network('Network 1', 3, 5, 100);
    localManager = Manager("admin")
    MyFlow = Flow("easy");

    def __init__(self,Network,Manager):
        self.localNet = NetGame
        self.localManager = Manager



    def setDifficultyLevel(self,level):
        self.level = level
        self.MyFlow = self.level
        print(self.level)

    def start(self,totalTime):
        self.totalTime = totalTime
        ## Here the main code
        input = "1"
        while(input != "0"):
            print("enter key")
            input = raw_input()
            print input
        jaafar()
