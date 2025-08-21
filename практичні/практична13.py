from tkinter import *
window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

label = Label(text=f'ширина вікна {screen_width}, висота вікна {screen_height}', font='Arial,32', bg='blue', fg='yellow')



new_width = screen_width // 2
new_height = screen_height

label.pack(pady=250, padx=40)


window.geometry(f"{new_width}x{new_height}")

window.mainloop()
