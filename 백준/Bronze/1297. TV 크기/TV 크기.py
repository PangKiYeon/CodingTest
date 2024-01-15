import math

a, b, c = map(int, input().split())

    
x = a **2 / (b**2 + c**2)
x = x**0.5

print(math.floor(b*x), math.floor(c*x))