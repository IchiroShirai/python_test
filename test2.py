# # 課題2　task1

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def order(self):
        print(self.item_code, self.item_name, self.price,"円")

ringo = Item("001", "りんご", 100) 
ringo.order()
 




# class Myclass :
#     def __init__(self,code,name,price):
#         self.code = code
#         self.name = name    
#         self.price = price

# ringo = Myclass(001, "りんご", 100)
# ringo.print

# def say(self) :
#     print("商品コード:{0}、商品名:{1}、価格:{2}" .format(self.code,self.name,self.price))    

# fruits1 = Myclass()
# fruits1.code = "001"
# fruits1.name = "りんご"
# fruits1.price = "100円"

# fruits1.say()

# # 商品クラス
# class Item:
#     def __init__(self,item_code,item_name,price):
#         self.item_code=item_code
#         self.item_name=item_name
#         self.price=price
    
#     def get_price(self):
#         return self.price

# # オーダークラス
# class Order:
#     def __init__(self,item_master):
#         self.item_order_list=[]
#         self.item_master=item_master
    
#     def add_item_order(self,item_code):
#         self.item_order_list.append(item_code)
        
#     def view_item_list(self):
#         for item in self.item_order_list:
#             print("商品コード:{}".format(item))
    

# def main():
#     # マスタ登録
#     item_master=[]
#     item_master.append(Item("001","りんご",100))
#     item_master.append(Item("002","なし",120))
#     item_master.append(Item("003","みかん",150))
    
#     # オーダー登録
#     order=Order(item_master)
    
#     # 注文
#     order.add_item_order("001")
#     order.add_item_order("002")
#     order.add_item_order("003")
    
#     # オーダー表示
#     order.view_item_list()
    
# if __name__ == "__main__":
#     main()