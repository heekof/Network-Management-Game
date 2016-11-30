from Util import *
from Flow import *
from Network import *

# Class Network Game

class NetGame:

    Score = 0  # can be negative or positive
    level = ""
    totalTime = 0
    MyNet = Network('Network 1', 3, 5, 100);
    MyFlow = Flow("easy");

    def __init__(self,Network):
        self.MyNet = NetGame



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
