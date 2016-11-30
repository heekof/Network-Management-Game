


# Class Resource

# Abstact Class Resource
class Resource(object):
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