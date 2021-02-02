n = abs(int(input("Введите целое положительное число ")))
BiggestDigit = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > BiggestDigit:
        BiggestDigit = n % 10
    if n <= 9:
        print("Максимальное цифра в числе ", BiggestDigit)
        break
    else:
        continue
