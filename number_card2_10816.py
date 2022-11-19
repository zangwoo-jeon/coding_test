from bisect import bisect_left, bisect_right

n = int(input())
sanguen_card = list(map(int, input().split()))
sanguen_card.sort()
m = int(input())
find = list(map(int, input().split()))
result = []
def count_bisect(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

for i in find:
    count = 0
    count += count_bisect(sanguen_card, i, i)
    result.append(count)

for i in result:
    print(i, end=" ")
