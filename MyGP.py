from Components.Evolve import Evolve
from Components.TerminalSet import TerminalSet
from Components.FunctionSet import FunctionSet
from Components.Tree import Tree
from Components.Fitness import Fitness
from random import random
from random import choice

import Kits.Operations as genop
import Kits.Functions as genfunc

import Kits.Functions as funcKit

add_func = FunctionSet(name='add', func=funcKit.add, arity=2)
sub_func = FunctionSet(name='sub', func=funcKit.sub, arity=2)
mul_func = FunctionSet(name='mul', func=funcKit.mul, arity=2)
mod_func = FunctionSet(name='mod', func=funcKit.mod, arity=2)

termSet = TerminalSet(var=['x', 'y'], const=[i for i in range(10)])

funcSet = [add_func, sub_func, mul_func, mod_func]

fitness = Fitness(funcKit.fitnessFnc)

varDict = {'x':2, 'y':1}

if __name__ == '__main__':
    evolve = Evolve(funcSet=funcSet, termSet=termSet, fit=fitness, varDict=varDict)

    evolve.init()
    ans = evolve.evolve()

    ans.getSize()
    ans.getDeep()
    ans.calVal(varList=varDict)
    ans.calFitness(varList=varDict, fit=fitness)

    print 'fitness is %d' % ans.fitness

    print ans.displayTree()