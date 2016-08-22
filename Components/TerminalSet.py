from collections import namedtuple
from random import random

class TerminalSet(object):
    def __init__(self, var = None, const = None):
        self.varSet = var
        self.constSet = const

    def getVar(self, index):
        if len(self.varSet) == 0:
            return None
        try:
            _ = self.varSet[index]
            return _
        except IndexError, e:
            print e
            return self.varSet[0]

    def getConst(self, index):
        if len(self.constSet) == 0:
            return None
        try:
            _ = self.constSet[index]
            return _
        except IndexError, e:
            print e
            return self.constSet[0]