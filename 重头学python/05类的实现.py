class GrilFriend():
    def __init__(self,name,age,high,weigt):
        self.name = name
        self.age = age
        self.high = high
        self.weigt= weigt
    def Lashi(self):
        print("叫做"+self.name+"的人他"+self.age+"岁高"+self.high+"重"+self.weigt+"他正在")
        print("拉屎中")


gril = GrilFriend("小直","18","180cm","50kg")         #实例化
gril.Lashi()
