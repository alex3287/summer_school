# НОД (GCD) => Наибольший общий делитель
# 12  8 => 1, 2, 4 !
# -8 -2 => 2
# -24 -12 => 12 (abs(num))
# -10 16 => 2
# 0 16 => 16
# 16 15 => 1 !
# 34 34 => 34
# 0 0 => плохо

# 16 24 => 16 8 => 8 8
# 9 14 => 9 5 => 4 5 => 4 1 => 3 1 => 2 1 => 1 1

num_1 = int(input())
num_2 = int(input())
num_1 = abs(num_1)
num_2 = abs(num_2)
# тест № 8
# if num_1 == 0 and num_2 == 0:
#     print('на 0 делить нельзя')
# else:
while num_1 != num_2:
    if num_1 > num_2:
        num_1 = num_1 - num_2
    else:
        num_2 = num_2 - num_1

print(num_1)