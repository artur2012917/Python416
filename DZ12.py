dict_sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
              "Tom": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
              "Anne": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
              "Fiona": {"N": 3056, "S": 8463, "E": 8441, "W": 2694}}

for x, y in dict_sales.items():
    print(x)
    for i, j in y.items():
        print("\t", i, ": ", j, sep="")

person = input("Имя: ")
region = input("Регион: ")
print(dict_sales[person][region])
new_data = int(input("Новое значение:  "))
dict_sales[person][region] = new_data
print(dict_sales[person])
