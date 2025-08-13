# def func1(*args):
#     print("args:", args)
#     print(args[0])
#
#
# def func2(**kwargs):
#     print("kwargs:", kwargs)
#     print(kwargs["one"])
#
#
# func1(1,2,3,4,5,6)
# func2(one= 123, two = 456)


# области видимости
# name = "Tom" #глобальная переменная
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson" #локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# hi()
# bye()
# print(name)


# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)


# print_ = 5
#
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))


# x = 4


# def func():
#     x = 2 #2
#
#     def inner():
#        print("x =", x) #4
#        print(x + 3) #5
#
#     inner() #3
#
# func()  #1


# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello", who)
#     inner()
#
#
# outer("World")


# def fun1():
#     a = 6 #2
#
#     def fun2(b):
#         a = 4 #5
#         print("Сумма:", a + b) #6
#
#     print("a:", a) #3
#     fun2(3) #4
#
# fun1() #1

# x = 25
# t = 5
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =",a)
#
#     inner()
#     t = a
#
# fn()
# c = x + t
# print(c)

def outer(a1, b1, a2, b2):
    a = 0
    b = 0

    def inner():
        a = a1 + a2
        b = b1 + b2

    inner()
    return [a,b]

print(outer(2,3,-1,4))