from customtkinter import *

EMERALD_IN_DIAMOND = 5
EMERALD_IN_NETHERITE = 50
DIAMOND_IN_NETHERITE = 5

def convert():
    try:
        number = float(chuslo.get())
        from_curr = from_currency_var.get()
        to_curr = to_currency_var.get()

        if from_curr == 'смарагди' and to_curr == 'діаманти':
            result = number / EMERALD_IN_DIAMOND
        elif from_curr == 'смарагди' and to_curr == 'незерит':
            result = number / EMERALD_IN_NETHERITE
        elif from_curr == 'смарагди' and to_curr == 'смарагди':
            result = number

        elif from_curr == 'діаманти' and to_curr == 'смарагди':
            result = number * EMERALD_IN_DIAMOND
        elif from_curr == 'діаманти' and to_curr == 'незерит':
            result = number / DIAMOND_IN_NETHERITE
        elif from_curr == 'діаманти' and to_curr == 'діаманти':
            result = number

        elif from_curr == 'незерит' and to_curr == 'діаманти':
            result = number * DIAMOND_IN_NETHERITE
        elif from_curr == 'незерит' and to_curr == 'смарагди':
            result = number * EMERALD_IN_NETHERITE
        elif from_curr == 'незерит' and to_curr == 'незерит':
            result = number

        result_label.configure(text=f'Результат: {result} {to_curr}')
    except ValueError:
        result_label.configure(text='Введи число!')

app = CTk()
app.title('конвертер майнкрафт')
app.geometry('400x300')

title_label = CTkLabel(app, text='Конвертер діамантів в смарагди', font=('Roboto',18))
title_label.pack(pady=10)

chuslo = CTkEntry(app, placeholder_text='введи суму')
chuslo.pack(pady=10)

from_currency_var = StringVar(value='смарагди')
from_currency_menu = CTkOptionMenu(app, variable=from_currency_var, values=['смарагди', 'діаманти', 'незерит'])
from_currency_menu.pack(pady=5)

to_currency_var = StringVar(value='діаманти')
to_currency_menu = CTkOptionMenu(app, variable=to_currency_var, values=['смарагди', 'діаманти', 'незерит'])
to_currency_menu.pack(pady=5)

b1 = CTkButton(app, text='Конвертувати', command=convert)
b1.pack(pady=5)

result_label = CTkLabel(app, text='')
result_label.pack(pady=10)


app.mainloop()
