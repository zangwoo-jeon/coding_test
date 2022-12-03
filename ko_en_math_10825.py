n = int(input())
array = []

for _ in range(n):
    name, ko, en, math = input().split()
    array.append((name, int(ko), int(en), int(math)))

array.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for a, b, c, d in array:
    print(a)
