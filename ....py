from tkinter import *

def show(user_choice):
    if user_choice == 1:
        output_label.config(text='запускаю таймер на 6 хв ⏱️...')
    elif user_choice == 2:
        output_label.config(text='запускаю таймер на 9 хв ⏱️...')
    elif user_choice == 3:
        output_label.config(text='запускаю таймер на 12 хв ⏱️...')
    elif user_choice == 4:
        output_label.config(text='Тоді допобачення 👋🏻!')
        vikno.destroy()
    else:
        output_label.config(text='щось пішло не так 🫤, спробуй ще раз 😉')

vikno = Tk()
vikno.title('Варіння яйця')
vikno.geometry('400x300')

Label(vikno, text='Як ти хочеш зварити яйце?').pack(pady=10)

Button(vikno, text='1 - з рідким жовтком 🍳', command=lambda: show(1)).pack(pady=5)
Button(vikno, text='2 - з густим жовтком 🥚', command=lambda: show(2)).pack(pady=5)
Button(vikno, text='3 - з синім жовтком 🔵', command=lambda: show(3)).pack(pady=5)
Button(vikno, text='4 - вже не хочу нічо варити 😵', command=lambda: show(4)).pack(pady=5)

# Ось цей Label показуватиме результат
output_label = Label(vikno, text='', fg='green', font=('Arial', 12))
output_label.pack(pady=20)

vikno.mainloop()
