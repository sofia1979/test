import os
from customtkinter import *
from customtkinter import CTkLabel


def write_login_in_txt_file():
    login_text = user_login.get()
    if login_text:
        with open('login.txt', 'a', encoding="utf-8") as login_file:
            login_file.write(f"{login_text}\n")

def everything_is_good():
    user = user_login.get()
    l2.configure(text='Дані збережено')

def on_finish():
    write_login_in_txt_file()
    everything_is_good()




login_window = CTk()
login_window.title('Логін')
login_window.geometry("400x400")

l1 = CTkLabel(login_window, text='Введіть логін 👇🏻', font=('Arial', 30), fg_color='darkblue', bg_color='black')
l1.pack(pady=25)

user_login = CTkEntry(login_window, font=('Arial', 16))
user_login.pack(pady=30)

l2 = CTkLabel(login_window, text='', text_color='green', font=('Arial', 24))
l2.pack()

b1 = CTkButton(login_window, text='Завершити', font=('Arial', 30), fg_color='darkgreen', command=on_finish)
b1.pack(side='left', padx=20, pady=50)

b2 = CTkButton(login_window, text='Вийти', font=('Arial', 30), fg_color='darkred', command=login_window.destroy)
b2.pack(side='right', padx=20, pady=50)


login_window.mainloop()
