# 题目：暂停一秒输出，并格式化当前时间。
import time

local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(local_time)
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
