# when u write len(45654) it gives type error we need to write string not integer
# num_char = str(len(input("whats your name?\n")))
# print("Your name has " + num_char + " characters")
# print(type(num_char))
print(5 + 5.5) # when summing int with float it becomes float automatically

print(70 + float("100.5")) # type conversion
print(str(70) + str(100)) # type conversion

print("---------------------")
num = input("type a two digit number\n")
num_0 = int(num[0])
num_1 = int(num[1])
result = num_0 + num_1
print(result)
