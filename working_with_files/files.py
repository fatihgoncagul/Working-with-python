# read write

file = open("my_file.txt")
contents = file.read()
print(f"{contents} and 111")
file.close() # we need it, beacuse it might still use resources of our computer after program is done with the file

# we can use below method with indentation, so it knows when to close
# which is after you go out of that indented block
#contents = file.read()
#print(contents)
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# writing file

with open("my_file2.txt",mode="a") as file2:
    # open method's second parameter "mode"'s default is set to 'r' (read only)
    # so we need to change that # by writng 'w' (clears and adds what you want)
    # if you write 'a', it just appends
    file2.write("new text2, appended")

