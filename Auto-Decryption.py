value = []
goodList = []
S = 0
    #Adds the message into a temporary list and checks for alphabeticals or spaces
def caesarCode(code):
    tempList =  []
    for letter in code:
        tempList.append(letter)			
    return goodList[value.index(goodness(tempList))]

    #Determines value of each message.
def goodness(list):
    global value, goodList, S,  msg
    letterGoodness = [.0817,.0149,.0278,.0425,.1270,.0223,.0202,.0609,
                      .0697,.0015,.0077,.0402,.0241,.0675,.0751,.0193,
                      .0009,.0599,.0633,.0906,.0276,.0098,.0236,.0015,
                      .0197,.0007]
    goodValue = 0
    position = 0
    for c in list:
        if position == len(list)-1:
            goodValue += float(letterGoodness[ord(c)-65])
            value.append(goodValue)
            joinList = ''.join(list)
            goodList.append(joinList)
            S += 1
            if S == 27:
                return finalValue(goodList)
            else:
                return letterBump(joinList)
        elif c == ' ':
            position += 1
            continue
        else:
            goodValue += float(letterGoodness[ord(c)-65])
            position += 1
            
    #Cycles through the alphabet for each letter in the message.
def letterBump(codeList):
    global msg, S
    while True:
        A = 90 - S                       
        position = 0
        nextList = []
        for i in codeList:
            if position == len(codeList)-1 and ord(i) <= 89:			
                nextList.append(chr(ord(i)+1))							   
                return goodness(nextList)
            elif position == len(codeList)-1 and ord(i) > 89:		
                nextList.append(chr((ord(i)-25)))						
                return goodness(nextList)
            elif codeList[position] == ' ':								
                nextList.append(' ')
                position += 1
            elif ord(i) >= 65 and ord(i) <= 89:
                nextList.append(chr(ord(i)+1))
                position += 1
            elif ord(i) > 89:
                nextList.append(chr((ord(i)-25)))
                position += 1

def finalValue(goodness):
    vSum = 0.0
    position = 0
    while position < len(value):
        for v in value:
            if float(v) > float(vSum):
                vSum = float(v)
                position += 1
        return vSum
            
print(caesarCode(input()))
