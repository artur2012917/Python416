class Car:
    def __init__(self, model="", year=0, creator="", engine_power=0, color="", price=0):
        self.__model = model
        self.__year = year
        self.__creator = creator
        self.__engine_power = engine_power
        self.__color = color
        self.__price = price


    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_creator(self, creator):
        self.__creator = creator

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price


    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_creator(self):
        return self.__creator

    def get_engine_power(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price


    def display_data(self):
        print("********** Данные автомобиля ***********")
        print(f"Название модели: {self.__model}")
        print(f"Год выпуска: {self.__year}")
        print(f"Производитель: {self.__creator}")
        print(f"Мощность двигателя: {self.__engine_power} л.с.")
        print(f"Цвет машины: {self.__color}")
        print(f"Цена: {self.__price}")
        print()


    def input_data(self):
        self.__model = input("Введите название модели: ")
        self.__year = int(input("Введите год выпуска: "))
        self.__creator = input("Введите производителя: ")
        self.__engine_power = int(input("Введите мощность двигателя (л.с.): "))
        self.__color = input("Введите цвет машины: ")
        self.__price = float(input("Введите цену: "))



if __name__ == "__main__":

    car = Car()


    car.set_model("X8 M50i")
    car.set_year(2021)
    car.set_creator("BMW")
    car.set_engine_power(530)
    car.set_color("white")
    car.set_price(10790000)


    car.display_data()


