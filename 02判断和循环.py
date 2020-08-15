# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end="  ")
#     print()
# #九九乘法表


# for h in range(1,4):
#     print("黄红绿")
#     h=h+1
# for r in range(4,31):
#         print("  红绿")
#         r=r+1
# for g in range(31,36):
#             print("   绿")
#             g=g+1

# # #打印红绿灯  黄灯3次  红灯30次 绿灯35次  注意缩进
# light = {"黄灯":3,"红灯":30,"绿灯":35}
# for i in light:
#     for j in range(light[i]):
#         print(i,"还有",light[i]-j,"秒")

# c=1
# p=1
# xinxi = {}
# while c:
#     username = input("账号：")
#     if len(username)>=5 and len(username)<=8:
#         if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#             xinxi["账号"]=username
#             while p:                    #多谢一个循环
#                 password = input("密码：")
#                 if len(password)>=6 and len(password)<=12:
#                     xinxi["密码"]=password
#                     print("注册成功",xinxi)
#                     exit()

#                 else:
#                     print("请输入6-12位密码")   #问题出现在这个地方
#                     p=1   #这里调回到第二个while 而不是之前的c=1（调回第一个while）               
#         else:
#             print("账号必须以小写字母开头")
#             c=1
#     else:
#             print("请输入5-8账号")
#             c=1
# exit()  #最后的成功
#现在有一个问题就是  账号输入符合的时候 如果密码不符合的话  一直输到密码合适  但是此时又会进入新的账号输入 此前的密码前功尽弃

#哇 经过一番琢磨  我出来结果啦哈哈哈哈哈哈哈   为了让上一步成功的账号能够保存  
# 一定要让密码这一步 跳会到账号正确之后的代码块  而不是直接回到原地的while



#新的问题就是 不知道为什么成功之后 还跳回第一个循环
#好了 我在和第一个while的平级 的最后加了一个exit()  成功了！

# #老师的
# u= input("账号：")
# p= input("密码：")
# if len(u)>=5 and len(u)<=8:
#     if u[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         if len(p)>=6 and len(p)<=12:
#             print("注册成功",{u:p})
#         else:
#             print("请输入6-12位密码")

#     else:
#         print("账号必须是小写字母开头")
# else:
#     print("账号必须是5-8为")


# def checkname(u):
#     if len(u)>=5 and len(u)<=8:
#         if u[0] in "qwertyuioplkjhgfdsazxcvbnm":
#             print("ok")
#         else:
#             print("账号必须是小写字母开头")
#     else:
#         print("账号必须是5-8为")


# checkname("qjfosn")

# # 两个数相加
# def jia(a,b):
#     c=a+b
#     print("两个数的和是",c)

# yi=int(input("请输入第一个数："))
# er=int(input("请输入第二个数："))
# jia(yi,er)


