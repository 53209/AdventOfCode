# INPUT
input = open("input.txt")

firewall = {}
for _ in range(0, 43):
    n = str(input.readline()).strip().split()
    firewall[int(n[0])] = int(n[1])

for i in range(0, 85):
    if i not in firewall:
        firewall[i] = 0

scannerPos = 0
caught = False
for delay in range(1000000, 10000000):
    caught = False
    for picosecond in range(0, 85):

        layerRange = firewall[picosecond]

        if layerRange == 0:
            continue

        scannerPos = (picosecond+delay) % ((layerRange-1)*2)

        if scannerPos == 0:
            caught = True
            break

    if not caught:
        print(delay)
        break