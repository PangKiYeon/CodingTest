a,b = map(int, input().split())
c = int(input())

a += ((b+c)//60)%24
b = (b+c) % 60

if a>=24: a -= 24
    
print(a, b)