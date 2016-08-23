from Components.Evolve import Evolve
from Components.TerminalSet import TerminalSet
from Components.FunctionSet import FunctionSet
from Components.Fitness import Fitness

import Kits.Functions as funcKit

termSet = TerminalSet(var=['x', 'y', 'z'], const=[i for i in range(10)])

add_func = FunctionSet(name='add', func=funcKit.add, arity=2)
sub_func = FunctionSet(name='sub', func=funcKit.sub, arity=2)
mul_func = FunctionSet(name='mul', func=funcKit.mul, arity=2)
mod_func = FunctionSet(name='mod', func=funcKit.mod, arity=2)

funcSet = [add_func, sub_func, mul_func, mod_func]

fitness = Fitness(funcKit.fitnessFnc)

varDict = {'x':2, 'y':1}

# if __name__ == 'main':
#     evolve = Evolve(funcSet=funcSet, termSet=termSet, fit=fitness)
#
#     evolve.init()
#     ans = evolve.evolve()
#
#     print ans.displayTree()


evolve = Evolve(funcSet=funcSet, termSet=termSet, fit=fitness, varDict=varDict)

evolve.init()
ans = evolve.evolve()

print ans.displayTree()