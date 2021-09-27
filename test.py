# task1

name1 : str = "シンジ"
name2 : str = "カヲルくん"

print(f"{name1} と {name2} は仲良し")


# task2

if name2 == "使徒です!":
   print("使徒です!")


# task3

names: list =["シンジ", "レイ", "カヲルくん"]
print(names)
names.append("アスカ")
print(names)

# task4

for friend in names:
 print(friend)

#  task5

def tomodachi() -> None:
    names: list =["シンジ", "レイ", "カヲルくん"]
    names.append("アスカ")
    for friend in names:    
        print(friend)

tomodachi()    

# task6

def tomodachi2(mari: str):
    names: list = ["シンジ", "レイ", "カヲルくん"]
    names.append("アスカ")
    names.append(mari)
    for friend in names:
        print(friend)


tomodachi2("マリ")


#  task7

names: list = ["シンジ", "レイ", "カヲルくん"]
input_name: str = input("名前を入力してください：")
if input_name in names:
    print(f"{input_name}はいます。")
else:
    print(f"{input_name}はいません。")