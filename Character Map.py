x = ord(' ')

for i in range(0,6):
    print('chr:'+' ', end=' ')
    for j in range(x,x+16):
        print(chr(j)+'  ', end=' ')
    print()   
    print('asc:', end=' ')
    for u in range(x,x+16):
        if u >= 100:
            print(str(u), end=' ')
        else:
            print(str(u)+' ', end=' ')
    print()
    x += 16
