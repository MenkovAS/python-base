'''Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

func = open('file.txt', 'w')
line = input('Введите текст \n')
while line:
    func.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
func.close()
func = open('file.txt', 'r')
text = func.readlines()
print(text)
func.close()
