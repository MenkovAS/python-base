a = int(input("Результат пробежки первого дня в км "))
b = int(input("Желаемый результат в км "))
Days = 1
km_day = a
while km_day < b:
        a = a + 0.1 * a
        Days += 1
        km_day = km_day + a
print(f"Вы достигнете требуемых показателей на %.d день" % Days)