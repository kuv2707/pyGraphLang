import consoleColors as cc
import graph
from typing import *

def start(Graph: graph.Graph):
    for i in range(0,Graph.nodeCount):
        print(Graph.nodes[i])
    print(cc.BG_CYAN + cc.BG_BLACK + "Ready!")
    subject = Graph.nodes[0]
    while True:
        command=input(">")
        
        if command == "X":
            print(cc.RED + "Terminating")
            return
        elif command == "dfs" :
            ret: List[graph.Node] = graph.dfs(subject)
            print("DFS traversal is: " + "".join(ret))
        else:
            print("Unknown command: " + command)