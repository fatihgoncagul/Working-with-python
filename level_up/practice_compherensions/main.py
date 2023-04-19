student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(f"\n {student_data_frame}")
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(f"{index} {row.student} {row.score}")

    # Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
print("-------------- NATO ALPHAPET")
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data_dict = data.to_dict()
# data dict does not give us the format we want so we use below compherension
dict = {row.letter : row.code for  (index,row) in data.iterrows() }
print(dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word: ").upper()
# useful compherension
output_list = [dict[letter] for letter in word ]
print(output_list)