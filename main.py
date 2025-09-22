# # # # # # # Занятие 1 19/01/2025
# # # # # # # name = "admin" #переменная
# # # # # # # # print("Hello," + name + "!")
# # # # # # # age = 20
# # # # # # # # print(name + str(age))
# # # # # # # age = 15.2
# # # # # # # print(age)
# # # # # # # print(type(name))
# # # # # # # print(type(age))
# # # # # # # import random
# # # # # #
# # # # # # # a = 4
# # # # # # # b = 5
# # # # # # # print(id(a))
# # # # # # # print(id(b))
# # # # # # # a = b #5
# # # # # # # print(a)
# # # # # # # print(id(a))
# # # # # # # print(id(b))
# # # # # #
# # # # # # # a = b = c = 1
# # # # # # # print(a)
# # # # # # # print(b)
# # # # # # # print(c)
# # # # # #
# # # # # # # a,b,c = 5, "hello", 9.2
# # # # # # # print(a)
# # # # # # # print(b)
# # # # # # # print(c)
# # # # # #
# # # # # # # _first_name ="admin"
# # # # # # # print(_first_name)
# # # # # #
# # # # # # # import keyword
# # # # # # # print(keyword.kwlist)
# # # # # #
# # # # # # # PI=3.14
# # # # # # # print(PI)
# # # # # # # PI=2
# # # # # # # print(PI)
# # # # # #
# # # # # # #
# # # # # # # a=1
# # # # # # # b=2
# # # # # # # print("a:", a)
# # # # # # # print("b:",b)
# # # # # # #
# # # # # # # c = a
# # # # # # # a = b
# # # # # # # b = c
# # # # # # #
# # # # # # # print("a:", a)
# # # # # # # print("b:",b)
# # # # # # # print("c:",c)
# # # # # #
# # # # # #
# # # # # # # Занятие 2 23/01/2025
# # # # # #
# # # # # # # print("строка \
# # # # # # # символов")
# # # # # # # print('строка \nсимволов')
# # # # # # # print("\tДокмуент\"file.txt\"  находится по пути: D\\folder\\file.txt")  # \r -удаляет предудущий элемент
# # # # # #
# # # # # #
# # # # # # # s1 = "Hello"
# # # # # # # s2 = "Python"
# # # # # # # s3 = s1 +" " + s2 + "___"
# # # # # # # print(s3 * 3)
# # # # # #
# # # # # #
# # # # # # # print(6+2)
# # # # # # # print(6-2)
# # # # # # # print(6*2)
# # # # # # #
# # # # # # # print(7/2)
# # # # # # # print(7//2) #убрал дробную часть
# # # # # # # print(7**2)
# # # # # # # print(7%2)
# # # # # #
# # # # # #
# # # # # # # Задача 1
# # # # # # # a=5
# # # # # # # b=7
# # # # # # # c=3
# # # # # # # res = a+b+c
# # # # # # #
# # # # # # # print(a+b+c)
# # # # # # # print(a*b*c)
# # # # # # # print(res//3)
# # # # # #
# # # # # # # Задача 2
# # # # # #
# # # # # # # num = 10
# # # # # # # num +=5 # num=num +5=15
# # # # # # # print(num)
# # # # # # # num -=3  #num= num -3 =12
# # # # # # # print(num)
# # # # # # # num *=4 #48
# # # # # # # print(num)
# # # # # # # num **=2 #num =num **2  144
# # # # # # # print(num)
# # # # # #
# # # # # #
# # # # # # # Задача 3
# # # # # # # num = 4321
# # # # # # # # print(num)
# # # # # # # a = num %10
# # # # # # # print("a:",a)
# # # # # # # num = num//10
# # # # # # # # print(num)
# # # # # # # b=num % 10
# # # # # # # print("b:",b)
# # # # # # # num = num//10
# # # # # # # # print(num)
# # # # # # # c=num % 10
# # # # # # # print("c:",c)
# # # # # # # num = num//10
# # # # # # # # print(num)
# # # # # # # d = num % 10
# # # # # # # print("d:",d)
# # # # # # # print("обратное число: ", a*1000 + b*100+ c*10 +d)
# # # # # #
# # # # # #
# # # # # # # Задача 3 другое решение
# # # # # # # num = 4321
# # # # # # # print("Исходное число:", num)
# # # # # # # res = num % 10 *1000
# # # # # # # num//=10
# # # # # # # res += num%10*100
# # # # # # # num //=10
# # # # # # # res+=num%10*10
# # # # # # # num//=10
# # # # # # # res += num%10
# # # # # # #
# # # # # # # print("обратное чиcло:", res)
# # # # # #
# # # # # #
# # # # # # # num1 ="2"
# # # # # # # num2= 3
# # # # # # # res = int(num1) + num2
# # # # # # # res = num1 +str(num2)
# # # # # # # print(res)
# # # # # #
# # # # # #
# # # # # # # округление
# # # # # # # print(int(3.8))
# # # # # # # print(round(3.8))
# # # # # # # print(type(round(3.8)))
# # # # # # # print(round(3.891,2))
# # # # # # # print(type(round(3.891,2)))
# # # # # #
# # # # # # # a= '5.2'
# # # # # # # b = 10
# # # # # # # c = float(a)+b
# # # # # # # print(c)
# # # # # #
# # # # # #
# # # # # # # name = "Victor"
# # # # # # # age = 28
# # # # # # # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="")
# # # # # # # print("Новая строка")
# # # # # #
# # # # # #
# # # # # # # name =input("Введите имя: ")
# # # # # # # print("Ваше имя:", name)
# # # # # #
# # # # # #
# # # # # # # num = int(input("Введите число: "))
# # # # # # # power = int(input ("Введите степень: "))
# # # # # # # res= num ** power
# # # # # # # print("Число", num, "В степени", power, "равно:", res)
# # # # # #
# # # # # #
# # # # # # # b1= True
# # # # # # # b2 = False
# # # # # # # print(type(b1))
# # # # # # # print(b1+5) #1+5
# # # # # # # print(b2+5)
# # # # # #
# # # # # # # print(bool("python"))
# # # # # # # print(bool(""))
# # # # # #
# # # # # #
# # # # # # # a = None
# # # # # # # print(a)
# # # # # # # print(type(a))
# # # # # #
# # # # # # # print(7==7)
# # # # # # # print(2+5 ==7/3)
# # # # # # # print(2+5 !=7/3)
# # # # # # # print(8>5)
# # # # # # # print(8>=8)
# # # # # # # print("привет">"ПРИВЕТ")
# # # # # #
# # # # # # #
# # # # # # # print(2<4<9)
# # # # # # # print(2*5>7>=4+3)
# # # # # #
# # # # # #
# # # # # # # 01/02/2025 занятие 3
# # # # # #
# # # # # # # print(5 - 3 == 2 and 1 + 3 == 4)  # true and true=>true
# # # # # # #
# # # # # # # print(5 - 3 == 2 or 1 + 3 == 4)  # true or true =>true
# # # # # # #
# # # # # # # print(not 4 - 4)  # not true меня на противоположное значение
# # # # # # #
# # # # # # # a = 5
# # # # # # # print("a:", a)
# # # # # #
# # # # # #
# # # # # # # cnt = 15
# # # # # # # if cnt < 10:
# # # # # # #     cnt += 1
# # # # # # # print(cnt)
# # # # # #
# # # # # #
# # # # # # # age = int(input("Введите свой возраст: "))
# # # # # # # if age >= 18:
# # # # # # #     print("Доступ на сайт разрешен")
# # # # # # # else:
# # # # # # #     print("Доступ запрещен")
# # # # # #
# # # # # #
# # # # # # # a = 25
# # # # # # # b = 15
# # # # # # # if a > b:
# # # # # # #     print("a > b ")
# # # # # # # elif a == b:
# # # # # # #     print("a==b")
# # # # # # # else:
# # # # # # #     print("b < a ")
# # # # # #
# # # # # #
# # # # # # # задача 1
# # # # # #
# # # # # # # a = int(input("Введите первую строку:"))
# # # # # # # b = int(input("Введите первую строку:"))
# # # # # # # c = int(input("Введите первую строку:"))
# # # # # # #
# # # # # # # if a == b == c:
# # # # # # #     print("Равносторонний")
# # # # # # # elif a == b or b == c or a == c:
# # # # # # #     print("Треуглольник равнобедренный")
# # # # # # # else:
# # # # # # #     print("Треугольник разносторонний")
# # # # # #
# # # # # #
# # # # # # # Задача 2
# # # # # #
# # # # # #
# # # # # # # day = int(input("Введите день недели(цифрой)"))
# # # # # # # if 1 <= day <= 5:  # (day >= 1) and (day <= 5):    #1<2<5
# # # # # # #     print("Рабочий день-",end="")
# # # # # # #     if day ==1:
# # # # # # #         print("понедельник", )
# # # # # # #     if day == 2:
# # # # # # #         print("вторник", )
# # # # # # #     if day ==3:
# # # # # # #         print("среда", )
# # # # # # #     if day ==4:
# # # # # # #         print("четверг", )
# # # # # # #     if day ==5:
# # # # # # #         print("пятница", )
# # # # # # # elif day == 6 or day == 7:
# # # # # # #     print("Выходной день - ",end="")
# # # # # # #     if day ==6:
# # # # # # #         print("суббота", )
# # # # # # #     if day ==7:
# # # # # # #         print("воскресение", )
# # # # # # # else:
# # # # # # #     print("Такого дня не существует")
# # # # # #
# # # # # #
# # # # # # # Задача 3
# # # # # # # season = int(input("Введите номер месяца:"))
# # # # # # # if 1 <= season <= 12:
# # # # # # #     print("Время года:", end="")
# # # # # # #     if 1 <= season <= 2 or season == 12:
# # # # # # #         print("Зима")
# # # # # # #     if 3 <= season <=5:
# # # # # # #         print("Весна")
# # # # # # #     if 6 <= season <=8:
# # # # # # #         print("Лето")
# # # # # # #     if 9 <= season <=11:
# # # # # # #         print("Осень")
# # # # # # # else:
# # # # # # #     print("Такого месяца не существует")
# # # # # #
# # # # # #
# # # # # # # Задача 4
# # # # # #
# # # # # # # n = int(input("Введите количество ворон:"))
# # # # # # # if 0 <= n <= 9:
# # # # # # #     print("На ветке ", end="")
# # # # # # #     if n == 1:
# # # # # # #         print(n, "ворона")
# # # # # # #     if 2 <= n <= 4:
# # # # # # #         print(n, "вороны")
# # # # # # #     if 5 <= n <= 9 or n == 0:
# # # # # # #         print(n, "ворон")
# # # # # # # else:
# # # # # # #     print("Ошибка ввода")
# # # # # #
# # # # # #
# # # # # # # match выражение:
# # # # # # #       case шаблон 1:
# # # # # # #           действие_1
# # # # # # #       case шаблон 2:
# # # # # # #           действие_2
# # # # # # #       case_:
# # # # # # #           значение_по_умполчанию
# # # # # #
# # # # # #
# # # # # # # password ="admin"
# # # # # # # match password:
# # # # # # #     case"admin":
# # # # # # #         print("Администратор")
# # # # # # #     case "user":
# # # # # # #         print("Пользователь")
# # # # # # #     case _:
# # # # # # #         print("Пароль неверен")
# # # # # #
# # # # # #
# # # # # # # day = 'понедельник'
# # # # # # # time = 5
# # # # # # #
# # # # # # # match day:
# # # # # # #     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
# # # # # # #         print("Рабочий день")
# # # # # # #     case 'суббота' | 'выходной день':
# # # # # # #         print("Выходной день")
# # # # # # #     case _:
# # # # # # #         print("Такого дня недели не существует или нерабочее время")
# # # # # #
# # # # # #
# # # # # # # a,b=30,20
# # # # # # # print(a if a < b else b)
# # # # # # #
# # # # # # # res=0
# # # # # # # a,b = 30, 5
# # # # # # # print("На 0 делить нельзя" if b ==0 else a/b)
# # # # # #
# # # # # #
# # # # # # # Занятие 4
# # # # # #
# # # # # # # try:
# # # # # # #     n = int(input("Введите целое число: "))
# # # # # # #     print(n*2)
# # # # # # # except ValueError:
# # # # # # #     print("Что то пошло не так")
# # # # # # # print("Код далее")
# # # # # #
# # # # # # # try:
# # # # # # #     n=int(input("Введите делимое: "))
# # # # # # #     m=int(input("Введите делитель: "))
# # # # # # #     print(n/m)
# # # # # # # except ValueError:
# # # # # # #     print("Нельзя вводить строки")
# # # # # # # except ZeroDivisionError:
# # # # # # #     print("Нельзя делить на ноль")
# # # # # #
# # # # # #
# # # # # # # try:
# # # # # # #     n = int(input("Введите делимое: "))
# # # # # # #     m = int(input("Введите делитель: "))
# # # # # # #     print(n / m)
# # # # # # # except (ValueError, ZeroDivisionError):
# # # # # # #     print("Нельзя вводить строки")
# # # # # # #     print("Нельзя делить на 0")
# # # # # # # else:
# # # # # # #     print("Все нормально. Вы ввели", n, "и", m)
# # # # # # # finally:
# # # # # # #     print("Конец программы  ")
# # # # # #
# # # # # # # Задача 1
# # # # # # # try:
# # # # # # #     n = int(input("Введите первое число"))
# # # # # # #     m = int(input("Введите второе число"))
# # # # # # #     print(n+m)
# # # # # # # except ValueError:
# # # # # # #     print(str(n)+ str(m))
# # # # # # # finally:
# # # # # # #     print("Конец программы  ")
# # # # # #
# # # # # # # задача 1 второе решение
# # # # # # #
# # # # # # # n = input("Введите первое число: ")
# # # # # # # m = input("Введите второе число: ")
# # # # # # #
# # # # # # # try:
# # # # # # #     n=int(n)
# # # # # # #     m=int(m)
# # # # # # # except ValueError:
# # # # # # #     n=str(n)
# # # # # # # finally:
# # # # # # #     print(n+m)
# # # # # #
# # # # # #
# # # # # # # Циклы
# # # # # #
# # # # # # # while Условие:
# # # # # # #    блок_кода
# # # # # #
# # # # # # # итерация - один шаг цикла
# # # # # #
# # # # # # # i = 0
# # # # # # # while i < 5:
# # # # # # #     print("i=", i)
# # # # # # #     i += 1
# # # # # # # Задача 2
# # # # # # # i = 1
# # # # # # # while i <=20:
# # # # # # #     if i % 2 ==0:
# # # # # # #        print(i, end=" ")
# # # # # # #     i+= 1
# # # # # #
# # # # # # #
# # # # # # # i = 1
# # # # # # # while i <=20:
# # # # # # #     if i % 2 ==0:
# # # # # # #        print(i, end=" ")
# # # # # # #     i+= 1
# # # # # # #
# # # # # # #
# # # # # # # print()
# # # # # # # j=2
# # # # # # # while j<=20:
# # # # # # #     print(j, end=" ")
# # # # # # #     j+=2
# # # # # #
# # # # # # # задача 3
# # # # # #
# # # # # # # n = int(input("Укажиие количестов символов: "))
# # # # # # # i =0
# # # # # # # while i<n:
# # # # # # #     print("*", end=" ")
# # # # # # #     i+=1
# # # # # #
# # # # # # # другое решение
# # # # # #
# # # # # # # n = int(input("Укажиие количестов символов: "))
# # # # # # # print("*" *n)
# # # # # #
# # # # # #
# # # # # # # Задача 4
# # # # # #
# # # # # # # a = int(input("Введите начало диапозона"))
# # # # # # # b = int(input("Введите конец диапозона"))
# # # # # # # res = 0
# # # # # # # while a <= b:
# # # # # # #     if a % 2:
# # # # # # #         res +=a
# # # # # # #     a += 1
# # # # # # # print(res)
# # # # # #
# # # # # #
# # # # # # # n = (input("Введите целое число: "))
# # # # # # #
# # # # # # # while type(n) != int:
# # # # # # #     try:
# # # # # # #         n = int(n)
# # # # # # #     except ValueError:
# # # # # # #         print("Число не целое!")
# # # # # # #         n = input("Введите целое число: ")
# # # # # # #
# # # # # # # if n % 2 == 0:
# # # # # # #     print("четное число")
# # # # # # # else:
# # # # # # #     print("нечетное")
# # # # # #
# # # # # # # i = 0
# # # # # # # while i < 10:
# # # # # # #     if i==3:
# # # # # # #         i+=1
# # # # # # #         continue
# # # # # # #     print(i,end="  ")
# # # # # # #     if i == 5:
# # # # # # #         break
# # # # # # #     i += 1
# # # # # # # print("\nЦикл завершен")
# # # # # #
# # # # # # # i = 0
# # # # # # # while True:
# # # # # # #     print(i)
# # # # # # #     if i == 5:
# # # # # # #         break
# # # # # # #     i += 1
# # # # # #
# # # # # #
# # # # # # # while True:
# # # # # # #     n = int(input("Введите положительное число: "))
# # # # # # #     if n < 0:
# # # # # # #         break
# # # # # #
# # # # # #
# # # # # # # res = 1
# # # # # # # while True:
# # # # # # #     n = int(input("введите число: "))
# # # # # # #     if n == 0:
# # # # # # #         break
# # # # # # #     res = n * res
# # # # # # # print(res)
# # # # # #
# # # # # #
# # # # # # # i = 1
# # # # # # # while i < 5:
# # # # # # #     print("Внешний цикл: i=", i)
# # # # # # #     j = 1
# # # # # # #     while j < 4:
# # # # # # #         print("\tвнтуренний цикл: j=", j)
# # # # # # #         j += 1
# # # # # # #     i += 1
# # # # # #
# # # # # #
# # # # # # # i = 1
# # # # # # # while i < 10:
# # # # # # #     j = 1
# # # # # # #     while j < 10:
# # # # # # #         print(i, "*", j, "=", i * j, end="\t\t")
# # # # # # #         j += 1
# # # # # # #     print()
# # # # # # #     i += 1
# # # # # #
# # # # # #
# # # # # # # Занятие 5 12.02.2025
# # # # # #
# # # # # #
# # # # # # # for element in collections:
# # # # # # #     print(element)
# # # # # #
# # # # # # # for i in "Hello","world":
# # # # # # #     print(i)
# # # # # # #
# # # # # # # for i in "Hello":
# # # # # # #     print(i)
# # # # # #
# # # # # # # range(start, stop, step)
# # # # # #
# # # # # #
# # # # # # # for i in range(10, 0, -2):
# # # # # # #     print(i, end=" ")
# # # # # # #
# # # # # # # print()
# # # # # # # j = 10
# # # # # # # while j > 0:
# # # # # # #     print(j, end=" ")
# # # # # # #     j -= 1
# # # # # #
# # # # # # # Задача пользователь вводит целое число.
# # # # # # # необходимо вывести все целые числа, на которое заданное число делится без остатка.
# # # # # #
# # # # # # # a = int(input("Введите целое число:  "))
# # # # # # # for i in range(1, a):
# # # # # # #     if a % i == 0:
# # # # # # #         print(i, end=" ")
# # # # # #
# # # # # # # Вывести целые числа в диапозоне от 10 до 100 у которых есть две одинковые цифры.
# # # # # # # 11 22 33 44 55 66 77 88 99
# # # # # # # первые вариант
# # # # # # # for i in range(11,100, 11):
# # # # # # #     print(i, end=" ")
# # # # # #
# # # # # # # for i in range(10, 100):
# # # # # # #     if i % 10 == i//10:    #i%10 -последняя цифра. i//10 -первая цифра , они равны
# # # # # # #         print(i, end=" ")
# # # # # #
# # # # # #
# # # # # # # for i in range(3):
# # # # # # #     if i == 1:
# # # # # # #         break
# # # # # # #     print(i)
# # # # # # # else:
# # # # # # #     print("конец цикла")
# # # # # #
# # # # # #
# # # # # # # for i in range(3):
# # # # # # #     print("+++")
# # # # # # #     for j in range(2):
# # # # # # #         print("----")
# # # # # #
# # # # # #
# # # # # # # Задача вывести на экран прямоугольни из звездочек, ширину и высоту задает пользователь
# # # # # # #
# # # # # # # w = int(input("Введите ширину прямоугольника"))
# # # # # # # h = int(input("Введите высотупрямоугольника"))
# # # # # # #
# # # # # # # for i in range(h):
# # # # # # #     for j in range(w):
# # # # # # #         if i == 0 or i == h - 1 or j == 0 or j == w-1:
# # # # # # #             print("*", end="")
# # # # # # #         else:
# # # # # # #             print(" ", end="")
# # # # # # #     print()
# # # # # #
# # # # # #
# # # # # # # string = [letter * 2 for letter in "Python"]
# # # # # # # print(string)
# # # # # # #
# # # # # # # for letter in "Python":
# # # # # # #     print(letter * 2, end="\t")
# # # # # #
# # # # # # #
# # # # # # # num = [i for i in range(30) if i % 2 == 0]
# # # # # # # print(num)
# # # # # # #
# # # # # # # print()
# # # # # # #
# # # # # # # for i in range(30):
# # # # # # #     if i % 2 == 0:
# # # # # # #         print(i, end="\t")
# # # # # #
# # # # # #
# # # # # # # Список (list)
# # # # # # #
# # # # # # # nums = [8, 3, 9, 4, 1]
# # # # # # # print(nums)
# # # # # # # print(type(nums))
# # # # # # #
# # # # # # # num1= list([8, 3, 9, 4, 1])
# # # # # # # print(num1)
# # # # # #
# # # # # #
# # # # # # # nums = [8, 3, 9, 4, 1]
# # # # # # #
# # # # # # # print(nums)
# # # # # # # nums[1] = 256
# # # # # # # print(nums)
# # # # # # # nums[3] += 100
# # # # # # # print(nums)
# # # # # #
# # # # # #
# # # # # # # nums = [8, 3, 9, 4, 1]
# # # # # # # print(nums,id(nums))
# # # # # # # print(nums[1],id(nums[1]))
# # # # # # # nums[1]= 256
# # # # # # # print(nums[1],id(nums[1]))
# # # # # # # print(nums, id(nums))
# # # # # # # print("длина списка: ",len(nums))
# # # # # #
# # # # # # # nums = [8, 3, 9, 4, 1]
# # # # # # # nums2 = [11, 12, 13]
# # # # # # # n = nums + nums2
# # # # # # # print(n)
# # # # # # # print(n * 2)
# # # # # # # print(n * 3)
# # # # # #
# # # # # # # print(list("Hello"))
# # # # # # #
# # # # # # # print(range(10))
# # # # # # # print(list(range(10)))
# # # # # # # print(list(range(2, 10)))
# # # # # # # print(list(range(10, 2, -2)))
# # # # # #
# # # # # # # [выражение for перемення in последовательность]
# # # # # #
# # # # # # # a = [0 for i in range(5)]
# # # # # # # print(a)
# # # # # #
# # # # # # # n = 5
# # # # # # # a = [i ** 2 for i in range(1, n + 1)]
# # # # # # # print(a)
# # # # # #
# # # # # # # a = [0] * int(input("Введите количество элементов списка: "))
# # # # # # # print(a)
# # # # # # # for i in range(len(a)):
# # # # # # #     a[i] = int(input("->"))
# # # # # # # print(a)
# # # # # #
# # # # # #
# # # # # # # a = [int(input("->")) for i in range(int(input("n= ")))]
# # # # # # # print(a)
# # # # # #
# # # # # #
# # # # # # # Занятие 6
# # # # # #
# # # # # # # a = list(range(10, 100, 10))
# # # # # # # print(a)
# # # # # # #
# # # # # # # for i in range(len(a)):  #i выступает как число , i здесь от нуля до 10 1 2 3 4 5 6 7 8 9
# # # # # # #     # print(i, end=" ")
# # # # # # #     print(a[i] + 2, end=" ")
# # # # # # # print()
# # # # # # #
# # # # # # # for i in a:
# # # # # # #     print(i + 2, end=" ")
# # # # # #
# # # # # #
# # # # # # # a = [int(input("->")) for _ in range(int(input("n = ")))]
# # # # # # # s = 0  # переменная для суммы
# # # # # # # for i in range(len(a)):
# # # # # # #     if a[i] < 0:  #a[_]
# # # # # # #         s += a[i]
# # # # # # # print("Сумма отрицательных элементов: ", s)
# # # # # #
# # # # # # # i = 0
# # # # # # # while i < len(a):
# # # # # # #     if a[i] < 0:
# # # # # # #         s += a[i]
# # # # # # #     i += 1
# # # # # # # print("Сумма отрицательных элементов:", s)
# # # # # #
# # # # # #
# # # # # # # for _ in a:
# # # # # # #     if _ < 0:
# # # # # # #         s += _
# # # # # # # print("Сумма отрицательных элементов:", s)
# # # # # #
# # # # # # # задача выведи все элементы списка с четными индексами( то евть А[0] a[2] a[4]) выведите эдементы списка:
# # # # # #
# # # # # # # a = [int(input("->")) for _ in range(int(input("n = ")))]
# # # # # # # print(a)
# # # # # # #
# # # # # # # for i in range(len(a)):  # здесь не указывается шаг цикла, а выбирается что делится на 2
# # # # # # #     if i % 2 == 0:
# # # # # # #         print(a[i], end=" ")
# # # # # # # print()
# # # # # # # for i in range(0, len(a), 2): #шаг цикла 2
# # # # # # #     print(a[i], end=" ")
# # # # # #
# # # # # #
# # # # # # # Задача.Дан список чисел. выведите все элементы списка, которые больше предыдущего элмена. выведите элементы списка.
# # # # # #
# # # # # # # a = [int(input("->")) for _ in range(int(input("n = ")))]
# # # # # # # print(a)
# # # # # #
# # # # # # # for i in range(1, len(a)):
# # # # # # #     if a[i] > a[i - 1]:
# # # # # # #         print(a[i], end=" ")
# # # # # #
# # # # # #
# # # # # # # for i in a:
# # # # # # #     if i > i - 1:
# # # # # # #        print(i, end =" ")
# # # # # #
# # # # # #
# # # # # # # задача
# # # # # # # n = list(range(21, 41))
# # # # # # # print(n)
# # # # # # # k = s = 0
# # # # # # # for i in range(len(n)):
# # # # # # #     if n[i] % 2 ==0:
# # # # # # #         k+=1
# # # # # # #     else:
# # # # # # #         s+=n[i]
# # # # # # # print("количество четных элементов:",k)
# # # # # # # print("Сумма нечетных элементов:", s)
# # # # # #
# # # # # #
# # # # # # # задача
# # # # # # # a = [int(input("->")) for i in range(int(input("n = ")))]
# # # # # # # sum1 = kol = 0
# # # # # # # for i in range(len(a)):
# # # # # # #     if a[i] !=0:
# # # # # # #         kol +=1
# # # # # # #         sum1 +=a[i]
# # # # # # # print("среднее арифметическое", sum1/kol)
# # # # # #
# # # # # #
# # # # # # # lst = [7, 9, 2, 1, 17]
# # # # # # # print(lst)
# # # # # # #
# # # # # # # lst[0], lst[1] = lst [1] , lst [0]
# # # # # # #
# # # # # # # print(lst)
# # # # # #
# # # # # # # s = [9, 7, 2, 1, 17]
# # # # # # # print(s)
# # # # # # # print(s[1:4])
# # # # # # # print(s[:])
# # # # # # # print(s[2:])    #от 2 до конца
# # # # # # # print(s[:2])  # от начала до 2
# # # # # # # print(s[::2])  #от начала до конца , шаг - 2
# # # # # # # print(s[::3])
# # # # # # # print(s[::-1])  #от развернули(от конца до начала)
# # # # # #
# # # # # #
# # # # # # # Задача
# # # # # #
# # # # # # # lst = list(range(1, 8))
# # # # # # # print(lst)
# # # # # # # print(lst[::-1])
# # # # # # # print(lst[::2])
# # # # # # # print(lst[1::2])
# # # # # # # print(lst[:1])
# # # # # # # print(lst[::-7])
# # # # # #
# # # # # #
# # # # # # # st = "Hello"
# # # # # # # print(st[1:3])
# # # # # #
# # # # # #
# # # # # # # lst = list(range(1, 8))
# # # # # # # print(lst)
# # # # # # # lst[1:3] = [0, 0, 0, 0]
# # # # # # # print(lst)
# # # # # # # lst[1:2] = [20]
# # # # # # # print(lst)
# # # # # # # lst[10:11] = [100]
# # # # # # # print(lst)
# # # # # #
# # # # # # # Методы списка
# # # # # #
# # # # # # # lst = list(range(1, 8))
# # # # # # # print(lst)
# # # # # # # lst.append(99)  # добавляет один элемент в конец списка
# # # # # # # print(lst)
# # # # # # # lst.extend([1, 2, 3])  # добавляет список элемент в конец списка
# # # # # # # print(lst)
# # # # # # # lst.insert(1, 100) #индекс, объект (вставить)
# # # # # # # print(lst)
# # # # # #
# # # # # #
# # # # # # # s = []
# # # # # # # n = int(input("Кол-во элементов списка: "))
# # # # # # # for num in range(n):
# # # # # # #     x = int(input("Введите число: "))
# # # # # # #     # s.append(x)
# # # # # # #     s.insert(0, x)
# # # # # # # print(s)
# # # # # #
# # # # # # # # сделать чтоб из каждого списка нашли общие цифры
# # # # # # # a = [5, 9, 2, 1, 4, 3, 4, 2]
# # # # # # # b = [4, 2, 1, 3, 7, 2]
# # # # # # # c = []
# # # # # # #
# # # # # # # for i in a:
# # # # # # #     for j in b:
# # # # # # #         if i in c:
# # # # # # #             continue
# # # # # # #         if i == j:
# # # # # # #             c.append(i)
# # # # # # #             break
# # # # # # #
# # # # # # # print(c)
# # # # # #
# # # # # #
# # # # # # # Занятие 8
# # # # # #
# # # # # # #
# # # # # # # mas = [random.randint(0,10) for i in range(10)]
# # # # # # # print(mas)
# # # # # # # print(2 not in mas)
# # # # # #
# # # # # #
# # # # # # # lst = []
# # # # # # # # if len(lst) == 0:
# # # # # # # #     print("Список пустой")
# # # # # # #
# # # # # # # print(bool(lst))
# # # # # # #
# # # # # # #
# # # # # # # if not lst:
# # # # # # #     print("Список пустой")
# # # # # # # else:
# # # # # # #     print("В списке есть элементы")
# # # # # #
# # # # # #
# # # # # # # матрицы
# # # # # # #
# # # # # # # m = [
# # # # # # #     [1, 2, 3, 4], #0
# # # # # # #     [5,6,7,8],  #1
# # # # # # #     [9,10,11,12]  #2
# # # # # # # ]
# # # # # # # print(m)
# # # # # # # # print(len(m))
# # # # # # # # print(m[1])
# # # # # # # # print(m[1][3])
# # # # # # # # print(m[2][1])
# # # # # # # # print(m[1][3])
# # # # # # #
# # # # # # #
# # # # # # # # print("Вариант 1")
# # # # # # # # for row in range(len(m)):
# # # # # # # #     # print(m[row])
# # # # # # # #     for col in range(len(m[row])):
# # # # # # # #         print(m[row] [col], end="\t")
# # # # # # # #     print()
# # # # # # #
# # # # # # #
# # # # # # # print("Вариант 2")
# # # # # # # for row in m:
# # # # # # #     for x in row:
# # # # # # #         print(x, end="\t")
# # # # # # #     print()
# # # # # #
# # # # # #
# # # # # # # Модули
# # # # # #
# # # # # # # import math
# # # # # # #
# # # # # # # print(math.sqrt(4)) #корень кваддртный
# # # # # # # print(math.ceil(3.2)) #округление в большую
# # # # # # # print(math.floor(3.8)) #округление в меньшую
# # # # # #
# # # # # # # import math as m
# # # # # # #
# # # # # # # print(m.sqrt(4))
# # # # # # # print(m.ceil(3.2))
# # # # # # # print(m.floor(3.8))
# # # # # #
# # # # # #
# # # # # # # from  math import *
# # # # # # #
# # # # # # # print(sqrt(4))
# # # # # # # print(ceil(3.2))
# # # # # # # print(floor(3.8))
# # # # # #
# # # # # #
# # # # # # # from math import sqrt, ceil, floor
# # # # # # #
# # # # # # # print(sqrt(4))
# # # # # # # print(ceil(3.2))
# # # # # # # print(floor(3.8))
# # # # # #
# # # # # #
# # # # # # # Задача
# # # # # # # from math import pi
# # # # # # # radius = int(input("Введите радиус окружности: "))
# # # # # # # print("Длина окружности: ", round(2 * pi * radius,2))
# # # # # #
# # # # # #
# # # # # # # import time
# # # # # # # # import locale
# # # # # # # #
# # # # # # # # print(time.time())
# # # # # # # # print(time.ctime())
# # # # # # # # print(time.localtime())
# # # # # # # # res = time.localtime()
# # # # # # # # print(res.tm_year,"-0", res.tm_mon,"-0", res.tm_mday, sep="")
# # # # # # # # print(time.strftime("Today is %B %d, %Y"))
# # # # # # # # print(time.strftime("%m/%d/%Y, %H:%M:%S"))
# # # # # # # #
# # # # # # # # locale.setlocale(locale.LC_ALL, "ru")
# # # # # # # # print(time.strftime("Сегодня: %B %d,%A, %Y"))
# # # # # # # #
# # # # # # # # n = 1,000,000.98
# # # # # # # # start=time.monotonic()
# # # # # # # # pause = 5
# # # # # # # # print("Программа запущена")
# # # # # # # # time.sleep(pause)
# # # # # # # # result = time.monotonic() - start
# # # # # # # # print("Программа выполнена за ", result,"  секунд")
# # # # # # #
# # # # # # # print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(3382137128)))
# # # # # #
# # # # # #
# # # # # # # Занаятие 9
# # # # # #
# # # # # # # Функции
# # # # # #
# # # # # #
# # # # # # # def hello(name, age):
# # # # # # #     print("Меня зовут  "+ name +".Мне " +str(age)+ " лет.")
# # # # # # #
# # # # # # #
# # # # # # # hello("Irina", 28 )
# # # # # # # hello("Ivan", 15)
# # # # # #
# # # # # #
# # # # # # # def get_sum(a, b):
# # # # # # #     print(a + b)
# # # # # # #
# # # # # # #
# # # # # # # x = 2
# # # # # # # y = 5
# # # # # # # get_sum(x, y)
# # # # # # # get_sum("abc", "def")
# # # # # #
# # # # # #
# # # # # # # Задача 1
# # # # # #
# # # # # # # def print_line(count, a, b):
# # # # # # #     for i in range(count):
# # # # # # #         if i% 2 ==0:
# # # # # # #               print(a,end ="")
# # # # # # #         else:
# # # # # # #             print(b, end="")
# # # # # # #     print()
# # # # # # #
# # # # # # #
# # # # # # # print_line(9, "+", "-")
# # # # # # # print_line(7, "x", "0")
# # # # # #
# # # # # #
# # # # # # # def get_sum(a, b):
# # # # # # #
# # # # # # #     print("Hello")
# # # # # # #     return a + b
# # # # # # #
# # # # # # #
# # # # # # # x = 2
# # # # # # # y = 5
# # # # # # # res = get_sum(x, y)
# # # # # # # print(res)
# # # # # #
# # # # # #
# # # # # # # def max_value(one, two):
# # # # # # #     if one > two:
# # # # # # #         return one
# # # # # # #     else:
# # # # # # #         return two
# # # # # # #
# # # # # # #
# # # # # # # print(max_value(9, 6))
# # # # # # # print(max_value(9, 16))
# # # # # #
# # # # # #
# # # # # # # Задача 2
# # # # # #
# # # # # # #
# # # # # # # def add(x, y):
# # # # # # #     if x > y:
# # # # # # #         return x - y
# # # # # # #     else:
# # # # # # #         return x + y
# # # # # # #
# # # # # # #
# # # # # # # a = int(input("а = "))
# # # # # # # b = int(input("b = "))
# # # # # # # print(add(a, b))
# # # # # #
# # # # # # # Задача 3  поменяйте местами
# # # # # # # первый вариант
# # # # # # # def change(lst):
# # # # # # #     lst[0], lst[-1] = lst[-1], lst[0]
# # # # # # #     return lst
# # # # # # #
# # # # # # #
# # # # # # # print(change([1, 2, 3]))
# # # # # # # print(change([9, 12, 33, 54, 105]))
# # # # # # # print(change(['c', 'л', 'о', 'н']))
# # # # # #
# # # # # # # второй вариант
# # # # # #
# # # # # #
# # # # # # # def change(lst):
# # # # # # #     end = lst.pop()  #удаляет последний элемент из списка
# # # # # # #     start = lst.pop(0)  #удаляет первй элемент из списка
# # # # # # #     lst.append(start)  #добавляет первый элемент
# # # # # # #     lst.insert(0,end)
# # # # # # #     return lst
# # # # # # #
# # # # # # #
# # # # # # # print(change([1, 2, 3]))
# # # # # # # print(change([9, 12, 33, 54, 105]))
# # # # # # # print(change(['c', 'л', 'о', 'н']))
# # # # # #
# # # # # #
# # # # # # # def is_first_big(x,y):
# # # # # # #     if x > y:
# # # # # # #         return True
# # # # # # #     else:
# # # # # # #         return False
# # # # # # # print(is_first_big(10,5))
# # # # # # # print(is_first_big(5,10))
# # # # # # #
# # # # # # #
# # # # # # # if
# # # # # #
# # # # # #
# # # # # # # def check_password(password):
# # # # # # #     has_upper = False
# # # # # # #     has_lower = False
# # # # # # #     has_num = False
# # # # # # #
# # # # # # #
# # # # # # #     for ch in password:
# # # # # # #         if "A" <= ch <= "Z":
# # # # # # #             has_upper = True
# # # # # # #         if "a" <= ch<= "z":
# # # # # # #             has_lower = True
# # # # # # #         if 0<= ch <= 9:
# # # # # # #             has_num = True
# # # # # # #
# # # # # # #     if len(password) >= 8 and has_upper and has_lower and has_num:
# # # # # # #         return True
# # # # # # #     return False
# # # # # # #
# # # # # # #
# # # # # # # p = input("Введите пароль: ")
# # # # # # # if check_password(p):
# # # # # # #     print("Это надежный пароль")
# # # # # # # else:
# # # # # # #     print("Это ненадежный пароль")
# # # # # #
# # # # # #
# # # # # # # def get_sum(a, b, c=0, d=1):
# # # # # # #     return a + b + c + d
# # # # # # #
# # # # # # #
# # # # # # # print(get_sum(1, 5, 2, 7))
# # # # # # # print(get_sum(1, 5, 2))
# # # # # # # print(get_sum(1, 5))
# # # # # # # print(get_sum(1, 5, d=2))
# # # # # # #
# # # # # # #
# # # # # # # def display_info(name, age):
# # # # # # #     print("Name:", name, "\nAge:", age)
# # # # # # #
# # # # # # #
# # # # # # # display_info("Ira", 23)
# # # # # # # display_info(23, "Ira")
# # # # # # # display_info(age=23, name="Ira")
# # # # # #
# # # # # # #
# # # # # # # def set_param(count=20, symbol="-"):
# # # # # # #     print(count * symbol)
# # # # # # #
# # # # # # #
# # # # # # # set_param(10, "+")
# # # # # # # set_param(5, "*")
# # # # # # # set_param(15, "#")
# # # # # # # set_param(7)
# # # # # # # set_param()
# # # # # #
# # # # # #
# # # # # # # Занятиие 10
# # # # # #
# # # # # #
# # # # # # # def func(a, b=0):
# # # # # # #     return a + b
# # # # # # #
# # # # # # #
# # # # # # # print(func(2, 5))
# # # # # # # print(func(b=2, a=5))
# # # # # # # print(func(2))
# # # # # #
# # # # # #
# # # # # # # lst1 = [1, 2, 3]
# # # # # # # lst2 = [1, 2, 3]
# # # # # # # print(lst1, id(lst1))
# # # # # # # print(lst2, id(lst2))
# # # # # # # print(lst1 == lst2)
# # # # # # # print(lst1 is lst2)
# # # # # # #
# # # # # # # a = "Hello"
# # # # # # # b = "Hello"
# # # # # # # print(a, id(a))
# # # # # # # print(b, id(b))
# # # # # # # print(a == b)
# # # # # # # print(a is b)=
# # # # # #
# # # # # #
# # # # # # # lst1 = [1, 2, 3]
# # # # # # # print(lst1, id(lst1))
# # # # # # # lst1.append(4)  # добавляет еще один элемент  , называется "метод"
# # # # # # # print(lst1, id(lst1))
# # # # # # # lst1.pop(1)  #удаляет один элемент
# # # # # # # print(lst1, id(lst1))
# # # # # #
# # # # # #
# # # # # # # a="Hello"             # строка неизменяемый тип памяти
# # # # # # # print(a,id(a))
# # # # # # # a = a + "!"
# # # # # # # print(a,id(a))
# # # # # #
# # # # # # # list - список
# # # # # # # a = 5
# # # # # # # print(a, id(a))
# # # # # # # a = a + 3
# # # # # # # print(a, id(a))
# # # # # #
# # # # # # # Кортеж - неизменняемый тип данных
# # # # # # # tuple- кортеж
# # # # # #
# # # # # #
# # # # # # # lst = [10, 20, 30]
# # # # # # # tpl = (10, 20, 30) #кортеж неизменяемый
# # # # # # # print(lst.__sizeof__()) #размер данных
# # # # # # # print(tpl.__sizeof__())
# # # # # # #
# # # # # # #
# # # # # # # print(lst[1])
# # # # # # # print(tpl[1])
# # # # # # # lst[1] = 50
# # # # # # # print(lst)
# # # # # #
# # # # # #
# # # # # # # a = (1, 2, 3, 4, 5, 6)
# # # # # # # print(a, type(a))
# # # # # #
# # # # # # # a = tuple("Hello")
# # # # # # # print(a,type(a))
# # # # # #
# # # # # #
# # # # # # # a = (1, 2, 3, 4, 5, 6)
# # # # # # # print(a[2])
# # # # # # # print(a[1:3],type(a))
# # # # # #
# # # # # # # from random import randint
# # # # # # #
# # # # # # # print(tuple(i +2 for i in range(10)))
# # # # # # #
# # # # # # # # print(tuple(input("->") for i in range(5)))
# # # # # # #
# # # # # # # # print(tuple(randint(50,100)for i in range(10)))
# # # # # #
# # # # # #
# # # # # # # t1 = tuple("hello")
# # # # # # # t2 = tuple("world")
# # # # # # # t3 = t1 + t2
# # # # # # # # print(t3 * 2)
# # # # # # # print(t3)
# # # # # # # # print(len(t3))
# # # # # # # #
# # # # # # # # print(t3.count('l')) #счетчик
# # # # # # # # print(t3.count('a'))
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(t3.index("l", 4)) #первое вхождение индекса, c четветого индекса счет
# # # # # # # #
# # # # # # # # print(t3.index("a"))
# # # # # # #
# # # # # # #
# # # # # # # for i in t3:
# # # # # # #     print(i,end=" ")
# # # # # #
# # # # # # # Задача
# # # # # # # def slicer(tpl, el):
# # # # # # #     if el in tpl:
# # # # # # #         if tpl.count(el) == 1:
# # # # # # #             return tpl[tpl.index(el):]
# # # # # # #         else:
# # # # # # #             first = tpl.index(el)
# # # # # # #             second = tpl.index(el, first + 1)
# # # # # # #             return tpl[first:second + 1]
# # # # # # #
# # # # # # #     else:
# # # # # # #         return tuple()
# # # # # # #
# # # # # # #
# # # # # # # print(slicer((1, 2, 3), 8))
# # # # # # # print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# # # # # # # print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# # # # # #
# # # # # #
# # # # # # #
# # # # # # # t = (True, 11, "Python", (4, 5, 6),["hello", "world"])
# # # # # # # print(t, id(t))
# # # # # # # t[4][0] = 'new'
# # # # # # # print(t,id(t))
# # # # # # # t[4].append("hi")
# # # # # # # print(t,id(t))
# # # # # #
# # # # # #
# # # # # # # Распаковка кортежа
# # # # # #
# # # # # # # t = (1, 2, 3)
# # # # # # # # x = t[0]
# # # # # # # # y = t[1]
# # # # # # # # z = t[2]
# # # # # # # # x, y, z = t
# # # # # # #
# # # # # # # x, y, z = 1, 2, 3,
# # # # # # # print(x, y, z)
# # # # # #
# # # # # #
# # # # # # # def get_user():
# # # # # # #     name = "Tom"
# # # # # # #     age = 22
# # # # # # #     is_married = False
# # # # # # #     return name, age, is_married
# # # # # #
# # # # # #
# # # # # # # user = get_user()
# # # # # # # print(user)
# # # # # # #
# # # # # # # # print(user[0])
# # # # # # # # print(user[1])
# # # # # # # # print(user[2])
# # # # # # # first_name, year, married = user
# # # # # #
# # # # # #
# # # # # # # first_name, year, married = get_user()
# # # # # # # print(first_name)
# # # # # # # print(year)
# # # # # # # print(married)
# # # # # #
# # # # # #
# # # # # # lst = [1, 2, 3, 4, 5]
# # # # # # print(lst, type(lst))
# # # # # # tpl = tuple(lst)
# # # # # # print(tpl, type(tpl))
# # # # # # lst2 = list(tpl)
# # # # # # print(lst2, type(lst2))
# # # # # # lst2.append(6)
# # # # # # tpl2 = tuple(lst2)
# # # # # # print(tpl2, type(tpl2))
# # # # #
# # # # #
# # # # # countries = (
# # # # #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
# # # # #     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# # # # #
# # # # # )
# # # # #
# # # # # # print(countries)
# # # # # for country in countries:
# # # # #     country_name, country_population, cities = country
# # # # #     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
# # # # #     for city in cities:
# # # # #         city_name, city_population = city
# # # # #         # print("\tГород:", city_name, ", население= ", city_population, sep="")
# # # # #
# # # # #
# # # #
# # # #
# # # # # Введите статистику частности символов в кортеже
# # # #
# # # # tpl = tuple(input("Введите строку:  "))
# # # # print(tpl)
# # # #
# # # # lst = []
# # # # for i in range(len(tpl)):
# # # #     if tpl[i] not in lst:
# # # #         lst.append(tpl[i])
# # # #
# # # # print(lst)
# # # # for i in range(len(lst)):
# # # #     print("Количество", lst[i], "=", tpl.count(lst[i]))
# # # #
# # # #
# # #
# # # # занятие 11 множество(Set) #хранит набор уникальных элементов(не повторяющихся)
# # #
# # # # s={"red","yellow","green", "yellow", "green"}
# # # # print(s)
# # # # print(type(s))
# # # # print(len(s)) #длина элементов в списке
# # #
# # # #
# # # # a = {} #в фигурных скобках хранится dict (пустые скобки) и set (заполненые скобки)
# # # # print(a, type(a))
# # #
# # # # a = set("hello")
# # # # print(a,type(a))
# # #
# # #
# # # # s = {i* i for i in range(10)}
# # # # print(s)
# # #
# # #
# # # # lst = [10, 2, 2, 2, 2, 3, 3, 8, 8, 9, 9, 9, 10]
# # # # print(lst)
# # # # # st = {i for i in lst if i % 2 == 0}  # избавлися от дубликатов
# # # # # print(st)
# # # # st = set(lst)
# # # # # print(st)
# # # # lst2 = list(st)
# # # # print(lst2)
# # # #
# # # #
# # # # t = {'red','yellow','red'}
# # # # print("green" in t)
# # # # print("blue" in t)
# # #
# # # # первый вариант в идеале
# # # # lst = ["ab_1", "ac_2", "bc_1", "bc_2", "anna"]
# # # # print([i for i in lst if 'a' in i])
# # # # print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# # # # print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
# # # #
# # # # #второй вариант расшифровка
# # # # lst2 =[]
# # # # for i in lst:
# # # #     if i[1] == "c":
# # # #         if i[0] == "a":
# # # #              lst2.append("A" + i[1:])
# # # #         else:
# # # #             lst2.append("B"+ i[1:])
# # # # print(lst2)
# # #
# # #
# # # # set = изменяемый тип данных
# # #
# # #
# # # # print(dir(set))
# # #
# # #
# # # # a = {'red', 'yellow', 'green'}
# # # # print(a)
# # # # a.add("black")  # добавление элемента
# # # # print(a)
# # #
# # # # a.remove("yellow") #удляет элемент по значению
# # # # print(a)
# # #
# # # # a.remove("blue") #KeyError
# # # # print(a)
# # #
# # #
# # # # el = "blue"
# # # # if el in a:
# # # #     a.remove(el)
# # # #
# # # #
# # # # print(a)
# # #
# # #
# # # # a.discard('yellow')
# # # # print(a)
# # #
# # #
# # # # a.pop()
# # # # print(a)
# # #
# # # #
# # # # a.clear() #очистка множества(всего)
# # # # print(a)
# # #
# # # # a = {0, 1, 2, 3}
# # # # b = {4, 3, 2, 1}
# # # # # c = a.union(b) {0, 1, 2, 3, 4}
# # # # c = a|b
# # # # print(c)
# # #
# # #
# # # # a = {0, 1, 2, 3}
# # # # b = {4, 3, 2, 1}
# # # #
# # # # c = a & b
# # # # print(c)
# # #
# # # # Задача
# # #
# # #
# # # # s1 = {1, 2}
# # # # s2 = {3}
# # # # s3 = {4, 5}
# # # # s4 = {3, 2, 6}
# # # # s5 = {6}
# # # # s6 = {7, 8}
# # # # s7 = {9, 8}
# # # #
# # # # # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# # # # s = s1.union(s2, s3, s4, s5, s6, s7)
# # # # print(s)
# # # #
# # # # print("кол-во уникальных:", len(s))
# # # # print("Min:", min(s))
# # # # print("Max:", max(s))
# # #
# # #
# # # # найдите общие буквы в двух разных строках
# # #
# # # s1 = "Hello"
# # # s2 = "How are you"
# # #
# # # a = set(s1) & set(s2)
# # # print(a)
# # #
# # # for i in a:
# # #     print(i, end =" ")
# # #
# # #
# # # # a = {0, 1, 2, 3, 4}
# # # # b = {3, 2, 1}
# # # # c = a <= b
# # # # print(c)
# # #
# # #
# # # # s = frozenset([1,2,3,4,5])
# # # # print(s)
# # # #
# # # #
# # # # a = frozenset({"hello", "world"})
# # # # print(a)
# # #
# # #
# # # # Словарь (dict)
# # #
# # # # lst = ["one", "two"]
# # # # d = {"first": "one", "second": "two"}
# # # #
# # # # print(d)
# # # # print(lst[1])
# # # # print(d["second"])
# # #
# # #
# # # # d = dict(a="Hello", b="World")
# # # # print(d)
# # # # print(type(d))
# # # #
# # # # d1 ={"a": "Hello", "b": "World"}
# # # # print(d1)
# # #
# # #
# # # # d = {0: "text", "one": 45, (1, 2): [2, 3, 4, 5], 42: [9, 8]}
# # # # print(d)
# #
# #
# # # Занятие 12
# #
# #
# # # d = {i: i ** 2 for i in range(1, 8)}
# # # print(d)
# # #
# # # # print(3 in d)
# # # # print(25 in d)
# # #
# # # key = 4
# # # if key in d:
# # #     del d[key]
# # # print(d)
# #
# #
# # # d = {i: i ** 2 for i in range(1, 8)}
# # # print(d)
# # # key = 5
# # #
# # # try:
# # #     del d[key]
# # # except KeyError:
# # #     print("Элемент с ключом", key, "нет в словаре")
# # #
# # # print(d)
# #
# #
# # # d = {"x1": 3,"x2": 7,"x3": 5,"x4": -1}
# # # #
# # # #
# # # #
# # # # res = 1
# # # # for key in d:
# # # #      res *=d[key]
# # # #
# # # #
# # # # print(res)
# #
# #
# # # задача
# #
# # # d = dict()
# # # d[1]= input("->")
# # # d[2]= input("->")
# # # d[3]= input("->")
# # # d[4]= input("->")
# # # print(d)
# #
# # # второй вариант решения задачи
# # # d = {i: input("->") for i in range(1, 5)}
# # # print(d)
# # # dislike = int(input("какой элемент исключить:"))
# # # del d[dislike]
# # # print(d)
# #
# #
# # # goods = {
# # #     '1': ['Core-i3-4330', 9, 4500],
# # #     '2': ['Core-i5-4670k', 9, 8500],
# # #     '3': ['Amd FX-6300', 9, 3700],
# # #     '4': ['Pentium G3220', 9, 2100],
# # #     '5': ['Core i5-3450', 9, 6400],
# # # }
# # #
# # # for i in goods:
# # #     print(i, ") ",goods[i][0]," - ", goods[i][1], " шт. по ", goods[i][2]," руб ", sep="")
# #
# #
# # # Методы словарей
# #
# # d = {"A": 1, "B": 2, "C": 3}
# # print(d)
# #
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# #
# # for i, j in d.items():
# #     i = 0
# #     print(i, ":", j)
# #
# # print(d)
# from operator import itemgetter
#
# #
# # d = {"A": 1, "B": 2, "C": 3}
# # d2 = d.copy()   #возвращается копия словаря
# # print("D=", d)
# # print("D2=", d2)
# # d2["B"] = 5
# # print("D=", d)
# # print("D2=", d2)
#
#
# # d= {"A": 1, "B": 2, "C": 3}
# # print(d)
# # # d.clear() #Удалить все элементы из словаря
# # # item =d.pop("W", "Такого ключа не существует в словаре") #удаление по ключу
# # item = d.popitem()
# # print(d)
# # print(item)
#
# # d= {"A": 1, "B": 2, "C": 3}
# # print(d)
# #
# #
# # item = d.setdefault("W", 5) #по заданному ключу добвляет новый ключ и значение, если ключа не существовало
# # print(d)
# # print(item)
#
#
# d = {"A": 1, "B": 2, "C": 3}
# # d2 = {"R": 7, "Q": 9}
# d2 = [("R", 7), ("Q", 9)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# print(d)
# from curses.textpad import rectangle
# from curses.textpad import rectangle
# from zone info import reset_t z path
# from python.car.electrocar import ElectroCar

# d = {"name": "Kelly", "age":25, "salary": 8000, "city": "New York"}
# #
# # new_d = dict()
# # # new_d["name"] = d.pop("name")
# # # new_d["salary"] = d.pop("salary")
# # new_d
# # print(d)
# # print(new_d)


# d = {"name": "Kelly", "age":25, "salary": 8000, "city": "New York"}
#
# d['location'] = d.pop("city")
#
# print(d)


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({v: k for k, v in d.items()})
# print({k: v for k, v in d.items() if v <= 2})


# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)


# задача
# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
#
# for i in lst:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)


# zip([],[])

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(b, a)}
# print(d)
# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
# a,b = zip(*lst)
# print(a)
# print(b)


# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 2, 1]
# d = dict(zip(letter, number))
# print(d)
#
# # d = sorted(zip(letter, number))
# # print(d)
#
# data = sorted(d.items())
# print(data)

# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# print(data2)
# data2.sort()
# print(data2)
#
#
# d3 = {v: k for k, v in data2}
# print(d3)


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})


# colors = ["red", "yellow", "green"]
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for j, color in enumerate(colors, 1):
#     print(j, ") ", color, sep="")


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
#
# for i, (k, v) in enumerate(d.items()):
#     print(i, ") ", k, ":", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1,2,3))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# print("Текст в локальном репозитории")

# print("Код написан на новом устройстве")

# Файлы

# f = open("text.txt")
# f = open(r"C:\Users\artur\Desktop\python zanytie\python\text.txt")
# print(*f)
# print(f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)

# f = open("text.txt", "r")
# print(f.read(3))
# print(f.read())
#
# f.close()

# Занятие 22   28.04.2025

# f = open("xyz.txt", "w")
# f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# f.close()


# f = open("xyz.txt")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readlines(15))
# print(f.readlines())
# f.close()


# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()

# lines = ["This is line1.\n","This is line2.\n","This is line3.\n"]
#
# f = open("lines.txt", "w")
# f.writelines(lines)
# f.close()

# lines = [str(i) for i in range(10, 1000, 15)]
# print(lines)
#
# f = open("lines.txt", "w")
# for index in lines:
#     f.write(index + "\t")
# f.close()


# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле; \nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()


# f = open("text.txt", "r")
# print(f.read(3))
# print(f.tell()) #возвращает текущую позицию услового курсора в файле
# print(f.seek(1)) #перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text5.txt", "a")
# print(f.write("I am learning Python"))
# print(f.seek(0))
# print(f.write("--new string--"))
# # print(f.read())
# f.close()


# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)


# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Конец программы")


# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
#
# print(sum(map(float, nums.split())))


# Задача написать функцию, которая выводит слово из файла , имеющее максимальную длину (или список слов, если таковых несколько)

# with open("res2.txt", "w") as f:
#     f.write(
#         "Файл - именованная область данных на носителе информации, используемая как базовый объект взаимодействия с данными"
#         " в операционных системах. ")
#
#
# def longest_words(file):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         return res
#
#
# print(longest_words("res2.txt"))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# Занятие 23

# написать программу, которая создаст приведенное на рисунке дерево директорий и файлов.


# import os
#
# dirs = [r"Work\F1", r"Work\F2\F21"]
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():
#     for file in files:
#         file_path = os.path.join(d, file)
#         # print(file_path)
#         open(file_path, "w").close()
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Такой- то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход{root}{' сверху вниз' if topdown else '  снизу вверх'}")
#     for root, directory, file_name in os.walk(root, topdown):
#         print(root)
#         print(directory)
#         print(file_name)
#     print("-" * 50)


#
# print_tree( " Work ", False)
# print_tree(" Work ", True)


# Теория

# import os  #импорт функции для работы с операционной системой, не зависящие от используемой операционной системы.
# import time  #импорт времени
#
#
# # print(os.path.exists(r"nested1\nested2\nestred3\text5.txt"))
# # print(os.path.isfile(r"nested1\nested2\nestred3\text5.txt"))
# # print(os.path.isdir(r"nested1\nested2\nestred3\text5.txt"))
#
#
#
# #метод размер файла
#
#
# print(os.path.getsize())    # размер файла в байтах
#
# #метод
#
# print(os.path.getatime())  #время последнего  доступа к файлу
# print(os.path.getmtime())  #время последненго изменения файла
# print(os.path.getctime())  #время создания файла
#
# a = os.path.getmtime(file)
# m = os.path.getmtime(file)
# c = os.path.getmtime(file)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)


# Парадигмы ООП:

# *инкупсуляция
# *наследование
# *полиморфизм


# Классы - свойства, поля (переменные) - методы (функции) атрибуты = свойства +методы

# class Point:
#     x = 1 # 100
#     y = 2


# p1 = Point()
# p1.x = 10
# p1.y = 20
# # Point.x = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point
# print(p2.x, p2.y)
# p2.x = 5
# print(p2.__dict__)
#
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         print("Устанавливаем координаты")
#
#
# p1 = Point()
# p1.set_coord()


# Занятие 24

# Задача

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "address"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана:{self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):       #устанавливаем новое имя
#         self.name = name
#
#
#     def get_name(self): #получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва","Чистопрудный бульвар,1А")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())


# Задача 2

# class Person:
#     skill = 10
#
#
#     def __init__(self,name,surname): #инициализатор
#        self.name = name
#        self.surname = surname
#        # print("Иницилазтор для ", self.name., self.surname )
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self,k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
#
# del p1
# print()
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)
# print(p1.count)
# print(p2.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота", self.name)
#         Robot.k +=1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#
#         print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут", self.name)
#
#
#
#
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов", Robot.k)
#
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов", Robot.k)
#
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
#
# del droid1
# del droid2
#
#
# print("Численность роботов", Robot.k)


# class Point:
#
#     def __init__(self,x,y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#
#     def __check_value(s):
#         if isinstance(s,int) or isinstance(s,float):
#             return True
#         return  False
#
#     def set_coord(self,x,y):
#       if Point.__check_value(x) and Point.__check_value(y):
#           self.__x = x
#           self.__y = y
#       else:
#            print("Координаты должны быть числами")
#
#
#     def get_coord(self):
#         return self.__x ,self.__y
#
# p1 = Point(5,10)
# # print(p1.__dict__)
# # p1.z = 20
# # print(p1.__x,p1.__y)
# # p1.x = 50
# # p1.y = "abc"
# p1.set_coord(5.2,100)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.__check_value(s)


# модификатор доступа public => self.x
# protected
# private


# Занятия 25  Видео 25 13.07.2025

# Напишите программу, осуществляющую проверку, существует ли указанный файл.
# если файл существует, выведите на экран имя этого файла и имя его директории, а также время последнего доступа к файлу.
# Если файл не существует, вывдеите соответсвующее сообщение

# import os
#
# file_path = "test/text4.txt"
#
# if os.path.exists(file_path):
#     directory, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name}({directory}) - время последнего доступа к файлу{atime} секунд")
#
# else:
#     print(f"Файл {file_path} не существует")


# Создать класс Rectangle , описывающий прямоугольник. В класс е должны быть все необходимые методы. а также методы
# вычисления площади, периметр, диагональ

# class Rectangle:
#     def __int__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self,length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
# r1 = Rectangle(4,12)
# r1.set_width(9)
# r1.set_length(3)
# print("Длина прямоугольника:" , r1.get_length())
# print("Ширина прямоугольника:" , r1.get_width())


# class Point:
#     __slots__ = ["x", "y"]
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.x, p1.y)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
#     def __check_value(c):
#         if isinstance(c,int) or isinstance(c, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         # print("Вызов __set_coord_x")
#         if Point.__check_value(x)
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     def __get_coord_x(self):
#         # print("Вызов __get_coord_x")
#         return self.__x
#
#     def __del_coord_x(self):
#         print("Удаление  свойства")
#         del self.__x
#
#     coordX = property(__get_coord_x, __set_coord_x)
#
#
#
# p1 = Point(5,10)
# # print(p1.__set_coord_x(50))
# p1.coordX = "abc"
# print(p1.coordX)


# class Person:
#      def __init__(self, name,old):
#          self.__name = name
#          self.__old = old
#
#      @property
#      def name(self):
#          return self.__name
#      @name.setter
#      def name(self, n):
#          self.__name = n
#
#      @name.deleter
#      def name(self):
#          del self.__name
#
#      @property
#      def old(self):
#          return self.__old
#      @old.setter
#      def old(self,year):
#          self.__old = year
#      @old.deleter
#      def old(self):
#          del self.__old
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = "31"
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
#
# print(Point.get_count())
# print(p1.get_count())


# class Change:


# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#             return mn
#
#     @staticmethod
#     def averange(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *=i
#         return fact
#
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.averange(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))


# занятие 15 видео 15
# Анонимные функции (Lambda-- выражения)

#
# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
#
# print(func(1, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20, ))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))( 1, 2, 3, 4))


# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
#
# for i in tpl:
#     print(i("abc___"))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))


# def outer(n):
#     return lambda x: n + x


# f = outer(42)
# print(f(3))

# outer =
# f = outer(42)
# print(f(3))
#
#
# outer = lambda n: lambda x: n + x


# print((lambda n: lambda x: n + x)(42)(3))


# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))


# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key = lambda i: i[1])
# print(lst)
# print(dict(lst))

# задача
# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, reverse= True, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item:item['rating'])
# print(res)

#
# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[3](12,6))

#
# d = {
#     1: lambda: print("понедельник"),
#     2: lambda: print("вторник"),
#     3: lambda: print("среда"),
#     4: lambda: print("четверг"),
#     5: lambda: print("пятница"),
#     6: lambda: print("суббота"),
#     7: lambda: print("воскресенье")
# }
#
# d[2]()


# print((lambda a, b: a if a > b else b)(5, 13))
# print((lambda lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))


# map(function, iterables), filter(function, iterables)


# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))
#
#
# print(list(map(lambda t: t*2, lst)))


# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round,t)))
# print(tuple(map(str,t)))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(dict(map(lambda x, y: (x, y), st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))


# Найти поэлементрно сумму чисел двух списокв:

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s)== 3, t)))


# Декораторы 23.08.2025

# def  hello():
#       return "Hello, I am func 'hello'"
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
# super_func(hello)


# def hello ():
#     return "Hello, I am func 'hello'"
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return func_wrapper
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
# test = my_decorator(func_test)
# test()

#
# def my_decorator(func): #декорирующая функция
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#     return func_wrapper
#
#
# @my_decorator #декоратор
# def func_test(): #декорируемая фнукция
#     print("Hello, I am func 'func_test'")
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>"+ fn() + "</b>"
#
#     return wrap
#
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
# @italic
# @bold
# def hello():
#     return "text"
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def decor(args1):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, "и", y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма: ")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность: ")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# Создать декоратор, который будет принмиать в виде аргумента число, которое будет умножаться на чилсо принимаеомое функцией

# def multiply(arg):
#     def my_decoator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#         return wrap
#     return my_decoator
#
#
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print("Результат: ", return_num(5))


# Строки

# print(bin(18)) #0b10010 - двоичная система счисления
# print(oct(18)) #0o22 - восьмеричная система счисления
# print(hex(18)) #0x12 - шестнадтеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# Unicode
# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * -3)
# print("y" in e)
# print(e[-1])
# print(e[1:3])


# Задача
# def change_char_to_str(s, old, new):
#     s2 = " "
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)


# префиксы

# print(u"привет")
# print("привет")

# print("C:\\file.txt\\")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" +"\\")


# Занятие 17

# name = "Дмиитрий"
# age = 25
# print("Меня зовут", name , ". Мне ", age , "лет.", sep=" ")
# print("Меня зовут" + name + ". Мне " + str(age) + "лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

#
# x = 10
# y = 5
# print(f"{x : }, {y = }")
# # print("x=", x, ", y=", y, sep="")
#
# print(f"{x} x {y}/7 ={round(x * y / 7, 2)}")
# print(f"{x} x {y}/7 ={x * y / 7:.4f}")


# num = 74
# print(f"{{{{{num}}}}}")

#
# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# st = ("Односторочный  "
#       "текст")
# print(st)
#
# s = """Многострочный
# текст
# """
# print(s)
#
#
#
#
# """Маногострочный коментарий
# текст
# """
# "Однострочный комментарий"
#
#
# s1 ='''многострочный текст'''
# print(s1)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# from math import pi
#
#
# def cylinder(r, h):
#
#     """
#     Вычислите площадь цилиндра.
#     Вычислет площадь цилинлра на основании заданной высоты и радиуса основания
#     :param r: положительное чило, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#'))
# print(ord('п'))


# while True:
#     n = input("->")
#     if n  != "-1":
#         print(ord(n))
#     else:
#         break


# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr +=[ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)


# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 97
# b = 122
#
# if a > b:
#
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())


s = "hello , WORLD! I am learning Python."

# print(s.capitalize())  # Hello , world! i am learning python.
# print(s.lower()) #hello , world! i am learning python.
# print(s.upper()) #HELLO , WORLD! I AM LEARNING PYTHON.

# print(s.count("h", 1, -4))
# print(s.lower().count("i"))


# print("abc123".isalnum())  #состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("abc".isalnum())
# print("123№".isalnum())


# print("ABCabc".isalpha()) #состоит ли строка из букв
# print("ABC$c".isalpha())


# print("123".isdigit()) #состоит ли строка из цифр
# print("123D".isdigit())


# print('aab'.islower())
# print('Aab'.islower())

# print('ABC'.isupper())

#
# print("py".center(10))
# print("py".center(12, "-"))


# print("   py".lstrip())
# print("   py".rstrip())
# print("  py   ".strip())


# Занятие 18


# пользователь вводит фамилию, имя и отчество. Приложение должно вывести фамилию и инициалы.
# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]} ")


# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))


# регулярные выражения


# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# # print(dir(re))
#
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список совпадений с шаблоном
# print(re.search(reg, s))  # возвращает только первое совпадение с шаблоном
# # print(re.search(reg,s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# # print(re.split(reg, s)) #возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s))  # поиск и замена


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789. [Hel_lo] Wor-ld"


# reg = r"[2025]"
# reg = r"[6-9]"
# reg = r"[А-яЁё]"
# reg = r"[A-Za-z]"
# print(re.findall(reg, s))


# reg = r"[А-яЁё.\]\[-]"
# print(re.findall(reg, s))

#
# reg = r"[^0-9]"
# print(re.findall(reg, s))

# Задача найти время в формате: [16:25]


# import re
#
# # st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапозоне от 00 до 59. 2021-06-15Т01:09."
# #
# # reg = "[0-9][0-9]:[0-9][0-9]"
# # print(re.findall(reg, st))
#
#
# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r" #.+", "", st))\


# Занятие 19

# import re

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
#
#
# text = "hello world"
# print(re.findall(r"\w+", text))
# print(re.findall(r"\w+", text, re.DEBUG))

# text = "hello worLd"
# print(re.findall(r"l", text, re.IGNORECASE ))


# text = """
# one
# two
# """

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+
# @
# [a-z.]+
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python
# PYTHON
# """
#
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# полезный символ
# s =  "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg,s))


# s = "int = 4,float = 4.0f, double = 8.0"
# reg = r"\w+\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))


# s = "Самолет прилетет 10/23/2025. Будет рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date = cls(day, month, year)
#         return date
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.01.2025"
# # day, month, year = map(int, string_date.split("."))
# # d = Date(day, month, year)
# d = Date.from_string("23.01.2025")
# print(d.string_to_db())

# Задача большая
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет{self.num} принадлежащей {self.surname} был закрыт")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-"*20)
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_pecents(self):
#         self.value += self.value * self.percent
#         print("проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self,val):
#         if val > self.value:
#             print(f"К сожлению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val}{Account.suffix} было успешно снятно")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val}{Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
#
#
#
#
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
#
#
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счет: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счет: {eur_val} {Account.suffix_eur}")
#
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_pecents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# Занятие 27


# Занятие 31

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return f"перед вызовом функции \n{self.func(a,b)} \nПосле вызвова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# Создать класс Power , который будет докорировать функцию. Функция возвращет результат умножения двух чисел (a = 2, b = 3), а класс возводит их в квадрат
# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return  self.func(a,b) ** 2
#
# @Power
# def multiply(a,b):
#     return a * b
#
# print(multiply(2,3))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
# p1 = Person("Виталий", "Карасев")
#
# p1.info()

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_lenght(self):
#         return len(self)
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_lenght())


# Упаковка данных - сохранение данных (серилизация)
# Распаковка данных - получение данных (десерелизация)


#
# import pickle
#
#
# file_name = "basket.txt"
#
# shop_list = {
#      "фрукты": ["яблоки","манго"],
#      "овощи": ("морковь", "лук"),
#      "бюджет": 1000
#  }
#
# with open(file_name, "wb") as f:
#      pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
#
# print(shop_list2)




# class Test:
#     num = 25
#     st = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 33)
#
#
#     def __str__(self):
#         return f"Число:{Test.num}\nСтрока:{Test.st}\nСписок:{Test.lst}\nКортеж{Test.tpl}"
#
# obj = Test()
# # print(obj)
#
# string  = pickle.dumps(obj)
# print(string)
#
#
# string2 = pickle.loads(string)
# print(string2 )


# import pickle
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "Test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#
# item1 = Test2() #35 test 4
# #print(item1)
# item2 = pickle.dumps(item1)


# import json
#
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     "20":None,
#     "None": "no",
#     "True": False,
#     'hobbies' : ('running', 'signing'),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#     ]
# }


# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent =4)
#
#
#
# with open("data_file.json", "r") as f:
#     data1 = json.load(f)
#
# print(data1)


# string = json.dumps(data)
# print(string, type(string))
#
# data1 = json.loads(string)
# print(data1,type(data1))

#
# x = {"name": "Виктор"}
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
#
#
# st = json.dumps(x)
# print(json.loads(st))

import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h']
    nums = ['1','2','3','4','5','6','7','8','9','0']

    while len(name) !=7:
        name+= choice(letters)
    # print(name)

    while len(tel) !=10:
        tel+= choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    return person

def write_json(person_dict):
    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = []

    data.append(person_dict)

    with open("persons.json", "w") as f:
          json.dump(data, f, indent=2)



for i in range(5):
      write_json(gen_person())


