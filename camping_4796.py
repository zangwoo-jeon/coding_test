test = 0
while True:
    test += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    divide = v // p
    result = l * divide
    if v - p*divide > l:
        result += l
    else:
        result += v % p

    print("Case {}:".format(test), result)
