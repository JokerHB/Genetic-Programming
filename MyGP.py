from Components.TerminalSet import TerminalSet
from Components.FunctionSet import FunctionSet
from Components.Tree import Tree
from Components.Fitness import Fitness

def add(varList):
    sum = 0
    for _ in varList:
        sum += _
    return sum

def sub(varList):
    ans = varList[0]
    for _ in varList[1:]:
        ans -= _
    return ans

def mul(varList):
    ans = 1
    for _ in varList:
        ans *= _
    return ans

def mod(varList):
    ans = varList[0]
    for _ in varList[1:]:
        if _ == 0:
            ans %= 1
        else:
            ans %= _
    return ans

termSet = TerminalSet(var=['x', 'y'], const=[1,2,3,4,5])

add_func = FunctionSet(name='add', func=add, arity=2)
sub_func = FunctionSet(name='sub', func=sub, arity=2)
mul_func = FunctionSet(name='mul', func=mul, arity=2)
mod_func = FunctionSet(name='mod', func=mod, arity=2)

funcSet = [add_func, sub_func, mul_func, mod_func]

tree = Tree()

tree.makeTree(2, termSet=termSet, funcSet=funcSet)

print tree.calVal({'x':2, 'y':1})