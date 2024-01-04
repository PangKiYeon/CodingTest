n = int(input())
n  = m = 2*n-1
h = 0

for i in range(0, m):
    if i < m/2 - 1:
        for j in range(0,n):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        n -= 1
    else:
        for j in range(0,n):
            if j <= i - 2*h-1:
                print(" ", end="")
            else:
                print("*", end="") 
        n += 1
        h += 1
    if i != m-1:
        print("")