try:
    print("a"+1)
except:
    print("上面的代码写错了")


try:
    print("a"+1)
except Exception as e:
    print("上面的代码写错了",e)

    # Exception  异常类  as  ： 重命名     Exception as e ： 把这个异常类 崇明名为e
    #注意  当你把py文件放入你在这里新建的文件夹当中  如果你是中文你就会出现乱码 而且没有办法用 tab键补全