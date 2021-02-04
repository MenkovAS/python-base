'''Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.'''

my_file = open('test_2.txt', 'r')
content = my_file.read()
print(f'Текст файла: \n {content}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        print (f"{len(line.split())} слов в строке")
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
