# without list compherension

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

# with list compherension

new_list_2 = [n + 1 for n in numbers]
print(new_list_2)

name = "angela"
letters_list = [letter for letter in name]
print(letters_list)
print("--------------- with range")
range_list = [num*2 for num in range(1, 5)]
print(range_list)
print("--------------- with conditional")
names = ["alex", "beth", "caroline","dave","eleanor","freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# squarred numbers

numbers = [1,1,2,3,5,8,13,21,34,55]

squarred_numbers = [num**2 for num in numbers]
print(squarred_numbers)

# filtering even numbers

even_numbers = [num for num in numbers if num %2 ==0 ]
print(even_numbers)

# data overlap
print("---------- find data overlap")
with open("file1.txt") as file1:
    file1_data = file1.readlines()


with open("file2.txt") as file2:
    file2_data = file2.readlines()


result = [int(num) for num in file1_data if num in file2_data]

print(result)