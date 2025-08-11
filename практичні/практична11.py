from tkinter import *

homik = Tk()
homik.title('Auto Clicker')
homik.geometry('300x300')
homik.config(bg='lightblue')

l1 = Label(homik, text='Auto Clicker', fg='#4F7972', font=('Arial', 20), bg='lightblue')
l1.pack(side='top', pady=10)

l2 = Label(homik, text='Кліків на секунду', fg='#4F7972', font=('Arial', 15), bg='lightblue')
l2.pack(side='top', pady=15)


inputs = Entry(homik)
inputs.pack(side='top', pady=20)

b1 = Button(homik, text='Почати', fg='white', bg='#5CBE31', font=('Arial', 14))
b1.pack(side='left', padx=20)

b2 = Button(homik, text='Вийти', fg='white', bg='#E13232', font=('Arial', 14), command=homik.destroy)
b2.pack(side='right', padx=50)

homik.mainloop()