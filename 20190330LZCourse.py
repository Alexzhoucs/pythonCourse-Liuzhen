# 异常处理
print("----------异常处理")
a = -10
b = 2
# b = input("input b ")

try:
    c = a / int(b)
    print(c)
except:  # 此处IDE报错：too broad exception clause，希望精确指定异常类型（见下一个try块）
    print("b should not be 0!")
else:
    print("good!")
finally:
    print("finish! ")


# 断言 可用在try块中
print("\n\n-------------断言")
try:
    assert a > 0
except AssertionError:  # 此处加上了异常类型：断言失败
    print("ERROR: a < 0")
finally:
    print("assert finish")


# 集合的操作
print("\n\n-----------集合的操作")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print("a | b \t 并集")
print(a | b)
print("a & b \t 交集")
print(a & b)
print("差集")
print("a - b")
print(a - b)
print("b - a")
print(b - a)


