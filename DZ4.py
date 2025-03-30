n = int(input("количество символов:  "))
symbol = input("Тип символа: ")
orient = int(input("0-горизонт\n1-вертик\nориентация линии: "))
i = 0
while i < n:
    if orient == 1:
        print(symbol)
    else:
        print(symbol, end="  ")
    i += 1
