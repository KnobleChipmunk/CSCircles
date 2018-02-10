n=int(input())
for i in range(0 , n):
    x = 0
    for j in range(i , n):
        x = (x * 10) + 1
    print(x)
