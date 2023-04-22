

# file not found error
# with open("a_file.txt") as file:
#     file.read()

# try catches, try, except(catch), else(if theres no exception do this), finally(do this anyway)

try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"]) # if key exist it goess into else stmt, if it doesnt it does not go into else
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as message:
    print(f"that key {message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("end of try-except, file is closed")


# raising our own exceptions it is done with 'raise' keyword

height = float(input("height : "))
weight = int(input("weigt: "))

if height >3:
    raise ValueError("human height should not be over 3 meters")


bmi = height/weight**2
print(bmi)















