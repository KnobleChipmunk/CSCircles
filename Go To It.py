def findLine(prog, T):
    for i in range(0, len(prog)):
        swivel = prog[i].split()
        if T == swivel[0]:
            return i
        elif T == 'END':
            return i
        else:
            continue
