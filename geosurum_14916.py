n = int(input())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        break
    if n == 1:
        result = -1
        break
    n -= 2
    result += 1

print(result)