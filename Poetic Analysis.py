lineList = []
line = input()
while line != '###':
    lineList.append(line) 
    line = input()
lineList.append(line)
splitList = []
for i in range(0, len(lineList)):
    splitList.append(lineList[i].split())
lowerList = []
for i in range(0, len(splitList)):
    for j in range(0, len(splitList[i])):
        lowerList.append(splitList[i][j].lower())
max = 0
for x in lowerList:
    count = lowerList.count(x)
    if count > max:
        max = count
        maxItem = x
print(maxItem)
