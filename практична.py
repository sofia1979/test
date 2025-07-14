spusok = ['поїсти', 'пограти']
print('Ось твій список справ:\n')
print(spusok)
s = int(input('Що ти хочеш зробити?\n 1- Додати завдання\n 2- Видалити завдання\n 3-Переглянути список завдань\n 4-редагування існуючих завдань.\n'))
if s == 1:
    slovo = input('Що ви бажаєте додати?\n')
    spusok.append(slovo)
    print(spusok)
elif s == 2:
    slovo2 = input('Що ви бажаєте видалити?\n')
    spusok.remove(slovo2)
    print(spusok)
elif s == 3:
    print(spusok)
elif s == 4:
    slovo3 = input('який елемент ви бажаєте змінити?\n')
    slovo4 = input('На який елемент ви хочете це замінити?\n')
    spusok.remove(slovo3)
    spusok.append(slovo4)
    print(spusok)
else:
    print('Ми незнаємо такої функції')
