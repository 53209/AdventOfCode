input = "63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24".replace(",", " ").split()
lengths = [int(x) for x in input]
circle = [ x for x in range(0, 256)]
testCircle = [ x for x in range(0,5)]
# print(list(reversed(lengths[:3])).append(lengths[3:]))


def reverseSublist(currentpos, length):
    sublist = []
    for _ in range(0, length):
        sublist.append(circle[currentpos])
        currentpos += 1
        if currentpos >= len(circle):
            currentpos = 0
    return list(reversed(sublist))


def integrateSublist(sublist, currPos):
    length = len(sublist)
    sublist_idx = 0
    for _ in range(0, length):
        circle[currPos] = sublist[sublist_idx]
        currPos += 1
        sublist_idx += 1
        if currPos >= len(circle):
            currPos = 0

def goToPosition(currentPosition, currentLength, skipSize):
    for i in range(0, currentLength):
        currentPosition += 1
        if currentPosition >= len(circle):
            currentPosition = 0

    for j in range(0, skipSize):
        currentPosition += 1
        if currentPosition >= len(circle):
            currentPosition = 0
    return currentPosition



# DEBUG
test_reverse = reverseSublist(249, 10)
integrateSublist(test_reverse, 249)
newPosition = goToPosition(249, 10, 2)
# print(newPosition)
# print(circle[newPosition])
# print(circle)


skipSize = 0
currentPos = 0
for length in lengths:
    sublist = reverseSublist(currentPos, length)
    integrateSublist(sublist, currentPos)
    currentPos = goToPosition(currentPos, length, skipSize)
    skipSize += 1

print(circle[0]*circle[1])

