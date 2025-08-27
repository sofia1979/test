from tkinter import *

window = Tk()
window.title("My app")

menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open")
menu1.add_command(label="Exit", command=window.quit)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Copy")
menu2.add_command(label="Paste")

menubar.add_cascade(label="File", menu=menu1)
menubar.add_cascade(label="Edit", menu=menu2)

window.config(menu=menubar)

window.mainloop()