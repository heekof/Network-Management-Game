# This is the service on top of the network
# This is an abstract class

from SLA import *

class Service(object):

    mySLA = SLA("none")

    def __init__(self):
        self.x = 5
    def createSLA(self,SLA):
        self.mySLA = SLA
    def getSLA(self):
        return self.mySLA