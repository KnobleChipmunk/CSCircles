n = int(input())

for outer in range(1 , (n + 1)):
    for inner in range(1, (n+1)):
        if outer * inner == n:
            print(str(outer)+" times "+str(inner)+" equals "+str(n))   
