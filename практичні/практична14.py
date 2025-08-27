import customtkinter
from customtkinter import CTkEntry, CTkLabel, CTkButton

window = customtkinter.CTk()

def show_text():
    text = entry.get()
    label.configure(text=text)

label = CTkLabel(window, text="Вітання, я вікно", font=("Arial",25))
label.pack()

entry = CTkEntry(window)
entry.pack()

button = CTkButton(window, text="Показати введений текст", command=show_text)
button.pack()

window.mainloop()

#customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")