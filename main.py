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
