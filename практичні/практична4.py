user = input(print('напиши слово, а ми зашифруємо його:'))
golosni = ['а', 'е','є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
prugolosni = ['б', 'в', 'г', 'ґ', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


for bycvu in user:
        if bycvu in golosni:
            print(0)
        elif bycvu in prugolosni:
            print(1)
        else:
            break
