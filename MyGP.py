from Components.TerminalSet import TerminalSet
from Components.FunctionSet import FunctionSet
from Components.Tree import Tree
from Components.Fitness import Fitness
from random import random

import Kits.Operations as opKit
import Kits.Functions as funcKit

termSet = TerminalSet(var=['x', 'y', 'z'], const=[i for i in range(10)])

add_func = FunctionSet(name='add', func=funcKit.add, arity=2)
sub_func = FunctionSet(name='sub', func=funcKit.sub, arity=2)
mul_func = FunctionSet(name='mul', func=funcKit.mul, arity=2)
mod_func = FunctionSet(name='mod', func=funcKit.mod, arity=2)

funcSet = [add_func, sub_func, mul_func, mod_func]

fitness = Fitness(funcKit.fitnessFnc)

varList = {'x':2, 'y':1, 'z': 10}

tree = Tree()
_tree = Tree()

tree.makeTree(deep=5, termSet=termSet, funcSet=funcSet)
_tree.makeTree(deep=5, termSet=termSet, funcSet=funcSet)

tree.calVal(varList=varList)
_tree.calVal(varList=varList)

tree.calFitness(fit=fitness, varList=varList)
_tree.calFitness(fit=fitness, varList=varList)

tree.getDeep()
_tree.calFitness(fit=fitness, varList=varList)

tree.getSize()
_tree.getSize()

print 'main tree val %d' % tree.val

print 'main tree fitness %d' % tree.fitness

print 'main tree deep %d' % tree.deep

print 'main tree size %d' % tree.size

print tree.displayTree()

# ************** cross Test **************

print '_main tree val %d' % _tree.val

print '_main tree fitness %d' % _tree.fitness

print '_main tree deep %d' % _tree.deep

print '_main tree size %d' % _tree.size

print _tree.displayTree()

newTree = opKit.corssovers(tree_a=tree, tree_b=_tree)

newTree.calVal(varList=varList)

newTree.calFitness(fit=fitness, varList=varList)

newTree.getDeep()

newTree.getSize()

print newTree.displayTree()

# ************** mutation Test **************
# print 'mutation operation...\n'
#
# newTree = osKit.mutation(tree, funcSet=funcSet, termSet=termSet)
#
# newTree.calVal(varList=varList)
#
# newTree.calFitness(fit=fitness, varList=varList)
#

# ************** sub tree Test **************
# print newTree.displayTree()

# index = random() * tree.size
#
# index = int(index)
#
# print 'index is %d\n' % index
#
# tree.getSubTree(index=index)

# for i in range(100):
#
#     index = random() * tree.size
#
#     index = int(index)
#
#     print 'index is %d\n' % index
#
#     tree.getSubTree(index=index)
#
#     print '-----------------------------'
