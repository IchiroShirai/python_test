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

def tomodachi():
    for friend in names:    
        print(friend)

tomodachi()    

# task6

tomodachi2 = tomodachi()

print(tomodachi2)    