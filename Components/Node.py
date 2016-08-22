class Node(object):
    def __init__(self, type = None, val = None):
        self.type = type
        self.val = val

    def getType(self):
        return self.type

    def getVal(self):
        return  self.val

    def setType(self, type):
        self.type = type

    def setVal(self, val):
        self.val = val