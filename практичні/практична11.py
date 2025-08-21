from tkinter import *
from tkinter import messagebox
import time
import keyboard
import mouse



running = False # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0 # змінна, що зберігатиме тривалість перерви після кожного кліку

def exit_app():

    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    homik.destroy() # Закриття вікна Tkinter


def start_clicker():
    global running, delay # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(user.get())
    delay = 1 / clicks_per_second # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу.")
    running = True

    # Запуск процесу кліків
    schedule_click()


def schedule_click():
    if running:
        mouse.click()
        time.sleep(delay) # затримка між кліками
        schedule_click() # функція знову викликає сама себе


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

homik = Tk()
homik.title('Auto Clicker')

screenWidth = homik.winfo_screenwidth()
screenHeight = homik.winfo_screenheight()

newWidth = screenWidth // 2
newHeight = screenHeight // 2

homik.geometry(f"{newWidth}x{newHeight}")
homik.config(bg='lightblue')

l1 = Label(homik, text='Auto Clicker', fg='#4F7972', font=('Arial', 20), bg='lightblue')
l1.pack(side='top', pady=10)

l3 = Label(homik, text='Інформація:\n Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!\n Ти можеш вийти задопомогою кнопки ESC на клавіатурі', bg='grey', fg='white', font=('Arial',14))
l3.pack(side='top')

l2 = Label(homik, text='Кліків на секунду', fg='#4F7972', font=('Arial', 15), bg='lightblue')
l2.pack(side='top', pady=5)

user = Entry(homik, width=30, font=('Arial', 15))
user.pack(side='top', pady=30)

frame_b1 = Frame(homik, bg='darkgreen')
frame_b1.pack(side='left', padx=20, pady=20, expand=True)

frame_b2 = Frame(homik, bg='darkred')
frame_b2.pack(side='left', padx=20, pady=20, expand=True)


b1 = Button(frame_b1, text='Почати', fg='white', bg='#5CBE31', font=('Arial', 24), command=start_clicker)
b1.pack()

b2 = Button(frame_b2, text='Вийти', fg='white', bg='#E13232', font=('Arial', 24), command=homik.destroy)
b2.pack()

keyboard.add_hotkey('esc', exit_app)

homik.mainloop()