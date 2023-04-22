from tkinter import *
# remember: tkinter has time countdown stuff and canvas, you can add images etc.

def mile_to_km():
    print()
    miles = miles_input.get()
    print(miles)
    km = float(miles) * 1.609
    kilometer_label.config(text=f"{km} km")


window = Tk()

window.title("miles to kilometer converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="calculate",command=mile_to_km)
calculate_button.grid(column=1,row=2)




window.mainloop()