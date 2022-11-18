array = list(map(int, input().split()))
sort_a = sorted(array)
rev_a = sorted(array, reverse=True)
if array == sort_a:
    print("ascending")
elif array == rev_a:
    print("descending")
else:
    print("mixed")
