class FunctionSet(object):
    def __init__(self, name = None, func = None, arity = None):
        self.name = name
        self.func = func
        self.arity = arity

    def getName(self):
        return self.name

    def getArity(self):
        return self.arity

    def getFunc(self):
        return self.func

    def runFunc(self, varList):
        try:
            _ = self.func(varList)
            return _
        except Exception, e:
            print e
            return 0