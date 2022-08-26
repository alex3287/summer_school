# 5 = 1*2*3*4*5

n = int(input())

f = 1
for i in range(1, n+1):
    f *= i

print(f)