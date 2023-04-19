import csv
import pandas # data analysis package
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    # for row in data:
    #     print(row)

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data)) # type = data frame

print(data["temp"])
print(type(data["temp"])) # type = series (a column), kind of a list

print("-------------------- panda ops")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist() # turn column into a list
print(temp_list)
print(type(temp_list[0])) # elements in the list are integers

average = sum(temp_list) / len(temp_list)
print(average)
print(data["temp"].mean())
print(data["temp"].max())
print(data["condition"])  # this treats data as an dictionary
print("-----------------")
print(data.condition)  # this treats data as an object

# get data from row
print("----------------- get data from row")

print(data[data.day =="Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day =="Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

print(" create a dataframe from scratch")

data_dict = {
    "students" : ["amy", "angela", "james"],
    "scores" : [76, 55, 52]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data_csv")
print(data["students"].__len__())
print(data["students"][0])