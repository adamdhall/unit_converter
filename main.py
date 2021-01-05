from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.wm_minsize(width=300, height=200)
window.config(padx=25, pady=25)


def convert():

    miles = float(entry.get())
    km= round(miles * 1.609)
    converted_value.config(text=f"{km}")


entry = Entry(width=5)
entry.grid(row=0, column=1)

# #Label
miles_label = Label(text="Miles", font= ("Arial", 16, "normal"))
miles_label.grid(row=0, column=2)

equal_to = Label(text="is equal to", font= ("Arial", 16, "normal"))
equal_to.grid(row=1, column=0)


converted_value = Label(text= "0", font= ("Arial", 16, "normal"))
converted_value.grid(row=1, column=1)

km_label = Label(text="Km", font= ("Arial", 16, "normal"))
km_label.grid(row=1, column=2)


button=Button(text="Calculate", command=convert)
button.grid(row=2, column=1)



window.mainloop()


