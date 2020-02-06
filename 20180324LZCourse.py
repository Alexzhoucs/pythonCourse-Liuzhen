# 20180324刘真
# 声明变量直接赋值 不用考虑double

a = 1
print(type(a))
b = 1.2
print(type(b))
c = "asdf\nasdf"
print(type(c))
print(c)
d = r"asdf\nasdf"
print(d)

# 原生字符串
b = r"adsfg"

# 复数
a = complex(1 + 2j)

# 列表
a = [0, 1, 2, 3]

# 元组 不可变有序  常用来接收返回值
a = (2, 3, 4, '5', (0, 1, 2))

# 字典 无序
a = {'a': 1, 'b': 2, 'c': 3}
print(type(a))
print(a)

# 集合 自动去重，自动排序
a = {1, 2, 8, 4, 5}
print(a)
b = {1, 2, 'a', 5, 23, 6, 'z', 'b'}
print(b)
print(type(b))

# ---- print
print(a, end='')
print(a)
f = open("1.txt", 'w')
print(a, file=f)

# 字符串格式化


# 键盘输入 所有输入都是字符串

#
# a = input("请输入：")
print(a)
print(type(a))

# if语句

a = 1
b = [3, 2, 1]

if a in b:
    print(b)
elif a is b:
    print(a)

# for
for i in range(2, 10, 3):
    print(i)

a = "abcdefg"
for i in a:
    print(i)

print("---")
a = {1: 256, 3: 4}
for i in a:
    print(i, a[i])


# 定义函数
def devid(a, b):
    p = a / b
    q = a // b
    s = a % b

# 文件、上下文管理器
