from collections import defaultdict

class Tree(object):


    def __init__(self, name='root', weight=0, children=None):
        self.name = name
        self.weight = weight
        self.children = []


    def __repr__(self):
        return self.name


    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def add_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

n = []
with open("input.txt") as inputfile:
    for line in inputfile:
        line_cleaned = line.replace("(", "").replace(")", "").strip().split()
        line_cleaned[1] = int(line_cleaned[1])
        if len(line_cleaned) > 2:
            del line_cleaned[2]
        n.append(line_cleaned)

print(n)

dict = {}

for line in n:
    if line[0] not in dict:
        dict[line[0]] = Tree(line[0])
        if len(line) > 2:
            for idx in range(2, len(line)):
                if line[idx] not in dict:
                    dict[line[idx]] = Tree(line[idx])
                dict[line[0]].add_child(dict[line[idx]])
    dict[line[0]].add_weight(line[1])

print(dict["hlqnsbe"].children)