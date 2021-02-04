'''Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.'''

def summary():
    try:
        with open('summary.txt', 'w+') as file_obj:
            line = input('Введите набор чисел разделив пробелами \n')
            file_obj.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except ValueError:
        print('попробуйте ещё раз')
summary()
