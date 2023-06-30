import consoleColors as cc
import graph
from typing import *
from queue import Queue


def start(Graph: graph.Graph):
    for i in range(0, Graph.nodeCount):
        print(Graph.nodes[i])
    print(cc.BG_CYAN + cc.BG_BLACK + "Ready!")
    subject = Graph.nodes[0]
    while True:
        command = input(">")

        if command == "x":
            print(cc.RED + "Terminating")
            return
        elif command == "dfs":
            ret: List[graph.Node] = graph.dfs(subject)
            print("DFS traversal is: " + "".join(ret))
        elif command == "bfs":

            ret: List[graph.Node] = graph.bfs(subject)
            print("BFS traversal is: " + "".join(ret))
        elif command == "bcy":
            visited = {subject.name: True}
            parents = {subject.name: None}
            print("The graph has cycles: ", graph.bf_cycle_detect(
                subject, visited, parents))
        elif command == "dcy":
            visited = {subject.name: True}
            parents = {subject.name: None}
            print("The graph has cycles: ", graph.df_cycle_detect(
                subject, visited, parents))
        elif command == "print":
            for i in range(0, Graph.nodeCount):
                print(Graph.nodes[i])
        else:
            print("Unknown command: " + command)
