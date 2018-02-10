S = input()
j = "+"

if S.find(j) != -1:
    subOne = S[0:S.find(j)]
    subTwo = S[S.find(j)+1:len(S)]

print(int(subOne) + int(subTwo))
