student = {}

n = int(input("Количество студентов:  "))
s = 0
for i in range(n):
    name = input(str(i + 1) + "-й студент: ")
    point = int(input("Балл: "))
    student[name] = point
    s += point

average = s/n
print(student)
print("Средний балл: ",round(average), ". Стдуенты с баллом выше среднего: ", sep="")

for i in student:
    if student[i] > average:
        print(i)