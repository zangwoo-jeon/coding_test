array = []

for _ in range(5):
    a = list(map(str, input().split()))
    array.append(a)

result = 0
for i in array:
    A = int(i[0][0] + i[0][1])
    B = int(i[1][0] + i[1][1])
    C = int(i[0][3] + i[0][4])
    D = int(i[1][3] + i[1][4])
    result += (B - A) * 60 + (D - C)
print(result)
