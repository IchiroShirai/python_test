# 課題2　task1
class Myclass :
    code = None
    name = None
    price = None
def say(self) :
    print("商品コード:{0}、商品名:{1}、価格:{2}" .format(self.code,self.name,self.price))    

fruits1 = Myclass()
fruits1.code = "001"
fruits1.name = "りんご"
fruits1.price = "100円"

fruits1.say()