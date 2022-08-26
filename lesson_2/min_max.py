
N = int(input())
mini = 10001

for i in range(N):
    num = int(input())
    if num < mini:
        mini = num

print(mini)

