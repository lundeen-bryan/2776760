from tkinter import *

'''============================================
=            Constants Section                =
============================================'''
WIN_HEIGHT = 100
WIN_WIDTH = 200

'''========  End of Constants Section      ====
'''
def button_clicked():
  miles = my_input.get().capitalize().strip()
  km = float(miles) * 1.609
  value_label.config(text=str(km))

win = Tk()
win.title("Miles to Km Converter")
win.minsize(width=WIN_WIDTH, height=WIN_HEIGHT)
win.config(padx=WIN_HEIGHT/3, pady=WIN_WIDTH/3, bg="white")

# Label
equal_label = Label(text="is equal to", font=("Arial", 18, "normal"))
equal_label.grid(column=0, row=1)
equal_label.config(bg="white")
equal_label_info = equal_label.grid_info()

# Label 2
value_label = Label(text="0", font=("Arial", 18, "normal"))
value_label.grid(column=equal_label_info["column"]+1, row=equal_label_info["row"])
value_label.config(bg="white")
value_label_info = value_label.grid_info()

# Label 3
km_label = Label(text="Km", font=("Arial", 18, "normal"))
km_label.grid(column=equal_label_info["column"]+2, row=equal_label_info["row"])
km_label.config(justify="left")
km_label.config(bg="white")
km_label_info = km_label.grid_info()

# Data entry
my_input = Entry(width=5, font=("Arial", 18, "normal"), justify="center")
my_input.grid(column=1, row=0)
input_info = my_input.grid_info()

# Label 4
mi_label = Label(text="Miles", font=("Arial", 18, "normal"))
mi_label.grid(column=km_label_info["column"], row=km_label_info["row"]-1)
mi_label.config(padx=20, anchor="w", bg="white")
mi_label_info = mi_label.grid_info()

# new Button
new_button = Button(text="calculate", command=button_clicked, width=my_input["width"]-5, font=("Arial", 12, "normal"))
new_button.grid(column=input_info["column"], row=input_info["row"]+2)
new_button_info = new_button.grid_info()





win.mainloop()