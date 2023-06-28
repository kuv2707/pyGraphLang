import consoleColors as cc
import graph
from typing import *
from queue import Queue

def start(Graph: graph.Graph):
    for i in range(0,Graph.nodeCount):
        print(Graph.nodes[i])
    print(cc.BG_CYAN + cc.BG_BLACK + "Ready!")
    subject = Graph.nodes[0]
    while True:
        command=input(">")
        
        if command == "x":
            print(cc.RED + "Terminating")
            return
        elif command == "dfs" :
            ret: List[graph.Node] = graph.dfs(subject)
            print("DFS traversal is: " + "".join(ret))
        elif command == "bfs" :
            queue=Queue()
            queue.put(subject)
            ret: List[graph.Node] = graph.bfs(queue)
            print("BFS traversal is: " + "".join(ret))
        elif command == "print":
            for i in range(0,Graph.nodeCount):
                print(Graph.nodes[i])
        else:
            print("Unknown command: " + command)