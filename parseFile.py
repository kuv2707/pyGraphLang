TAB="    "
import graph
def parseFile(filename='./sampleFile.pgl'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines=[line[0:-1] for line in lines]
        print(lines)
        Graph = graph.Graph()
        for index,line in enumerate(lines):
            if line == "defs:":
                print("found defs")
                populateDefs(lines,index+1,Graph)
                print("printing nodes")
                for node,val in Graph.nodes.items():
                    print(val)
            if line == "rels:":
                print("found rels")
                establishRels(lines,index+1,Graph.nodes)
    return Graph



def populateDefs(lines,index,Graph):
    while lines[index].startswith(TAB):
        nodename=lines[index].strip()
        print("found node: "+nodename)
        node= graph.Node(nodename[0:-1])
        Graph.nodes[node.name]=node
        index = scrapeVars(lines,index+1,node)
        index+=1

def scrapeVars(lines,index,node):
    while True:
        line = lines[index]
        if line.startswith(2*TAB)== False:
            return index-1
        line=line.strip()
        toks=line.split("=")
        node.vars[toks[0]] = toks[1]
        index+=1


def establishRels(lines,index,nodes):
    while True:
        line=lines[index]
        if line.startswith(TAB)== False:
            return index-1
        toks =  line.strip().split("-")
        print(toks)
        index+=1




if __name__ == '__main__':
    parseFile()