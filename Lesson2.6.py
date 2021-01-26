"""Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя."""

products, order = [], 1
name, price, amount = None, None, None

while True:
    if name is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        name = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числом. Попробуйте еще раз.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Единица измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой или заполнена цифрами. Попробуйте еще раз.')
        continue

    measure = tmp

    products.append((
        order,
        {
            'name': name,
            'price': price,
            'amount': amount,
            'measure': measure
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Завершить формирование списка? (y/N)) ')
    if q.lower() == 'y':
        break

analitics = {
    'name': [],
    'price': [],
    'amount': [],
    'measure': set()
}

for _, item in products:
    analitics['name'].append(item['name'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['measure'].add(item['measure'])

print(analitics)
