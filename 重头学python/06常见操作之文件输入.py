# coding=gbk
tetx = input("请输入：")
with open("日记.txt","a") as f:
    f.write(tetx+"\n")

# w   写入。 每次写操作 都是把之间的清空的 再写入新的
# a   追加。 写入新的  但是不会清空之前有的内容
# \t
# \n  换行