n = int(input())
result = []
answer = []
for _ in range(n):
    A = input()
    result.append(A[0])

sett = list(set(result))

for i in range(len(sett)):
    if result.count(sett[i]) >= 5:
        answer.append(sett[i])

if answer == []:
    answer.append("PREDAJA")
answer.sort()
for i in answer:
    print(i, end="")