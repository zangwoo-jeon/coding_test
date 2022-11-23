n = int(input())
array = []
for _ in range(n):
    a = input()
    array.append(a)

array = list(set(array))
array.sort()
array.sort(key=lambda x: len(x))

for i in array:
    print(i)
