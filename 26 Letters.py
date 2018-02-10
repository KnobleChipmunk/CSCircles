letter = input()
if int(ord(letter)) <= int(ord('@')) or int(ord(letter)) >= int(ord('[')):
    print('invalid')
else:
    print((ord(letter)-65)+1)
