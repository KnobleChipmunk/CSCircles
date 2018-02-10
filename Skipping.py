counter = 0
while True:
    lineIn = input()
    if lineIn=='END':
        break
    if lineIn=='SKIP':
        continue
    counter = counter+1
    print('line', counter, '=', lineIn)
