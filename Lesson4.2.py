''' Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].'''

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')


'''
По этому заданию вопрос, понятно, что в результате пропускается первое число,
т.к. первым сравнением должно быть 300 и 2, как решение вижу, что можно сделать цикл и начинать именно со второго значения.
А есть ли вариант без цикла данную операцию провести? т.е. указать каким-то образом, что мы начинаем со 2 элемента.
Через индекс возможно?'''