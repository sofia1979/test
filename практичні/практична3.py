#Напиши програму, яка виводить числа від 1 до 30,
#але замість чисел, кратних 3, виводить "Три",
#а замість кратних 5 — "П’ять".
#Замість кратних 15 виводь "ТриП’ять".


# for - цикл лічильник - цикл діапазону

# range(start)

# x = range(7)
#
# for e in x:
#     print(e)

# range(start, stop)

# x = range(7,16)
#
# for e in x:
#     print(e)

# range(start, stop, step)

# x = range(1,20,2)
#
# for e in x:
#     print(e)

# summa = []
# for element in range(1,100):
#     if element % 2 == 0:
#         summa.append(element)
#
# print(f'Сума усі парних чисел {summa}')

#spisok = ['Nestor', 'Yakiv', 'Maxim']

#for student in spisok:
#    if student == 'Yakiv':
#        continue
#    else:
#        print(f'{student+" топовий стундент"}')
#    print('перевірка чи завершилась ітерація')

# pass - просто пропускає якийсь момент у коді, який ми сказали пропустити
# continue - ламає ітерацію
# break - ламає цикл


for chusla in range(1,31):
    if chusla % 3 == 0:
        print('Три')
    elif chusla % 5 == 0:
        print('П ять')
    elif chusla % 15 == 0:
        print('Три, П ять')
    else:
        print(chusla)

