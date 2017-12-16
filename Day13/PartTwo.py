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
severity = 0
for delay in range(1000000, 10000000):
    severity = 0
    caught = False
    for picosecond in range(0, 85):

        layerRange = firewall[picosecond]

        if layerRange == 0:
            continue

        scannerPos = (picosecond+delay) % ((layerRange-1)*2)

        if scannerPos == 0:
            caught = True
            severity += (picosecond+delay) * layerRange

    if severity == 0 and not caught:
        print(delay)
        break