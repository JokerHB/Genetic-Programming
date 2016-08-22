from random import random
from collections import namedtuple
from PublicDefine import PublicDefine

def generateNode(termSet, funcSet, node, method, deep, prob):
    public = PublicDefine()
    if deep == 0 or (method == public.grow and random() <= prob):
        if random() >= prob:
            # node.type = public.const
            node.setType(public.const)
            index = len(termSet.constSet) * prob
            # node.var = termSet.getConst(index=index)
            node.setVar(termSet.getConst(index=index))
        else:
            # node.type = public.var
            node.setType(public.var)
            index = len(termSet.varSet) * prob
            # node.var = termSet.getVar(index=index)
            node.setVar(termSet.getVar(index=index))
    else:
        node.setType(public.func)
        # node.type = public.func
        index = len(funcSet) * prob
        # node.var = funcSet[index]
        node.setVar(funcSet[index])
