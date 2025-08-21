from tkinter import *
import random

window = Tk()
window.title('зміна кольору фону')
window.geometry('600x200')

def change_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    window.config(bg=random.choice(colors))

label = Label(window, text='натисни enter, щоб змінити колір', bg='lightyellow')
window.bind('<Return>', change_color)
label.pack(expand=True, anchor="center")


window.mainloop()


