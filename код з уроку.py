from tkinter import *
from PIL import ImageTk, Image

def on_left_click(event):
    print("ліва кнопка миші була клікнута")

def on_right_click(event):
    print("права кнопка миші була клікнута")

def on_middle_click(event):
    button.configure(bg="blue")
    print('навівся на кнопку')

def on_enter(event):
    print("Курсор увійшов на віджет")

def on_leave(event):
    button.configure(bg="red")
    print("Курсор вийшов з віджета")

def on_mouse_wheel(event):
    print(f"Колесо миші прокручено: {event.delta}")


window = Tk()
window.title("Events")
window.geometry("600x400")

image = Image.open("example.png")
photo = ImageTk.PhotoImage(image)

label = Label(window, image=photo, bg="lightgrey")
label.pack(expand=True, anchor="center")
button = Button(window, text="кнопка", bg='red')
button.pack(expand=True, anchor="center")

# bind(що ми слухаємо(який event), функцію)
# <Button-1> - ліва кнопка
# <Button-3> - права кнопка
# <Enter> - курсор знаходиться над віджетом, або увійшо в поле віджета
# <Leave> - курсор вийшов за межі віджета
# <MouseWheel> - прокручення колесиком миші

label.bind("<Button-1>", on_left_click)
label.bind("<Button-3>", on_right_click)
label.bind("<MouseWheel>", on_mouse_wheel)
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

button.bind("<Enter>", on_middle_click)
button.bind("<Leave>", on_leave)

window.mainloop()