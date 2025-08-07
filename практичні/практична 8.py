while True:

    try:

        chuslo1 = int(input('введи перше число, яке ти хочеш поділити\n'))
        chuslo2 = int(input('введи друге число, яке ти хочеш поділити\n'))
        vidpovid = (chuslo1/chuslo2)
        print(vidpovid)

    except ZeroDivisionError:
        print('на нуль ділити не можна')

