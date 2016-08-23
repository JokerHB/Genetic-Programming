from Components.TerminalSet import TerminalSet
from Components.FunctionSet import FunctionSet
from Components.Tree import Tree
from Components.Fitness import Fitness

import Kits.Functions as funcKit

termSet = TerminalSet(var=['x', 'y'], const=[1,2,3,4,5])

add_func = FunctionSet(name='add', func=funcKit.add, arity=2)
sub_func = FunctionSet(name='sub', func=funcKit.sub, arity=2)
mul_func = FunctionSet(name='mul', func=funcKit.mul, arity=2)
mod_func = FunctionSet(name='mod', func=funcKit.mod, arity=2)

funcSet = [add_func, sub_func, mul_func, mod_func]

fitness = Fitness(funcKit.fitnessFnc)

varList = {'x':2, 'y':1}

tree = Tree()

tree.makeTree(deep=3, termSet=termSet, funcSet=funcSet)

tree.calVal(varList=varList)

tree.calFitness(fit=fitness, varList=varList)

tree.getDeep()

tree.getSize()

print 'main tree val %d' % tree.val

print 'main tree fitness %d' % tree.fitness

print 'main tree deep %d' % tree.deep

print 'main tree size %d' % tree.size

print tree.displayTree()
