# it has key and value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    123: "A piece of code that you can easily call over and over again.",

}


print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# adding new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# create empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "Böcek"
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
