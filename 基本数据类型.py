# 输出

# print(type("你好 我是好学习的小直"))  #字符串
# print(type(2333))             #整数
# print(type(6.77))             #小数
# print(type(True))             #布尔值
# print(type((2,3)))             #元组
# print(type([3,4]))              #数组
# print(type({1:"学习"}))          #字典

# print("喜欢你"*100)     #运算符
# print(2<3)              #逻辑判断
# print("hahah","哈哈哈"+"123")

# a = "小直"
# c = "小Lo"
# print(a)
# print(c)
# print(a,c)
# print(a+c)
# print(3*(a+"喜欢"+c))

# # 输入
# a = input("请输入")
# print(a)


# a="jaifafnjnsnssk"
# b="jacnsvnsjdndkvhaha哈哈哈"
# print(len(a)+len(b))


# a=int(input("a是"))
# b=int(input("b是"))
# c=(a+b)/2
# print("等于",c)



# time=int(input("请输入分钟数："))
# if time<=60
# shi=int（time/60）
# fen=time%60
# print(shi+"时"+fen+"分")
# #第一次提交代码到gtihub
# print("大家都很努力 我也要加油")
# print("虽然说，是已经多次去进行 但是我现在的能力水准的话实在是 我自己感觉还不行")
# print("所以我就更要努力了啊啊啊啊啊")


# a = (2,3,4,(6,7),"我是","谁")
# print(a[4])
# print(a.index(3))
# print(a.count(3))

xinxi = {}
name=input("姓名")
sex=input("性别")
age=input("年龄")
# xinxi.update(xname=name)
# xinxi.update(xsex=sex)
# xinxi.update(xsge=age)
xinxi.update(name=name,sex=sex,age=age)     #update这个方法中 可以新建/修改多个值
print(xinxi)