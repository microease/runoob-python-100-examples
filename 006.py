# 题目：斐波那契数列。
# coding=utf-8
def Fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(Fib(10))
