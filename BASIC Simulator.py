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

def findLine(prog, T):
    for i in range(0, len(prog)):
        swivel = prog[i].split()
        if T == swivel[0]:
            return i
        elif T == 'END':
            return i
        else:
            continue

def execute(prog):
    location = 0
    visited = [False] * len(prog)
    while True:
        if prog[location]==prog[len(prog)-1]: return "success"
        elif visited[location] == True: return "infinite loop"
        visited[location] = True
        T = prog[location].split()
        location = findLine(prog, T[len(T)-1])

print(execute(getBASIC()))
