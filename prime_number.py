# Natural number > 1
# Which only has 2 factors: 1 & itself
#
# 17 => 1 & 17 => Prime Number
# 28 => 1, 2, 4, 7, 14, 28 => Not a Prime Number

num = 19
count = 0

if num > 1:
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Number is Prime")
    else:
        print("Number is not Prime")


