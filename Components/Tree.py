from Components.Node import Node
from random import random
from Kits.PublicDefine import PublicDefine

import Kits.GenerateNode as genNode

public = PublicDefine()

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.children = []
        self.fitness = 0
        self.val = 0
        self.toString = ''
        self.deep = 0
        self.size = 0
        # self.public = PublicDefine()

    def makeTree(self, deep, termSet, funcSet):
        """
        build a tree with terminal set and function set that deep is determined
        :param deep:
        :param termSet:
        :param funcSet:
        :return:
        """
        self.deep = 1
        self.size = 1
        if random() <= 0.5:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root,
                                 method=public.grow, deep=deep, prob=random())
        else:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root,
                                 method=public.full, deep=deep, prob=random())

        if self.root.getType() == public.func:
            self.toString = self.root.getVal().getName()
            for i in range(self.root.getVal().getArity()):
                child = Tree()
                if random() <= 0.5:
                    genNode.generateNode(termSet=termSet, funcSet=funcSet, node=child.root,
                                         method=public.grow,deep=deep - 1, prob=random())
                else:
                    genNode.generateNode(termSet=termSet, funcSet=funcSet, node=child.root,
                                         method=public.full,deep=deep - 1, prob=random())
                child.makeTree(deep=deep - 1, termSet=termSet, funcSet= funcSet)
                self.children.append(child)

    def calVal(self, varList):
        """
        get the value of the tree
        :param varList:
        :return:
        """
        'varList is a dictionary of x:1, y: 2, z: 3 ...'
        if self.root.getType() == public.const:
            self.val = self.root.getVal()
            return self.val
        elif self.root.getType() == public.var:
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
        """
        reset the tee
        :return:
        """
        self.size = 1
        self.deep = 1
        self.val = 0
        if self.root.getType() != public.func:
            self.toString = ''
        else:
            self.toString = self.root.getVal().getName()
        for child in self.children:
            child.clearTree()

    def calFitness(self, fit ,varList):
        self.fitness = abs(fit.getFitness(varList=varList) - self.val)

    def getDeep(self):
        """
        get the deep of the tree, value stored in self.deep
        :return: deep
        """
        'NOTION: This method can ONLY using ONCE !'
        if len(self.children) == 0:
            self.deep = 1
            return self.deep
        else:
            deepList = []
            for child in self.children:
                deepList.append(child.getDeep() + 1)
            self.deep = max(deepList)
            return self.deep

    def getSize(self):
        """
        get the size of the tree, value stored in self.size
        :return: size
        """
        'NOTION: This method can ONLY using ONCE !'
        if self.root.getType() != public.func:
            self.size = 1
            return self.size
        for child in self.children:
            self.size += child.getSize()
        return self.size

    def getSubTree(self, index):
        """
        get the sub tree from the index
        :param index:
        :return:
        """
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
        """
        display the tree from the deep
        :param deep:
        :return:
        """
        content = ' ' * deep
        # function type node
        if self.root.getType() == public.func:
            # content += self.toString + ': ' + str(self.val) + ' : ' + str(self.size) +'\n'
            content += self.toString + '(' + str(self.val) + ')' + ': d: ' + str(self.deep) + ' s: ' + str(self.size) + '\n'
        else:
            # terminal type node
            self.toString = str(self.root.getVal())
            content += self.toString + '\n'
        for child in self.children:
            _content = child.displayTree(deep + 2)
            content += _content
        return content
