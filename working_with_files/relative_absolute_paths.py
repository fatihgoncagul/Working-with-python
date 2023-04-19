# .. two dot represents previous directory
# ./ acceses current working directory


with open("C:/Users/fatih/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("../level_up/list__dict_compherensions/my_file2.txt") as file2:
    contents = file2.read()
    print(contents)