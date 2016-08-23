from random import random
from PublicDefine import PublicDefine

def generateNode(termSet, funcSet, node, method, deep, prob):
    public = PublicDefine()
    if deep == 1 or (method == public.grow and random() <= prob):
        if random() >= prob:
            # node.type = public.const
            node.setType(public.const)
            index = int(len(termSet.constSet) * prob)
            # node.var = termSet.getConst(index=index)
            node.setVal(termSet.getConst(index=index))
        else:
            # node.type = public.var
            node.setType(public.var)
            index = int(len(termSet.varSet) * prob)
            # node.var = termSet.getVar(index=index)
            node.setVal(termSet.getVar(index=index))
    else:
        node.setType(public.func)
        # node.type = public.func
        index = int(len(funcSet) * prob)
        # node.var = funcSet[index]
        node.setVal(funcSet[index])
