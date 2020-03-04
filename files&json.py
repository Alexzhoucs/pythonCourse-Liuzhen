text = '''This is a test string. \n\
123345567 \n\
阿斯蒂芬'''

# 擦除后写入
f1 = open('testfile1.txt', 'w')
f1.write(text)
f1.close()


# 使用with块
with open('testfile1.txt', 'w') as f2:
    f2.write('again:')
    f2.write(text)


# 增加文件内容
with open('testfile1.txt', 'a') as f3:
    f3.write(text)

# 读取文件
filename = 'testfile1.txt'
with open(filename, 'r') as f4:
    print(f4.readline())
    print('\n---')
    print(f4.read())
print('\n---')

with open(filename, 'r') as f5:
    for line in f5:
        print(line, end='')
print('\n---')

with open(filename, 'r') as f6:
    a = f6.readlines()
    print(a)
    # 删除末尾字符
    for i in a:
        print(i)
        i = 'ad'
        print(i)
    print('----=----')
    for i in a:
        print(i)
    # 循环中更改列表内容的正确操作
    for i in range(len(a)):
        a[i] = a[i].rstrip()
    print(a)

import json

data = [{'name': 'alex', 'age': 22, 'sex': True}, {'name': 'elinor', 'age': 22, 'sex': False}]
jsdata = json.dumps(data)
print(jsdata)
with open('1.json', 'w') as f1:
    json.dump(data, f1)

with open('2.json', 'w') as f2:
    f2.write(jsdata)

with open('1.json', 'r') as f1:
    d1 = json.load(f1)
print('d1', d1)
print(type(d1))

with open('2.json', 'r') as f2:
    tmp = f2.read()
    d2 = json.loads(tmp)
print('d2', d2)
print(type(d2))
