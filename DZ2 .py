



num =int(input("Введите пятизначное число: "))
a= num%10
num//=10


b=num%10
num//=10


c=num%10
num//=10


d=num%10
num//=10


e=num%10


print("Произведение цифр числа: ", a*b*c*d*e)
print("Среднее арифметическое:", (a+b+c+d+e)/5)