# INPUT
input = open("input.txt")

firewall = []
for _ in range(0, 43):
    temp_list = []
    n = str(input.readline()).strip().split()
    temp_list.append(int(n[0]))
    temp_list.append(int(n[1]))
    firewall.append(temp_list)

print(firewall)

scanner = 0
for layer in firewall:
    range = layer[1]

    #Calculate position of scanner
