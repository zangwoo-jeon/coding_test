T = int(input())

for _ in range(T):
    d = int(input())
    t = 0
    while (t+1) + (t+1)**2 <= d:
        t += 1
    print(t)
    
    '''
    count = 0
    for i in range(1, 101):
        if d >= i + i**2:
            count += 1
        else:
            print(count)
            break
    '''
    
