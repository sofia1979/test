from tkinter import *

window = Tk()
window.title('My program')
window.geometry('350x350')

llabel = Label(window, text='Welcome', bg='lightgreen', fg='white', font=('Times New Roman', 42))
button = Button(window, text='Тиць!', bg='lightblue', fg='white', font=('Times New Roman', 30))



llabel.pack(padx=10, pady=20)
button.pack(padx=20, pady=20)

window.mainloop()