# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
source = int(input("请输入您的分数:"))
if source >= 90:
    grade = 'A'
elif source >= 60 and source < 90:
    grade = 'B'
else:
    grade = 'C'

print("%d 属于 %s" % (source, grade))
