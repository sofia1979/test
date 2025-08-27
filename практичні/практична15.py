from tkinter import *

window = Tk()
window.title("додаток художника")
window.geometry('400x400')

def color_red():
    window.config(bg='red')

def color_blue():
    window.config(bg='blue')

def color_green():
    window.config(bg='green')

def color_yellow():
    window.config(bg='yellow')

def color_purple():
    window.config(bg='purple')

def color_orange():
    window.config(bg='orange')

menubar = Menu(window)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="червоний", command=color_red)
menu1.add_command(label="синій", command=color_blue)
menu1.add_command(label="зелений", command=color_green)
menu1.add_command(label="жовтий", command=color_yellow)
menu1.add_command(label="фіолетовий", command=color_purple)
menu1.add_command(label="помаранчевий", command=color_orange)

menubar.add_cascade(label="Вибір кольору", menu=menu1)

window.config(menu=menubar)

window.mainloop()