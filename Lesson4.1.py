'''Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу:
 (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.'''


def Func():
    hours = float(input('Выработка в часах : '))
    perhour = float(input('Оплата труда за 1 час : '))
    prize = float(input('Премии - '))
    Salary = hours * perhour
    return Salary + prize
print(f'Размер заработной платы составил: {Func()}')