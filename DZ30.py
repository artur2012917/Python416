import math
from abc import ABC, abstractmethod


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side * self.side

    def draw(self):
        return ("* " * self.side + "\n") * self.side

    def info(self):
        print(
            f"=== Квдарат ===\nСторона:{self.side}\nЦвет:{self.color}\nПлощадь:{self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")


sq = Square(3, "red")
sq.info()


class Rectangle(Shape):
    def __init__(self, lenght, width, color):
        super().__init__(color)
        self.length = lenght
        self.width = width

    def get_perimetr(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    def draw(self):
        return ("* " * self.width + "\n ") * self.length

    def info(self):
        print(f"===Прямоугольник===\nДлина:{self.length}\nШирина:{self.width}\nЦвет:{self.color} "
              f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimetr()}\n{self.draw()}\n")


sq = Square(3, "red")
sq.info()
rect = Rectangle(3, 7, "green")
rect.info()


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3, color):
        super().__init__(color)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimetr(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        p = self.get_perimetr() / 2
        return math.sqrt(p * (p - self.side_1) * (p - self.side_2) + (p - self.side_3))

    def draw(self):
        # return
        rows = []
        for n in range(self.side_2):
            rows.append(" " * n + "*" * (self.side_1 - 2 * n))
        return "\n".join(rows)


    def info(self):
        print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3:{ self.side_3}"
                f"\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimetr()}\n{self.draw()}")


sq = Square(3, "red")
sq.info()
rect = Rectangle(3, 7, "green")
rect.info()
tr = Triangle(11, 6, 6, "yellow")
tr.info()
