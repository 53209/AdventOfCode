# INPUT
input = open("example_input.txt")

firewall = {}
for _ in range(0, 4):
    n = str(input.readline()).strip().split()
    firewall[int(n[0])] = int(n[1])


for i in range(0, 85):
    if i not in firewall:
        firewall[i] = 0

print(firewall)

severity = 0
for picosecond in range(0, 7):
    layerRange = firewall[picosecond]

    if layerRange == 0:
        continue

    # Calculate position of scanner when entering layer
    scannerPos = 0
    coefficient = 1
    for _ in range(0, picosecond):
        scannerPos += 1 * coefficient
        if scannerPos == (layerRange - 1):
            coefficient = -1    # returning
        if scannerPos == 0:
            coefficient = 1     # forward

    # Next Scanner step
    next_scannerPos = scannerPos + 1*coefficient
    # print("Picosecond: %s,\n LayerRange: %s,\n current ScannerPos: %s, \n next ScannerPos: %s" % (picosecond, layerRange, scannerPos, next_scannerPos))

    # Calculate severity
    if next_scannerPos == 0:    # caught
        print("Picossecond: %s, \n severity: %s, \n layerrange: %s" % (picosecond, severity, layerRange))
        severity += picosecond*layerRange

print(severity)