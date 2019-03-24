# 杨辉三角
# 行数
numberOfLine = 10
#
# testString = '''begin:
#                 1
#             1       1
#         1       2       1
#     1       3       3       1
# 1       4       6       4       1'''
#
# print(testString)

lastLine = []
thisLine = []

for line in range(numberOfLine):
    line = line + 1
    for i in range(numberOfLine - line):
        print("\t", end="")     # 1

    print('1', end="")
    thisLine.append(1)          # 2

    for i in range(line - 2):
        if line < 3:
            break
        num = lastLine[i] + lastLine[i + 1]
        print("\t\t", end="")
        print(num, end="")
        thisLine.append(num)        # 3

    if line > 1:
        print("\t\t", end="")
        print(1, end="")
        thisLine.append(1)          # 4

    print("")
    lastLine = thisLine
    thisLine = []






