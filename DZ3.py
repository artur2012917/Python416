a = int(input("Введите число от 1 до 99:  "))
kop = a
if 11 <= kop <= 14:
    print(a, "копеек")
elif 1 <= a <= 10 or 15 <= a <= 99:
    kop = kop % 10
    if kop == 1:
        print(a, "копейка")
    elif 2 <= kop <= 4:
        print(a, "копейки")
    else:
        print(a, "копеек")
else:
    print("Значение должны быть от 1 до 99")
