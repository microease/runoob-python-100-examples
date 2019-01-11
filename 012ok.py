# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
# coding = utf-8
res = []
for i in range(101, 200):
    for j in range(2, i - 1):
        if i % j == 0:
            break
    else:
        res.append(i)
print(res)
print("总数为：%d" % len(res))
