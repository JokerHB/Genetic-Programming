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
        self.maxDeep = 0
        self.public = PublicDefine()

    def makeTree(self, deep, termSet, funcSet):
        self.root = Node()
        if random() <= 0.5:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root, method=self.public.grow, deep=deep, prob=random())
        else:
            genNode.generateNode(termSet=termSet, funcSet=funcSet, node=self.root, method=self.public.full, deep=deep, prob=random())

        if self.root.getType() == self.public.func:
            for i in range(self.root.getVal().getArity()):
                child = Node()
