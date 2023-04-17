import another_module

print(another_module.another_variable)

# import turtle
# from turtle import Turtle, Screen
#
# timmy = turtle.Turtle() #  constucting object
# timmy2 = Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen.exitonclick()
from prettytable import  PrettyTable

print(" pokemon name  |   type")

table = PrettyTable()

table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electiric", "Water", "Fire"])

print(table)
print(table.align)
table.align = "l"
print(table)
