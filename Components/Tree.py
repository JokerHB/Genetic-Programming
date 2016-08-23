from Components.Node import Node
from random import random
from Components.FunctionSet import FunctionSet
from Components.TerminalSet import TerminalSet
from Kits.PublicDefine import PublicDefine

import Kits.GenerateNode as genNode


class Tree(object):
    def __init__(self):
        self.root = None
        self.children = []
        self.fitness = 0
        self.val = 0
        self.toString = ''
        self.public = PublicDefine()

    def makeTree(self, deep, termSet, funcSet):
        self.root = Node()
        if random() <= 0.5:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root,
                                 method=self.public.grow, deep=deep, prob=random())
        else:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root,
                                 method=self.public.full, deep=deep, prob=random())

        if self.root.getType() == self.public.func:
            self.toString = self.root.getVal().getName()
            for i in range(self.root.getVal().getArity()):
                child = Tree()
                child.root = Node()
                if random() <= 0.5:
                    genNode.generateNode(termSet=termSet, funcSet=funcSet, node=child.root,
                                         method=self.public.grow,deep=deep - 1, prob=random())
                else:
                    genNode.generateNode(termSet=termSet, funcSet=funcSet, node=child.root,
                                         method=self.public.full,deep=deep - 1, prob=random())
                child.makeTree(deep=deep - 1, termSet=termSet, funcSet= funcSet)
                self.children.append(child)

    def calVal(self, varList):
        'varList is a dictionary of x:1, y: 2, z: 3 ...'
        if self.root.getType() == self.public.const:
            self.val = self.root.getVal()
            return self.val
        elif self.root.getType() == self.public.var:
            try:
                self.val = varList[self.root.getVal()]
            except Exception, e:
                print ('Tree.calVal', e)
                self.val = 0
            return self.val
        else:
            vars = []
            for i in range(int(self.root.getVal().getArity())):
                tmp_var = self.children[i].calVal(varList=varList)
                vars.append(tmp_var)
            self.val = self.root.getVal().runFunc(vars)
            return self.val

    def displayTree(self, deep = 1):
        content = ' ' * deep
        if self.toString != '':
            content += self.toString + ': ' + str(self.val) + '\n'
        else:
            self.toString = str(self.root.getVal())
            content += self.toString + '\n'
        for child in self.children:
            _content = child.displayTree(deep + 2)
            content += _content
        return content
