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

# 对于列表、元组、字典的操作
print("\n\n----------对于列表、元组、字典的操作")
# 解包
p = [1, 2, 3]
a, b, c = p
print(a, b, c)

# 依次访问
p = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(p[1:8:2])
print(p[3:5])

# in
print(1 in p)
print(0 in p)
print(0 not in p)

# all 若所有项目都是true，则返回true
print(all(p))
p = list(p)
print(type(p))
p += [0]
p.append(-1)
print(p)
print(all(p))

# any 有一个true 则true
print(any(p))

# min max len sum
print(min(p))
print(max(p))
print(sum(p))
print(len(p))

# 一种创建方式
q = (3, 4, 6, 8)
a = [i for i in p]
print(a)
a = [i for i in p if i not in q]
print(a)

# 列表操作
print("\n\n--------------列表操作")
s = [1, 2, 3, 4, 5, 6]
print(s)
s.append(3)
print(s)
print(s.count(3))
print("remove")
try:
    s.remove(0)
except Exception:
    print("Exception!")  # todo: find the exception name

print(s)
s.insert(3, 4)
print("insert")
print(s)
print(s.pop())
print(s)
s.reverse()
print(s)
s.sort()
print(s)
s.sort(reverse=True)
print(s)
s.clear()
print(s)

# 字典操作
print("\n\n-----------字典操作")
d = {1: 'a', 2: 'b', 3: 'c'}
print(d)
d[4] = 'd'
print(d)
print(d.get(2))
n = d.items()
print(type(n))  # 迭代器
print(n)
for i in n:
    print(i)
print(type(d))
print(n)
print("---------")
print(d.pop(2))  # 字典的 pop() 方法必须有参数
print(d.popitem())
print(d)

# 字符串操作
print("\n\n-----------字符串操作")
s = "abc def abc"
print(s.count('a'))
print(s.find('b'))
print(s.find('v'))
print(s.index('c'))
try:
    print(s.index('v'))
except ValueError:
    print("ERROR: ValueError - can not find this letter")

# upper lower
print(s.upper())
print(s.lower())

# split replace
print(s.split(' '))
print(type(s))
print(type(s.split()))
print(s.replace('a', 'r'))

# 字符串格式化
print("\n-----------字符串格式化")
a = 34
b = 21.356543359
c = "hello"
d = {'x': 12, 'y': "cdefg", 'z': 23.23465778765}
e = 34567654390654654896654

s = "a is %d or %10d" % (a, a)
print(s)
s = "%+010d \t %.4f %.4g %e" % (a, b, b, b)  # g 有效数字
print(s)
s = "%(x)-10d \t %(z).8g" % d  # 符号左对齐
print(s)
s = "%8.4s %0.4s %s" % (c, c, d['y'])
print(s)
s = "%*.*f" % (5, 3, b)  # 共5位，小数点后三位
print(s)
# 更复杂的可用format
