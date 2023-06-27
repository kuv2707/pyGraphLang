import graph
TAB = "    "


def parseFile(filename='./sampleFile.pgl'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line[0:-1].split("#")[0] for line in lines]

        # print(lines)
        Graph = graph.Graph()
        for index, line in enumerate(lines):
            if line == "defs:":
                print("found defs")
                populateDefs(lines, index+1, Graph)
                
            if line == "rels:":
                print("found rels")
                establishRels(lines, index+1, Graph.nodes)
            if line == "adjmat:":
                print("linking from adjmat")
                modelAdjacencyMatrix(lines,index+1, Graph.nodes)





    print("printing nodes")
    for i in range(0,Graph.nodeCount):
        print(Graph.nodes[i])
    
    # Graph.createAdjacencyMatrix()
    return Graph


def populateDefs(lines, index, Graph):
    nodecount=0
    while lines[index].startswith(TAB):
        nodename = lines[index].strip()
        print("found node: "+nodename)
        node = graph.Node(nodename[0:-1])
        Graph.nodes[node.name] = node
        Graph.nodes[nodecount] = node
        nodecount+=1
        index = scrapeVars(lines, index+1, node)
        index += 1
    Graph.nodeCount=nodecount


def scrapeVars(lines, index, node):
    while True:
        line = lines[index]
        if line.startswith(2*TAB) == False:
            return index-1
        line = line.strip()
        toks = line.split("=")
        node.vars[toks[0]] = toks[1]
        index += 1


def establishRels(lines, index, nodes):
    while True:
        line = lines[index]
        if line.startswith(TAB) == False:
            return index-1
        toks = line.strip().split("-")
        print("tokens",toks)
        left = nodes[toks[0]]
        right = nodes[toks[-1]]
        rel = toks[2]
        l_r = toks[3]
        r_l = toks[1]
        if l_r == ">":
            left.adjacent.append((right,rel))
        if r_l == '<':
            right.adjacent.append((left,rel))
        print(left.name, rel, right.name)
        index += 1


def modelAdjacencyMatrix(lines, index, nodes):
    i = 0
    while True:
        line = lines[index]
        if line.startswith(TAB) == False:
            return index-1
        toks = line.strip().split(",")
        print(i,toks)
        
        for j,tok in enumerate(toks):
            if notFalse(tok.strip()):
                n1 = nodes[i]
                n2 = nodes[j]
                n1.adjacent.append((n2,tok.strip()))
        i+=1
        index+=1


def notFalse(str):
    return not(str == "0" or str == 0)


if __name__ == '__main__':
    parseFile()
