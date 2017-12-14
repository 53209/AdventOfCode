# INPUT
input = open("input.txt")
n = str(input.readline()).split(",")
nodebook = {}

x = y = 0
for direction in n:
    if direction == "n":
        y += 1

    if direction == "ne":
        x += 1

    if direction == "se":
        x += 1
        y -= 1

    if direction == "s":
        y -= 1

    if direction == "sw":
        x -= 1

    if direction == "nw":
        x -= 1
        y += 1

    key = str(x)+" "+str(y)

    if key not in nodebook:
        nodebook[key] = 1
    else:
        nodebook[key] += 1

print(x, y)

nw = 0
w = 0

steps = 0
while w != x:
    steps += 1
    nw += 1
    w -= 1

#print(w, nw, steps)
steps += y-nw
print(steps)