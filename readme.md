# pyGraphLang
A simple graph language implemented in python

## Usage
Write your graph in a .pgl file, for example:
```
# the defs block holds the definitions of the nodes
defs:
    node1:
        key=value
    node2:
        key=valor
    node3:
        key=valeur

# the rels block holds the relations between the nodes
rels:
    node1-<-bidirectional_link->-node2
    samantha-<-friend->-alicia

# the adjmat block holds the adjacency matrix of the graph. both rels and adjmat can be used to describe relations at the same time

adjmat:
    0, friend, 0, 0, 1, 0, 0, 0, 0, 0
    friend, 0, 1, 0, 0, 1, 0, 0, 0, 0
    0, 0, 0, 1, 0, 0, 1, 0, 0, 0
    0, 0, 0, 0, 1, 0, 0, 1, 0, 0
    0, 0, 0, 0, 0, customer, 0, 0, 1, 0
    0, 0, 0, 0, 0, 0, 1, 0, 0, 1
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1
    0, 0, 0, f, 0, 0, 0, 0, 0, 0

end # end of the file
```

Then, run the following command:
```
python3 main.py <path_to_pgl-file>
```
once successfully loaded, you can now use the terminal to specify commands to perform different operations on the data structure. For example:
```
> print
> bfs
> dfs