import os

for i in range(51, 101):
    res = "0" + str(i) + ".py"
    # print(type(res))
    open("%s" % res, "w+")
