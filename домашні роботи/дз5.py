import os

with open('daily.txt', 'w', encoding="utf-8") as file:
    file.write("поїсти\n")

while True:

    user = int(input('У тебе є список справ, що ти хочеш з ним зробити?\n 1 - Показати всі справи\n 2 - Додати нову справу\n 3 - Очистити всі справи\n 4 - Вийти з програми\n'))
    if user == 1:
        with open('daily.txt', 'r', encoding="utf-8") as file:
            tasks = file.read()
            print(tasks)


    elif user == 2:
        with open('daily.txt', 'a', encoding="utf-8") as file:
            text = input('напиши, що ти хочеш додати:\n')
            file.write(text + '\n')
        print('Справу додано 😊, ось твій список:')
        with open('daily.txt', 'r', encoding="utf-8") as file:
            tasks = file.read()
            print(tasks)


    elif user == 3:
        with open('daily.txt', 'w', encoding="utf-8") as file:
            tasks = file.write('')
        print('список очищено 👌:')
        with open('daily.txt', 'r', encoding="utf-8") as file:
            tasks = file.read()
            print(tasks)


    elif user == 4:
        print('Допобачення 👋🏻')
        break

    else:
        print('я не знаю такої операції зі списком 🫤. спробуйте ще раз')
