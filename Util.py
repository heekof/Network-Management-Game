import numpy as np
import logging
import numpy as np
import pandas as pd
#standard import
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import sys
from numpy.random import randn
import os


def jaafar():
    print "Put the game here"

def printVar(a,b=3,*args,**kwargs):
    print 'a = {} and b  = {} and c = {} '.format(a,b,args[0])

    for key,value in kwargs.iteritems():
        print 'key = {} , value = {} '.format(key,value)

    return True
def deleteContent(path):
    open(path,'w').close()

def initLog(path,debug=0):


    logger = logging.getLogger(__name__)
    deleteContent(path)
    logger.setLevel(logging.DEBUG)
    # create a file handler
    handler = logging.FileHandler(path)
    handler.setLevel(logging.DEBUG)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)



    if not debug:
        logging.disable(logging.DEBUG)


    return logger
