# Завдання:
# Створи вікно де ти привітаєшся з користувачем.
# Використай цікавий шрифт та колір для тексту.

# Наприклад:
# `Вітаю у програмі "назва програми".
# Аби зайти у програму скажіть, як вас звуть?`

# Людина має увести своє імя та натиснути на кнопку - увійти.

# Опісля кліку на кнопку "увійти" - виведи в консоль: Вітаю, "ім'я людини".

# Крім кнопки - увійти - також має бути кнопка - вийти - при кліку на яку вікно буде закриватись(знищуватись).

# Завдання із зірочкою: Нехай текст, введений у поле користувачем, відображатиметься у лейблі.


from tkinter import *
wikno = Tk()
wikno.title('Вхід користувача')
wikno.geometry('700x700')


def show():
    user = inputs_from_tk.get()
    print(f'Текст: {user}')
    success_label.config(text='Успішний вхід')


ramka = Frame(wikno,bg='blue',bd=6)
text = Label(wikno,text='Вітаю у моїй першій програмі :)',fg='#D4C04E',font='lobster')
button1 = Button(ramka,text="увійти",command=show)
inputs_from_tk = Entry(wikno)
button2 = Button(ramka,text="вийти",command=wikno.destroy)

success_label = Label(wikno, text='', fg='green', font=('Arial', 14))

text.pack(pady=15)
ramka.pack()
inputs_from_tk.pack()
button1.pack(pady=7)
button2.pack(pady=10)
success_label.pack(pady=10)

wikno.mainloop()

#--------------------------------------------------------------

window = Tk()
window.title('Атрибути')
window.geometry("300x300")

firstLabel = Label(window,text='first label', width=15, height=5)
secondLabel = Label(window,text='second label', width=15, height=5)
thirdLabel = Label(window,text='third label', width=15, height=5)

firstLabel.place(x=50,y=20)
secondLabel.place(x=150,y=100)
thirdLabel.place(relx=0.5,rely=0.2,anchor="center")

window.mainloop() 