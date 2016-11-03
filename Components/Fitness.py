class Fitness(object):
    """
    fitness function class, provide the method of calculating the fitness
    """
    def __init__(self, func = None):
        self.func = func

    def getFitness(self, varList):
        try:
            _ = self.func(varList)
            return _
        except Exception, e:
            print ('Fitness.getFitness', e)
            return 0