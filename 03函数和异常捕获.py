try:
    print("a"+1)
except:
    print("上面的代码写错了")


try:
    print("a"+1)
except Exception as e:
    print("上面的代码写错了",e)

    # Exception  异常类  as  ： 重命名     Exception as e ： 把这个异常类 崇明名为e