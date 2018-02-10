def getBASIC():
    list = []
    n = input()
    while True:
        line = n
        if n.endswith('END'):
            list.append(line)
            return list
        else:
            list.append(line)
            newN = input()
            n = newN
