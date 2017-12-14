# INPUT
input = open("input.txt")
n = str(input.readline()).split(",")
nodebook = {}

def get_distance(x, y):
    nw = 0
    se = 0
    w = 0
    e = 0
    steps = 0

    if y == 0:
        steps = abs(x)
    elif x == 0:
        steps = abs(y)
    elif x < 0 and y > 0:
        while steps != abs(x):
            nw += 1
            steps += 1
        steps += (y-nw)
    elif x < 0 and y < 0:
        while steps != abs(x):
            w -= 1
            steps += 1
        steps += (abs(y)-abs(w))
    elif x > 0 and y > 0:
        while steps != abs(x):
            e += 1
            steps += 1
        steps += y
    elif x > 0 and y < 0:
        while steps != abs(x):
            w -= 1
            steps += 1
        steps += (abs(y)-abs(w))

    return steps


x = y = 0
distances = []

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
        distance = get_distance(x, y)
        #print(x, y, distance)
        distances.append(distance)
    else:
        nodebook[key] += 1


print(max(distances))