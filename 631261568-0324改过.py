# 杨辉三角
# 行数
numberOfLine = 10    #要求输入而不是提前规定


lastLine = []
thisLine = []

for line in range(numberOfLine):   #可以用range(1,numberOfLine+1)，就可以不用在循环里+1了，减少可能发生的错误，还有变量的大小写要统一，要么都大写，要么都小写。
    line = line + 1             # 当前行数
    for i in range(numberOfLine - line):
        print("\t", end="")     # 1 打出总行数 - 当前行数个tab

    print('1', end="")
    thisLine.append(1)          # 2 打出第一个“ 1 ”并记录在列表中

    for i in range(line - 2):
        if line < 3:
            break               # 若为前两行，不需要打非1数字
        num = lastLine[i] + lastLine[i + 1]
        print("\t\t", end="")
        print(num, end="")
        thisLine.append(num)        # 3 根据上一行数据打出非1数字并记录

    if line > 1:
        print("\t\t", end="")
        print(1, end="")
        thisLine.append(1)          # 4 打出最后一个1

    print("")
    lastLine = thisLine
    thisLine = []                   # 5 换行并将当前行 -> 上一行



#算法有点繁杂，可以看之后给出的示例，写注释是一个好习惯，希望保持

#10 20190327 20:53


