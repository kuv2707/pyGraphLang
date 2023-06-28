import consoleColors as cc

def start(Graph):
    for i in range(0,Graph.nodeCount):
        print(Graph.nodes[i])
    print(cc.BG_CYAN + cc.BG_BLACK + "Ready!")
    subject = Graph.nodes[0]
    while True:
        command=input(">")
        print(command)
        if(command == "X"):
            print(cc.RED + "Terminating")
            return