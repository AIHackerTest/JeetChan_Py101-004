""" print,格式化和Python2有区别 """
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))  # 格式化，替代大括号
print("And everywhere that Mary went.")
print("." * 10)  # 可以用’乘‘操作符输出多个符号

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# 和Python2不同的是'end'参数，该参数可以设置print连接符
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
