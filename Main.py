'''

    Call of local classes

'''


from NetGame import NetGame
from Service import Service
from Manager import Manager
from Network import Network
from SLA import SLA
from Util import initLog,printVar



# Logs initialization

logger = initLog('log/system.log',debug=1)


logger.debug("Start of the Main Program")





# Is this program a package or is it running as main

if __name__ == '__main__' :

    print('This is the main program')

    # Instanciate the Network with a name, a number of router, a number of servers and a budget
    MyNet = Network('Network 1', 3, 5, 100)
    Manager1 = Manager("admin")
    logger.debug("The role of the Manager is {}".format(Manager1.role))
    Game = NetGame(MyNet,Manager1)
    Game.setDifficultyLevel("easy")
    Game.start(100)
    print(Network.__dict__)
    print(MyNet.__dict__)
    print(Game.__dict__)
    MySLA = SLA("SLA1")
    print(MySLA.MySLOs[0].getInfo())

print dir()

MyService = Service()

printVar(7,4,7,f=7,j=9,s=0,RT=4)

