from Components.Node import Node
from random import random
from Kits.PublicDefine import PublicDefine

import Kits.GenerateNode as genNode


class Tree(object):
    def __init__(self):
        self.root = None
        self.children = []
        self.fitness = 0
        self.val = 0
        self.toString = ''
        self.deep = 0
        self.size = 0
        self.public = PublicDefine()

    def makeTree(self, deep, termSet, funcSet):
        self.deep = 1
        self.size = 1
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

    def clearTree(self):
        self.size = 1
        self.deep = 1
        self.val = 0
        if self.root.getType() != self.public.func:
            self.toString = ''

        else:
            self.toString = self.root.getVal().getName()
        for child in self.children:
            child.clearTree()

    def calFitness(self, fit ,varList):
        self.fitness = abs(fit.getFitness(varList=varList) - self.val)

    def getDeep(self):
        'NOTION: This method can ONLY using ONCE !'
        if self.root.getType() != self.public.func:
            self.deep = 1
            return self.deep
        deepList = []
        for child in self.children:
            child.deep += child.getDeep()
            deepList.append(child.deep)
        self.deep = max(deepList)
        return self.deep

    def getSize(self):
        'NOTION: This method can ONLY using ONCE !'
        if self.root.getType() != self.public.func:
            self.size = 1
            return self.size
        for child in self.children:
            self.size += child.getSize()
        return self.size

    def getSubTree(self, index):
        if index == 0:
            print self.displayTree()
        for child in self.children:
            index -= child.size
            if index < 0:
                index += child.size - 1
                child.getSubTree(index=index)
                break
            elif index == 0:
                child.getSubTree(index=child.size - 1)
                break

    def displayTree(self, deep = 1):
        content = ' ' * deep
        # function type node
        if self.root.getType() == self.public.func:
            # content += self.toString + ': ' + str(self.val) + ' : ' + str(self.size) +'\n'
            content += self.toString + ': ' + str(self.val) + '\n'
        else:
            # terminal type node
            self.toString = str(self.root.getVal())
            content += self.toString + '\n'
        for child in self.children:
            _content = child.displayTree(deep + 2)
            content += _content
        return content
