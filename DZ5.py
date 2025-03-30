a = [int(input("->")) for i in range(int(input("n =")))]
s = 0


for i in a:
    if i < 0:
        s += i
print("Сумма отрицательных элементов:", s)