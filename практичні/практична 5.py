while True:

    try:

        numberOne = int(input('введи перше число\n'))
        numberTwo = int(input('введи друге число\n'))
        mark = input('введи знак + - /\n')

        if mark == '+':
            print(numberOne + numberTwo)

        elif mark == '-':
            print(numberOne - numberTwo)

        elif mark == '/':
            print(numberOne / numberTwo)

        else:
            print('Ти ввів не ту дію')

    except ValueError:
        print('Пише ввести ЧИСЛО, а не букву!')
