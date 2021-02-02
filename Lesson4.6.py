'''Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''


from itertools import count
from itertools import cycle

def count_func(number1, number2):
    for el in count(number1):
        if el > number2:
            break
        else:
            print(el)
def cycle_func(list, iteration):
    i = 0
    iter = cycle(list)
    while i < iteration:
        print(next(iter))
        i+=1
count_func(number1 = 12, number2 = 35)
cycle_func(list = [1, 2], iteration = 14)
