n = list(map(int, input()))

count = 0

start = n[0]

for i in range(len(n)-1):
    if n[i] != n[i+1] and start != n[i+1]:
        count += 1

print(count)
