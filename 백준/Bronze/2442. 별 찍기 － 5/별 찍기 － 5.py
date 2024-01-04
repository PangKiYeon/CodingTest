n = m = int(input())

for i in range(0,n):
    m += 1
    for j in range(0, m):
        if n - i - 1 <= j <= n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    if i != n-1:
        print("")