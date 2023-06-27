# Text colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Text styles
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

RESET = "\033[0m"



class Graph:
    def __init__(self):
        self.nodes = {}



class Node:
    def __init__(self, name):
        self.name = name
        self.vars = {}
        self.adjacent = []

    def __str__(self):
        return f"{BLUE + self.name + RESET}---[vars-{GREEN + str(self.vars) + RESET}  adjs-{'{'} {MAGENTA + ', '.join([f'{node[0].name} : {node[1]}' for node in self.adjacent]) + RESET} {'}'}]"

    def add_adjacent(self, node):
        self.adjacent.append(node)