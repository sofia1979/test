import random

r = int(random.randint(1,10))
# функція яка виводить рандомне число від a до b
print('Давай пограємо у гру. Я загадаю число від 1 до 10, а ти спробуєш відгадати його\n')

while True: #запускає нескінченний цикл.
    k = int(input('Введи своє число:\n '))

    if k>r:
        print('я загадав менше число')
    elif k<r:
        print('Я загадав більше число')
    else:
        print('ти вгадав!!!')
        break  # вихід з циклу, коли користувач вгадав
