T = int(input())

for _ in range(T):
    d = int(input())
    count = 0
    for i in range(1, 101):
        if d >= i + i**2:
            count += 1
        else:
            print(count)
            break