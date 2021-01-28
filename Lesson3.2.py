'''Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.'''

name2 = str(input("Введите имя: "))
surname2 = str(input("Введите фамилию: "))
year2 = str(input("Введите год рождения: "))
city2 = str(input("Введите город: "))
email2 = str(input("Введите email: "))
number2 = str(input("Введите номер телефона: "))

def personal_info(name,surname,year,city,email,number):
    return ' '.join([
        "Имя: ", name,
        ". Фамилия: ", surname,
        ". Год Рождения: ", year,
        ". Город проживания: ", city,
        ". email: ", email,
        ". Номер телефона: ", number, "."
        ])
print(personal_info(name=name2, surname=surname2, year=year2, city=city2, email=email2, number=number2))
