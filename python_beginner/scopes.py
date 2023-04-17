print("modify variables with global scope")
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}, this creates another variable")


increase_enemies()
print(f"enemies outside function: {enemies}, this uses enemies at global scope")


# local scope

def drinkpotion():
    potion_strentgh = 2
    print(potion_strentgh)


drinkpotion()
# we cant do this print(potion_strength)

# global scope

p_health = 10


def drink():
    potion_strnth = 2
    print(
        p_health)  # we can do this but we cant change p healt value with writing p_helth = 15, u can use that within the function tho.


# if you have nested functions, f1,f2. you cant use the inner one f2, outside of f1


def f1():
    def f2():
        pass


# f2() we cant do this because of the scope

# THERE IS NO BLOCK SCOPE

game_level = 3
enemies = ["skeleton", "zombi", "alisen"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)
# if u create a variable it is only avalaible in that function
# if, for, while, or anything has indentation or colon that does not count as a scope.
# block does not have a scope if you create a new variable inside you can use it

################################################
# modify variables with global scope
print("modify variables with global scope")
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# without using the global keyword
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


# python constants and global scopes

PI = 3.14
URL = "https:/www.google.com"

