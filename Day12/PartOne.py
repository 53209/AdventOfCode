class Tree(object):


    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


# INPUT
input = open("input.txt")

'''
records = {}
for _ in range(0, 2000):
    n = str(input.readline())
    n_cleaned = n.replace("<->", "").replace(",", " ").strip().split()
    n_int = [int(x) for x in n_cleaned]
    if len(n_int) > 2:
        sublist = n_int[1:]
        records[n_int[0]] = sublist
    else:
        records[n_int[0]] = n_int[1]

print(records)
'''

records = {}
for _ in range(0, 2000):
    n = str(input.readline())
    n_cleaned = n.replace("<->", "").replace(",", " ").strip().split()
    if len(n_cleaned) > 2:
        sublist = n_cleaned[1:]
        records[n_cleaned[0]] = sublist
    else:
        records[n_cleaned[0]] = n_cleaned[1]

# print(records)


visited = []
def find_all_the_nodes(record):
    visited.append(record)
    children = records[record]
    for child in children:
        if child not in visited:
            find_all_the_nodes(child)


find_all_the_nodes("0")

print(visited)
print(len(visited))

'''
set_visited = list(set(visited))
print(set_visited)
print(len(set_visited))
'''




