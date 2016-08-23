from copy import deepcopy
from random import random
from Components.Tree import Tree

def corssovers(tree_a, tree_b):
    tree_A = deepcopy(tree_a)
    tree_B = deepcopy(tree_b)
    index_a = int(random() * tree_A.size)
    subTreeCorssovers(sourceTree=tree_A, index=index_a, subTree=tree_B)
    tree_A.clearTree()
    return tree_A

def mutation(tree, funcSet, termSet):
    _tree = deepcopy(tree)
    index = int(random() * _tree.size)
    # print 'mutation index %d' % index
    subTreeMutation(sourceTree=_tree, index=index, funcSet=funcSet, termSet=termSet)
    _tree.clearTree()
    return _tree

def subTreeMutation(sourceTree, index, funcSet, termSet):
    if index == 0:
        subTree = Tree()
        subTree.makeTree(deep=sourceTree.getDeep(), funcSet=funcSet, termSet=termSet)
        # MARK: This part need to be REWRITE
        sourceTree.root = subTree.root
        sourceTree.children = subTree.children
        sourceTree.fitness = subTree.fitness
        sourceTree.val = subTree.val
        sourceTree.toString = subTree.toString
        sourceTree.deep = subTree.deep
        sourceTree.size = subTree.size
        sourceTree.public = subTree.public
        sourceTree.clearTree()
        return None
    for i in range(len(sourceTree.children)):
        index -= sourceTree.children[i].size
        if index < 0:
            index += sourceTree.children[i].size - 1
            subTreeMutation(sourceTree=sourceTree.children[i], index=index, funcSet=funcSet, termSet=termSet)
            break
        elif index == 0:
            subTreeMutation(sourceTree=sourceTree.children[i], index=sourceTree.children[i].size - 1, funcSet=funcSet, termSet=termSet)
            break

def getSubTreeList(tree, deep, sublist):
    if tree.deep <= deep and tree not in sublist:
        sublist.append(tree)

    for child in tree.children:
        if child.deep <= deep:
            sublist.append(child)
        getSubTreeList(tree=child, deep=deep, sublist=sublist)

def subTreeCorssovers(sourceTree, index, subTree):
    if index == 0:
        subTreeList = []
        getSubTreeList(tree=subTree, deep=sourceTree.deep, sublist=subTreeList)
        index_b = int(random() * len(subTreeList))
        _subTree = subTreeList[index_b]
        # MARK: This part need to be REWRITE
        sourceTree.root = _subTree.root
        sourceTree.children = _subTree.children
        sourceTree.fitness = _subTree.fitness
        sourceTree.val = _subTree.val
        sourceTree.toString = _subTree.toString
        sourceTree.deep = _subTree.deep
        sourceTree.size = _subTree.size
        # sourceTree.public = _subTree.public
        sourceTree.clearTree()
        return None
    for i in range(len(sourceTree.children)):
        index -= sourceTree.children[i].size
        if index < 0:
            index += sourceTree.children[i].size - 1
            subTreeCorssovers(sourceTree=sourceTree.children[i], index=index, subTree=subTree)
            break
        elif index == 0:
            subTreeCorssovers(sourceTree=sourceTree.children[i], index=sourceTree.children[i].size - 1, subTree=subTree)
            break