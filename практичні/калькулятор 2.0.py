from customtkinter import *
from customtkinter import CTkEntry
import tkinter as tk

def set_theme(theme):

    if theme == "light":
        calculator.configure(bg_color='white')
        display.configure(fg_color='lightgray', text_color='black')
        for btn in buttons:
            btn.configure(fg_color="#BEC2E9", text_color="black")


    elif theme == "dark":
        calculator.configure(bg_color='black')
        display.configure(fg_color='gray', text_color='white')
        for btn in buttons:
            btn.configure(fg_color="#5D5D5F", text_color="white")

    elif theme == 'yellow':
        calculator.configure(bg_color='#F5D243')
        display.configure(fg_color='#F8E327', text_color='black')
        for btn in buttons:
            btn.configure(fg_color="#F9C408", text_color="black")

    elif theme == 'green':
        calculator.configure(bg_color='darkgreen')
        display.configure(fg_color='green', text_color='black')
        for btn in buttons:
            btn.configure(fg_color="#184F0A", text_color="black")

    elif theme == 'red':
        calculator.configure(bg_color= '#830D0D')
        display.configure(fg_color='#FE0A0A', text_color='black')
        for btn in buttons:
            btn.configure(fg_color="#7B0F0F", text_color="white")

def on_button_click(button):

    pass

calculator = CTk()
calculator.geometry('340x500')
calculator.title = 'Калькулятор'


display = CTkEntry(calculator, font=('Arial', 34), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

temu = tk.Menu(calculator)
tema1 = tk.Menu(temu, tearoff=0)
tema1.add_command(label="light", command=lambda: set_theme('light'))
tema1.add_command(label="dark", command=lambda: set_theme('dark'))
tema1.add_command(label="yellow", command=lambda: set_theme('yellow'))
tema1.add_command(label="green", command=lambda: set_theme('green'))
tema1.add_command(label="red", command=lambda: set_theme('red'))

temu.add_cascade(label='тема', menu=tema1)
calculator.configure(menu=temu)

buttons = []
button_texts = [
'1', '2', '3', '/',
'4', '5', '6', '*',
'7', '8', '9', '-',
'C', '0', '=', '+'
]
row_val = 1
col_val = 0


for text in button_texts:
    btn = CTkButton(calculator, text=text, font=('Arial', 36), width=70, height=70)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    buttons.append(btn)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

calculator.mainloop()