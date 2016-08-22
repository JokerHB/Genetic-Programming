class Fitness(object):
    def __init__(self, func = None):
        self.func = func

    def getFitness(self, varList):
        try:
            _ = self.func(varList)
            return _
        except Exception, e:
            print e
            return 0