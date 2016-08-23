'This is an test file'

import Kits.GenerateNode as genNode
from Kits.PublicDefine import PublicDefine
from random import random

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

# def func(val):
#     func_a = 33
#     print func_a
#     if val >= 10:
#         global func_a
#         print func_a
#     else:
#         func_a = 2
#         print func_a
#
# func(111)
#
# p = PublicDefine()
#
#
# # print genNode.PublicDefine.grow
# print p.grow
# print random()
#
# print range(10)
#
# print 1 % 0


class A(object):
    def __init__(self, val):
        self. a = val

def replace(a):
    _a = A(4)
    # a = _a
    a.a = 3
    print id(a)

test_a = A(1)

print test_a.a

print id(test_a)

replace(test_a)

print test_a.a

