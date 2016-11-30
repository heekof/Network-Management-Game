
from SLO import *

# Class SLA

class SLA:
    name = "SLA"
    MySLOs = [SLO(4),SLO(2),SLO(1)]

    def __init__(self,name):
        self.name = name