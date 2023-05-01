# In the name of Allah, the most beneficent the most merciful
from tkinter import *
FONT = ("Courier",15,"bold")
def calculate():
    miles = float(input.get())
    cal_km = round((miles * 1.609))

    km.config(text=cal_km)


window = Tk()
window.title(".....Riza's Miles-to-KM Converter.....")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input = Entry(width=11, font=FONT)
input.grid(row=0, column=1)


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_eq_label = Label(text="is equal to", font=FONT)
is_eq_label.grid(row=1, column=0)

km = Label(text="0", font=FONT)
km.grid(row=1, column=1)

km_label = Label(text="kilometers", font=FONT)
km_label.grid(row=1, column=2)

calculate_btn = Button(text="Calculate", command=calculate, font=FONT)
calculate_btn.grid(row=2, column=1)

window.mainloop()
