import consoleColors as cc

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


 
def dfs(node: Node,accum={},ret=[]):
    accum[node.name]=True
    for a_node,reln in node.adjacent:
        try:
            accum[a_node.name]
                
        except:
            ret.append(cc.YELLOW + node.name + cc.BLUE + "-[" + reln + "]-")
            dfs(a_node,accum,ret)
    return ret
