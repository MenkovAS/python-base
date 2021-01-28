'''Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.'''


def div():

    try:
        argument1 = int(input("Введите делимое "))
        argument2 = int(input("Введите делитель "))
        result = argument1 / argument2
    except ValueError:
        return 'Необходимо ввести целое число, попробуйте ещё раз'
    except ZeroDivisionError:
        return "Ошибка деления на 0"

    return result


print(f'result  {div()}')