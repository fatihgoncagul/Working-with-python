student_dict = {
    "student" : ["angela","james","lilly"],
    "score": [56, 76,98]
}

for (key,value) in student_dict.items():
    print(value)

import pandas as pd

# create data frame from dictionary
student_DataFrame = pd.DataFrame(student_dict)
print(student_DataFrame)

for (index, row) in  student_DataFrame.iterrows():
    print(index)

for (index, row) in  student_DataFrame.iterrows():
    print(row)

for (index, row) in  student_DataFrame.iterrows():
    print(row.student)
    if row.student == "angela":
        print(row.score)

