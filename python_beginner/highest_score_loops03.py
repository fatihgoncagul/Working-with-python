# 🚨 Don't change the code below 👇 find highest score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆 we can do it with max func but lets do it with loops
print(max(student_scores))
#Write your code below this row 👇 # my sol
highest_score = 0;
for n in range(0,student_scores.__len__()-2):
    highest_score = student_scores[n]
    if highest_score < student_scores[n+1]:
        highest_score = student_scores[n+1]
print(f"the highest score is: {highest_score}")
# ############# another way
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"the max score is: {max_score}")
