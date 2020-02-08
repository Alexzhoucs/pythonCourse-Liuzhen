# 函数
print("---------------函数")
def multi(x, y):
    return x ** y


print(multi(3, 2))


def multi1(x, y=2):
    return x ** y


print(multi1(3))
print(multi1(3, 3))
print(multi1(y=3, x=2))


def multi2(x, y=2):
    return x ** y, x, y


a, b, c = multi2(3)
print(type(a))
print(a)
a = multi2(3)
print(type(a))
print(a)


def multi3(x, y=2):
    global b                    # 将外部的b拉入修改，结果会影响外部
    print(b)
    b = b + 1
    print(a)                    # 函数中a并未被定义
    return x**y


print(multi3(4))
print(b)

