m, n, k = map(int, input().split())

A = input().split()
B = input().split()
A = "".join(A)
B = "".join(B)

if A in B:
    print("secret")
else:
    print("normal")
