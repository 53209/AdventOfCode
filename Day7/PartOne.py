tower = []

for _ in range(0,1039):
    n = input().replace(",","").strip().split()
    #n = n.replace(",","")
    tower += n

s = set(tower)
print(len(tower))
print(len(s))

for element in tower:
    if "(" in element:
        tower.remove(element)
    if "-" in element:
        tower.remove(element)

temp = {}
for element in tower:
    if element not in temp:
        temp[element] = 1
    else:
        temp[element] += 1

print(temp)
