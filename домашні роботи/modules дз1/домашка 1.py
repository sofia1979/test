print('****************************************')
print('|Вітаю у спрощеній програмі калькулятор|')
print('****************************************')

k = int(input('яку математичну дію ти хочеш зробити?\n 1 - відняти;\n 2 - поділити\n 3 - додати\n 4 - помножити\n'))

if k == 1:
    import minusModule
    a = int(input('Введи перше число, яке ти хочеш відняти\n'))
    b = int(input('Введи друге число, яке ти хочеш відняти\n'))
    print(minusModule.vidnimanna(a, b))

elif k == 2:
    import divisionModule
    a = int(input('Введи перше число, яке ти хочеш поділити\n'))
    b = int(input('Введи друге число, яке ти хочеш поділити\n'))
    print(divisionModule.dilenna(a, b))

elif k == 3:
    import plusModule
    a = int(input('Введи перше число, яке ти хочеш додати\n'))
    b = int(input('Введи друге число, яке ти хочеш додати\n'))
    print(plusModule.dodavanna(a, b))

elif k == 4:
    import multModule
    a = int(input('Введи перше число, яке ти хочеш помножити\n'))
    b = int(input('Введи друге число, яке ти хочеш помножити\n'))
    print(multModule.mnogenna(a, b))

else:
    print('Ми не знаємо такої математичної функції')
