m = int(input())
n = int(input())
result = 0
answer = []
for i in range(10001):
    result = i**2
    if m <= result <= n:
        answer.append(result)

if answer == []:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])