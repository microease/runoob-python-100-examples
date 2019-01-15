# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# coding=utf-8


x = int(input("请输入一个正整数："))
temp = []
while x != 1:
    for i in range(2, x + 1):
        if x % i == 0:
            temp.append(i)
            x = x / i
            break

print(temp)
