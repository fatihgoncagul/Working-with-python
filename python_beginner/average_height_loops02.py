# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above, sum method usage
totel_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(totel_height / number_of_students)
print("total height: " + str(totel_height))
print(average_height)
# Write your code below this row 👇 below is a way with for loops
print("---------")
total_h = 0

for height in student_heights:
    total_h += height
av_height = round(totel_height / len(student_heights))
print("total height: " + str(total_h))

print(av_height)
