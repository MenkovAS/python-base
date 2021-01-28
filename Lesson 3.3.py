'''3. Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
  и возвращает сумму наибольших двух аргументов.'''


def my_func(*arguments):
    arg1 = int(input("Аргумент 1: "))
    arg2 = int(input("Аргумент 2: "))
    arg3 = int(input("Аргумент 3: "))

    if arg1 >= arg2 > arg3:
        return arg1 + arg2
    elif arg3 >= arg2 > arg1:
        return arg3 + arg2
    elif arg1 >= arg3 > arg1:
        return arg1 + arg3
    else:
        exit(-1)


print(my_func())
