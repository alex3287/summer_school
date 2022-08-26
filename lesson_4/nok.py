# 2 3 => 6
# 12 6 => 12

# 36 24 => 72
# 36 => 2 2 3 3
# 24 => 2 2 2 3
# 2 2 2 3 3

# 1 34 => 34

# НОК = (num_1 * num_2) / НОД(num_1, num_2)
# НОК = (12 * 6) / 6

num_1, num_2 = map(int, input().split())

mult = num_1 * num_2

while num_1 != num_2:
    if num_1 > num_2:
        num_1 -= num_2
    else:
        num_2 -= num_1

result = mult // num_2

print(result)

# 3/4 2/6
# nok = 12
# (3 * (nok/6) + 2 * (nok/4)/12
# 12/12 => нод
