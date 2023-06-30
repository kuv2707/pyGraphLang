import consoleColors as cc
from queue import Queue
from typing import *


class Graph:
    def __init__(self):
        self.nodes = {}
        self.nodeCount = 0

    def createAdjacencyMatrix(a):
        return


class Node:
    def __init__(self, name):
        self.name = name
        self.vars = {}
        self.adjacent = []

    def __str__(self):
        return f"{cc.BG_RAND + cc.COL1_RAND + self.name + cc.RESET}---[vars-{cc.COL2_RAND + str(self.vars) + cc.RESET}  adjs-{'{'} {cc.COL3_RAND + ', '.join([f'{node[0].name} : {node[1]}' for node in self.adjacent]) + cc.RESET} {'}'}]"

    def add_adjacent(self, node):
        self.adjacent.append(node)


def dfs(node: Node, visited={}, ret=[]):
    visited[node.name] = True
    ret.append(cc.YELLOW + node.name + cc.BLUE + "-[" + "-" + "]-")
    for a_node, reln in node.adjacent:
        if a_node.name not in visited:
            ret = dfs(a_node, visited, ret)

    print(cc.RESET)
    return ret


def bfs(node: Node, visited={}, ret=[]):
    queue = Queue()
    queue.put(node)
    visited[node.name] = True
    while queue.empty() == False:
        node = queue.get()
        ret.append(cc.YELLOW + node.name + cc.BLUE + "-[" + "-" + "]-")
        for a_node, reln in node.adjacent:
            if a_node.name not in visited:
                visited[a_node.name] = True
                queue.put(a_node)

    print(cc.RESET)
    return ret


def bf_cycle_detect(node, visited: Dict[str, str], parents: Dict[str, str], prev: Node = None):
    queue = Queue()
    queue.put((node, None))
    visited[node.name] = True
    parents[node.name] = ""
    while queue.empty() == False:
        node, prev = queue.get()

        for a_node, reln in node.adjacent:
            if a_node == prev:
                continue
            if a_node.name not in visited:
                visited[a_node.name] = True
                queue.put((a_node, node))
                parents[a_node.name] = node.name
            else:
                # if a node is visited, and its parent is not same as current node, there is a cycle
                if parents[a_node.name] != node.name:
                    print("cycle ", node.name, a_node.name)
                    return True
    return False


def df_cycle_detect(node: Node, visited: Dict[str, str], parents: Dict[str, str], prev: Node = None):

    for a_node, reln in node.adjacent:
        if a_node == prev:
            continue
        if a_node.name not in visited:

            visited[a_node.name] = True
            parents[a_node.name] = node.name
            boo = df_cycle_detect(a_node, visited, parents, node)
            if boo == True:
                return boo
        else:
            if parents[a_node.name] != node.name:
                print("cycle ", node.name, a_node.name)
                return True

    print(cc.RESET)
    return False
