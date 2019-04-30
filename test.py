from random import randint
a = randint(2, 9)
a1 = randint(1, a-1)
b1 = randint(10, 99)
b2 = randint(10, 99)
b3 = b1 * b2
c = a * b1
c1 = a * b1 + a1
addnum1 = randint(1000, 9999)
addnum2 = randint(1000, 9999)
addnum3 = addnum1 + addnum2

print(c, "/", a, "=", end=' ')

answer = int(input())
if answer == b1:
    print("正确")
else:
    print("错误")
print()