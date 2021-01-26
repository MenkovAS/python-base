"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться
после них."""

raiting = []

while True:
    element = input('Пожалуйста введите число: ')
    if not element.isdigit():
        print("Попробуйте снова")
        continue
    else:
        element = int(element)

    indx = None

    for i, num in enumerate(raiting):
        if element > num:
            indx = i
            break

    if indx is None:
        raiting.append(element)
    else:
        raiting.insert(indx, element)

    print(raiting)

    q = input('Завершить форматирование списка? (Y/N)) ')
    if q.upper() == 'Y':
        break
    if q.lower() == 'y':
        break