# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
random_int = random.randint(0,names.__len__()-1)

print(f"the person wholl pay for all of you is {names[random_int]}")

fruits = ["strwbr","nectarine", "apple"]
vegatables = ["spinach","kale", "tomatoes"]
dirty_dozen = [fruits,vegatables]
print(dirty_dozen[1])
