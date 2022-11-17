A, B = map(int, input().split())
array = []
result = 0

for i in range(1001):
    for j in range(i):
        array.append(i)

for i in range(A-1, B):
    result += array[i]

print(result)