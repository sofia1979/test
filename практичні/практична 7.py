while True:

    try:


        t = int(input('введи суму гривень для конвертації 🤑\n'))
        k = input('введи у яку валюту ви хочете конвертувати гривні (EUR 💶/USD 💵)\n')

        if k == 'EUR':
            i = (t / 47.59)
            print(f'{i} євро')

        elif k == 'USD':
            a = (t / 41.65)
            print(f'{a} доларів')

        else:
            print('я не знаю таку валюту 🫣')

    except ValueError:
        print('введи число, а не текст 🫥😶‍🌫️')
