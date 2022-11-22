n, m = map(int, input().split())

result = 0
while True:
    target = (n//m)*m
    result += (n-target)
    n = target
    if n < m:
        break
    result += 1
    n //= m

result += (n-1)
print(result)
