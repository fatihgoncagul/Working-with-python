# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
to_array = [char for char in position] #buna gerek yok, direkt position[0] yapabiliyosun!!!
# 🚨 Don't change the code above 👆
index_1 = int(to_array[0])
index_2 = int(to_array[1])
map[index_1-1][index_2-1] = "X"
print(f"{row1}\n{row2}\n{row3}")


#Write your code below this row 👇