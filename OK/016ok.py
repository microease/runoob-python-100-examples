# 输出指定格式的日期。
import datetime
import time

print(datetime.date.today())
print(datetime.date.today().strftime('%Y/%B/%d'))
local_time = time.localtime()
# print(time.strftime("%Y年%m月%d日", local_time))
