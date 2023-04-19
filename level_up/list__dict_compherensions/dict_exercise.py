sentence = "what is the airspeed velocity of an unladen swallow?"

word_list = sentence.split()

dict = { word: len(word) for word in word_list }
print(dict)
dict2 = { word: len(word) for word in sentence.split() }
print(dict)

print("------------dict, turn celcius to fahreneit")
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    day:value*9/5+32 for (day, value) in weather_c.items()
}
print(weather_f)