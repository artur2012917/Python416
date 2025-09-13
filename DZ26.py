# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self._num = num
#         self._surname = surname
#         self._percent = percent
#         self._value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#
#     @property
#     def num(self):
#         return self._num
#
#     @num.setter
#     def num(self, value):
#         if not isinstance(value, str):
#             raise ValueError("Номер счета должен быть строкой")
#         self._num = value
#
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @surname.setter
#     def surname(self, value):
#         if not isinstance(value, str) or not value:
#             raise ValueError("Фамилия должна быть непустой строкой")
#         self._surname = value
#
#
#     @property
#     def percent(self):
#         return self._percent
#
#     @percent.setter
#     def percent(self, value):
#         if not isinstance(value, (int, float)) or value < 0:
#             raise ValueError("Процент должен быть неотрицательным числом")
#         self._percent = value
#
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, amount):
#         if not isinstance(amount, (int, float)):
#             raise ValueError("Баланс должен быть числом")
#         if amount < 0:
#             raise ValueError("Баланс не может быть отрицательным")
#         self._value = amount
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет {self.num} принадлежащей {self.surname} был закрыт")
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
#         print("-" * 20)
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_pecents(self):
#         self.value += self.value * self.percent
#         print("проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
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
# print("До изменения:", acc.surname)
# acc.surname = "Иванов"
# print("После изменения:", acc.surname)
#
# print("Текущий баланс:", acc.value)
# acc.value = 2000
# print("Новый баланс:", acc.value)


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self._num = num
        self._surname = surname
        self._percent = percent
        self._value = value
        print(f"Счет #{self.get_num()} принадлежащий {self.get_surname()} был открыт.")
        print("*" * 50)


    def get_num(self):
        return self._num

    def set_num(self, value):
        if not isinstance(value, str):
            raise ValueError("Номер счета должен быть строкой")
        self._num = value


    def get_surname(self):
        return self._surname

    def set_surname(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Фамилия должна быть непустой строкой")
        self._surname = value


    def get_percent(self):
        return self._percent

    def set_percent(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Процент должен быть неотрицательным числом")
        self._percent = value


    def get_value(self):
        return self._value

    def set_value(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Баланс должен быть числом")
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._value = amount

    def __del__(self):
        print("*" * 50)
        print(f"Счет {self.get_num()} принадлежащей {self.get_surname()} был закрыт")

    def print_balance(self):
        print(f"Текущий баланс {self.get_value()} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.get_num()}")
        print(f"Владелец: {self.get_surname()}")
        self.print_balance()
        print(f"Проценты: {self.get_percent():.0%}")
        print("-" * 20)

    def edit_owner(self, surname):
        self.set_surname(surname)

    def add_pecents(self):
        new_value = self.get_value() + self.get_value() * self.get_percent()
        self.set_value(new_value)
        print("проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.get_value():
            print(f"К сожлению у вас нет {val} {Account.suffix}")
        else:
            self.set_value(self.get_value() - val)
            print(f"{val}{Account.suffix} было успешно снятно")
        self.print_balance()

    def add_money(self, val):
        self.set_value(self.get_value() + val)
        print(f"{val}{Account.suffix} было успешно добавлено!")
        self.print_balance()

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.get_value(), Account.rate_usd)
        print(f"Состояние счет: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.get_value(), Account.rate_eur)
        print(f"Состояние счет: {eur_val} {Account.suffix_eur}")



acc = Account("12345", "Долгих", 0.03, 1000)
print("До изменения:", acc.get_surname())
acc.set_surname("Иванов")
print("После изменения:", acc.get_surname())

print("Текущий баланс:", acc.get_value())
acc.set_value(2000)
print("Новый баланс:", acc.get_value())