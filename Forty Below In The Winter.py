temp = input()
list = []
tempList = []
if temp.endswith("F" or "f"):
    for i in range(0, len(temp)):
         if temp[i] == 'F':
             list.append(temp[i])
         elif temp[i] == 'f':
             list.append(temp[i])
         elif temp[i] == '-':
             list.append(temp[i])
         elif temp[i] != '-':
             tempList.append(temp[i])       
    f = ''.join(tempList)
    if list[0] == '-':
        c = (float(f) * (-1) - 32) * (5 / 9)
    else:
        c = (float(f) - 32) * (5 / 9)
    print(str(c)+'C')
elif temp.endswith("C" or "c"):
    for i in range(0, len(temp)):
         if temp[i] == 'C':
             list.append(temp[i])
         elif temp[i] == 'c':
             list.append(temp[i])
         elif temp[i] == '-':
             list.append(temp[i])
         elif temp[i] != '-':
             tempList.append(temp[i])       
    c = ''.join(tempList)
    if list[0] == '-':
        f = (float(c) * (-1)) * (9 / 5) + 32
    else:
        f = float(c) * (9 / 5) + 32
    print(str(f)+'F')
