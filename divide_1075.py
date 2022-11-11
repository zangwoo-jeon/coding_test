n = int(input())
f = int(input())

for i in range(10):
    for j in range(10):
        n = n // 100
        n = n*10 + i
        n = n*10 + j
        if n % f == 0:
            print(str(i)+str(j))
            exit()