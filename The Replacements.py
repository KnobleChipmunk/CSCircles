def replace(list, X, Y):
    while X in list:
        j = 0
        for n in list:
            pos = (len(list)+ j) - ((len(list)))
            if n == X:
                list.insert(pos, Y)
                list.remove(X)
                j += 1 
            elif list.count(X) == 0:
                break
            else:
                j += 1
                continue
