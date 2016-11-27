
# Python Network Simulation for Q-Learning

class Network:

    serverInstantiationTime = 8
    serverUpdateNonAvailability = 3
    linkInstantiationTime = 5
    linkUpdateNonAvailability = 3
    routerInstantiationTime = 12
    linkUpdateNonAvailability = 7
    totalTime = 1
    Score = 0

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
        pass
    class Router:
        pass
    class Link:
        pass

class Resource:

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

if __name__ == '__main__':
    print('This is the main program')



emp_1 = Network('Network 1', 3, 5, 100)


print(Network.__dict__)

print(emp_1.__dict__)