import os

os.mkdir("C:/Users/sophi/OneDrive/Робочий стіл/windows")
with open("C:/Users/sophi/OneDrive/Робочий стіл/windows/passwod.txt", "w", encoding="utf-8") as meow:
    meow.write("котохакер передає тобі привіт😈😊")

with open("C:/Users/sophi/OneDrive/Робочий стіл/windows/passwod.txt", "r", encoding="utf-8") as meow:
    text = meow.read()
    print(text)
