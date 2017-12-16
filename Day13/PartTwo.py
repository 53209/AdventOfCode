# INPUT
input = open("example_input.txt")

firewall = {}
for _ in range(0, 4):
# for _ in range(0, 43):
    n = str(input.readline()).strip().split()
    firewall[int(n[0])] = int(n[1])

for i in range(0, 7):
# for i in range(0, 85):
    if i not in firewall:
        firewall[i] = 0

# print(firewall)

severities = []
for delay in range(0, 20):
    severity = 0
    for picosecond in range(0, 7):
    # for picosecond in range(0, 84):

        # print("curent Pico: %s" % (picosecond))
        layerRange = firewall[picosecond]

        if layerRange == 0:
            # print("LR0: %s" % (picosecond))
            continue

        # Calculate position of scanner when entering layer
        scannerPos = 0
        coefficient = 1
        for _ in range(0, (picosecond + delay)):
            scannerPos += 1 * coefficient
            if scannerPos == (layerRange - 1):
                coefficient = -1  # returning
            if scannerPos == 0:
                coefficient = 1  # forward

        # Next Scanner step
        next_scannerPos = scannerPos + 1 * coefficient
        # print("Pico+Del: %s,\n LayerRange: %s,\n current ScannerPos: %s" % (picosecond+delay, layerRange, scannerPos))

        # Calculate severity
        if scannerPos == 0:  # caught
            severity += (picosecond+delay) * layerRange
            # print(severity)

    severities.append(severity)

print(severities)