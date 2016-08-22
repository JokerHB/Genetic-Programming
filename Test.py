'This is an test file'

# def generateNode(termSet, funcSet, node, method, deep, prob):
#     if deep == 0 or random <= prob:
#         nodeVal = namedtuple('NodeVal', ['type', 'val'])
#         type = None
#         var = None
#         if random >= prob:
#             type = public.const
#             index = len(termSet.constSet) * prob
#             var = termSet.getConst(index=index)
#         else:
#             type = public.var
#             index = len(termSet.varSet) * prob
#             var = termSet.getVar(index=index)
#         return nodeVal._make([str(type), str(var)])

def func(val):
    func_a = 33
    print func_a
    if val >= 10:
        global func_a
        print func_a
    else:
        func_a = 2
        print func_a

func(111)

import Kits.GenerateNode as genNode
from Kits.PublicDefine import PublicDefine
from random import random

p = PublicDefine()


# print genNode.PublicDefine.grow

print p.grow
print random()

print range(10)