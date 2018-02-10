def check(S):
    if len(S) != 19:
        return False
    elif S[4] != ' ':
        return False
    elif S[9] != ' ':
        return False
    elif S[14] != ' ':
        return False
    else:
        sumList = []
        i = 0
        while len(sumList) < 19:
            sumList.append(S[i])
            i += 1
        while ' ' in sumList:
            sumList.remove(' ')
        i = 0
        strList = []
        for i in range(0, len(sumList)):
            if sumList[i].isdigit() == False:
                return False
            else:
                strList.append(int(sumList[i]))
                i += 1
        sumS = sum(strList)
        strL = ''.join(sumList)
        if not strL.isdigit():
            return False
        elif sumS % 10 == 0:
            return True
        else:
            return False
