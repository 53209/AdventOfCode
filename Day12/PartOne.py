# INPUT
input = open("input.txt")

n = " "
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

group = []
def group_up(num):
    children = records[num]
    for child in children:
        if child not in group:
            group.append(group_up(child))
group_up(0)
print(group)


