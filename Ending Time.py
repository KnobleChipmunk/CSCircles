startingTime = input()
d = int(input())

colon = ":"

if startingTime.find(colon) != -1:
    subOne = int(startingTime[0:startingTime.find(colon)])
    subTwo = int(startingTime[startingTime.find(colon)+1:len(startingTime)])
    subTwo = int(subTwo) + d
   
    if subTwo >= 60:
        subOne = subOne + int(subTwo // 60)
        subTwo = 00 + (subTwo % 60)
        subTwo = "{0:0=2d}".format(subTwo)

    if subOne >= 24:
        subOne = 00 + (subOne % 24)
        subOne = "{0:0=2d}".format(subOne)
   
    elif subOne <= 12:
        subOne = "{0:0=2d}".format(subOne)

print(str(subOne) + colon + str(subTwo))
