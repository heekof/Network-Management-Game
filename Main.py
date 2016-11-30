from Network import *
from Resource import *
from NetGame import *
from Service import *
from SLA import *


if __name__ == '__main__':
    print('This is the main program')

# Instanciate the Network with a name, a number of router, a number of servers and a budget
MyNet = Network('Network 1', 3, 5, 100)



Game = NetGame(MyNet)

Game.setDifficultyLevel("easy")

Game.start(100)



print(Network.__dict__)

print(MyNet.__dict__)

print(Game.__dict__)

MySLA = SLA("SLA1")




print(MySLA.MySLOs[0].getInfo())

