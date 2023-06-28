import consoleColors as cc
from queue import Queue
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


 
def dfs(node: Node,visited={},ret=[]):
    visited[node.name]=True
    for a_node,reln in node.adjacent:
        if a_node.name not in visited:
            ret.append(cc.YELLOW + node.name + cc.BLUE + "-[" + reln + "]-")
            dfs(a_node,visited,ret)
    print(cc.RESET)
    return ret

def bfs(queue: Queue, visited={}, ret=[]):
        
    while queue.empty() == False:
        node=queue.get()
        if node.name in visited:
            continue
        visited[node.name]=True
        ret.append(cc.YELLOW + node.name + cc.BLUE + "-["  + "-" + "]-")
        for a_node,reln in node.adjacent:
            if a_node.name not in visited:
                queue.put(a_node)
                
    print(cc.RESET)
    return ret
