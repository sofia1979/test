#from tkinter import *

#window = Tk()
#window.title("Моє перше вікно")

#text = Label(window,text="Hello,world")

#button1 = Button(text="кнопка 1")
#button2 = Button(text="кнопка 2",command=lambda: print("натиснута кнопка 2"))

#text.pack()
#button1.pack()
#button2.pack()

#window.mainloop()


from tkinter import *

window = Tk()
window.title("Моє перше вікно")

def show_text():
    info = inputs_from_tk.get()
    print(f'Текст в ентрі є: {info}')

frame1 = Frame(window,bg='green',bd=5)

text = Label(window,text="Напишіть щось",fg="#607394",font='Ariel')
inputs_from_tk = Entry(window)
button1 = Button(frame1,text="Показати текст",command=show_text)

frame1.pack()
text.pack(pady=10)
inputs_from_tk.pack()
button1.pack(pady=5)

window.mainloop()