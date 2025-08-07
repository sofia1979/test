print('напиши число, а я виведу квадратний корінь')

import math

while True:

    try:

        number = int(input('введи число\n'))

        result = (math.sqrt(number))
        print(result)

    except ValueError:
        print('від ємні числа не можна писати!')