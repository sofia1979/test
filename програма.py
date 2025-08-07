import time
from tkinter import *

def show(user):


    if user == 1:
        timer.config(text='запускаю таймер на 6 хв ⏱️.\n Коли пройде 6 хв - зможеш припиняти варити яйце 😉')
        minutes = 6


    elif user == 2:
        timer.config(text='запускаю таймер на 9 хв ⏱️.\n Коли пройде 9 хв - зможеш припиняти варити яйце 😉')
        minutes = 9


    elif user == 3:
        timer.config(text='запускаю таймер на 12 хв ⏱️.\n Коли пройде 12 хв - зможеш припиняти варити яйце 😉')
        minutes = 12


    elif user == 4:
        timer.config(text='Тоді допобачення 👋🏻!')
        window.destroy()


    else:
        timer.config(text='схоже щось пішло не так 🫤, спробуй ще раз 😉')


window = Tk()
window.title('варіння яйця')
window.geometry('700x500')

user = Label(window, text='Як ти хочеш зварити яйце?', fg='#D758A9', font=('Arial',24), bg='#D4D758')

button1 = Button(window, text='1 - з рідким жовтком 🍳', fg='#D6C558', font='Arial', bg='#1F1D34', command=lambda: show(1))
button2 = Button(window, text='2 - з густим жовтком 🥚', fg='#D7A658', font='Arial', bg='#1F1D34', command=lambda: show(2))
button3 = Button(window, text='3 - з синім жовтком 🔵', fg='#8158D5', font='Arial', bg='#1F1D34', command=lambda: show(3))
button4 = Button(window, text='4 - вже не хочу нічо варити 😵', fg='#D55868', font='Arial', bg='#1F1D34', command=lambda: show(4))


timer = Label(window,text='', fg='#532323', font=('Arial', 18), bg='#A337EB')
timer.pack(pady=40)


user.pack(pady=10)
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=5)


window.mainloop()