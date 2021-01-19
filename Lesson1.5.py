Profit = float(input("Введите выручку фирмы "))
Costs = float(input("Введите издержку фирмы "))
if Profit > Costs:
    print(f"Фирма отработала с прибылью. Рентабельность выручки  : {Profit / Costs:.2f}")
    Employees = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль на одного сторудника {Profit / Employees:.2f}")
elif Profit == Costs:
    print("Фирма работает в ноль")
elif Profit < Costs:
    print("Фирма Работает в убыток")
    
