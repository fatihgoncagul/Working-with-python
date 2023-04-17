# for loops with range
#for number in range(1,11,3):
# print(number)

for number in range(1,10): # 1 to 10, 1 included not including 10
    print(number)
print("-------------- below for loop, adds 3 to each step")
for number in range(1,11,3):
    print(number)
print("-------------- below for loop, adds all numbers between 1 to 100")
total = 0
for number in range(1,101):
    total += number
print(total)
print("--------- below lets calculate sum off all even numbers from 1 to 100")
total = 0
for number in range(1,101):
    if number %2==0:
        total += number
print(total)
# or you can do it this way
total = 0
for number in range(0,101,2):
    total += number
print(total)
#total of odd numbers
print("--------- below lets calculate sum off all odd numbers from 1 to 100")
total =0
for number in range(1,101,2):
    total += number
print(total)