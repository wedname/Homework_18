"""
#Задание 1:
1) Нужно создать абстрактный класс "Машина".
Который должен содержать следующие функции:
 - Получить марку
 - Получить год покупки машины
 - Получить цену
 - Получить пробег

2) Создать класс "BMW", "Audi", "Bentley" которые будут наследоваться от класса "Машина", они должны содержать полную
реализацию всех функций класса от которого наследуются.
В качестве готового ДЗ отправить файл с расширением .py
"""


class Car:
    def __init__(self, model: str, year: int, price: float, mileage: float, vin: str):
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.vin = vin

    def get_mark(self):
        pass

    def get_model(self):
        pass

    def get_year(self):
        pass

    def get_price(self):
        pass

    def get_mileage(self):
        pass

    def get_cars_number(self):
        pass


class BMW(Car):
    def __init__(self, model, year, price, mileage, vin):
        super(BMW, self).__init__(model, year, price, mileage, vin)

    def __str__(self):
        return f"Марка: {self.get_mark()}\n " \
               f"Модель: {self.model}\n " \
               f"Год выпуска: {self.year}\n " \
               f"Цена: ${self.price}\n " \
               f"Пробег: {self._mileage}\n " \
               f"VIN: {self.vin}\n"

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def get_mark(self):
        return "BMW"

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def get_cars_number(self):
        return self.vin

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        self._mileage = value

    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value: str):
        self._vin = value


class Audi(Car):
    def __init__(self, model, year, price, mileage, vin):
        super(Audi, self).__init__(model, year, price, mileage, vin)

    def __str__(self):
        return f"Марка: {self.get_mark()}\n " \
               f"Модель: {self.model}\n " \
               f"Год выпуска: {self.year}\n " \
               f"Цена: ${self.price}\n " \
               f"Пробег: {self._mileage}\n " \
               f"VIN: {self.vin}\n"

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def get_mark(self):
        return "Audi"

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def get_cars_number(self):
        return self.vin

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        self._mileage = value

    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value: str):
        self._vin = value


class Bentley(Car):
    def __init__(self, model, year, price, mileage, vin):
        super(Bentley, self).__init__(model, year, price, mileage, vin)

    def __str__(self):
        return f"Марка: {self.get_mark()}\n " \
               f"Модель: {self.model}\n " \
               f"Год выпуска: {self.year}\n " \
               f"Цена: ${self.price}\n " \
               f"Пробег: {self._mileage}\n " \
               f"VIN: {self.vin}\n"

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def get_mark(self):
        return "Bentley"

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def get_cars_number(self):
        return self.vin

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: float):
        self._mileage = value

    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value: str):
        self._vin = value


"""
#Задание 2:
Написать консольный интерфейс который должен реализовать следующие функции:
 - Добавление машины (Перед этим необходимо запросить марку "BMW", "Audi", "Bentley") - DONE
 - Удаление машины - DONE
 - Изменение машины - DONE
 - Просмотр всех машин (Реализовать с помощью функции __str__ во всех классах) - DONE
 - Посмотреть машины с большим пробегом (Большой пробег считается если машина за год проехала больше 17К км. Например
 машину купили в 2019 году, а ее пробег составляет 60К, допустимой нормой за год 17К, машина проездила уже +2 года
 (2021-2019), т.е. нормальный пробег для нее составляет 34К км)
 - Получить 5 машин с самой большой/маленькой ценой - DONE

!!Нужно использовать код из первого задания.

В качестве готового ДЗ отправить файл с расширением .py
"""


def search_cars(vin: str, list_of_cars: list):
    for i in range(len(list_of_cars)):
        if list_of_cars[i].vin == vin:
            return i
    return None


def add_car(value, list_of_cars: list):
    cars_vin = input("Введите VIN автомобиля: ")
    car = search_cars(cars_vin, list_of_cars)
    if car is None:
        cars_model = input("Введите модель автомобиля: ")
        cars_year = int(input("Введите год выпуска автомобиля: "))
        cars_price = float(input("Введите цену автомобиля: "))
        cars_mileage = float(input("Введите пробег автомобиля: "))
        if value == "BMW":
            car = BMW(cars_model, cars_year, cars_price, cars_mileage, cars_vin)
            list_of_cars.append(car)
        elif value == "Audi":
            car = Audi(cars_model, cars_year, cars_price, cars_mileage, cars_vin)
            list_of_cars.append(car)
        elif value == "Bentley":
            car = Bentley(cars_model, cars_year, cars_price, cars_mileage, cars_vin)
            list_of_cars.append(car)
        else:
            print("В базе нет такой марки!")
    else:
        print("Автомобиль с таким VIN уже есть!")


def delete_car(delete_vin: str, list_of_cars: list):
    for i in range(len(list_of_cars)):
        if list_of_cars[i].vin == delete_vin:
            list_of_cars.pop(i)
            break
    else:
        print("Нет такого автомобиля!")


def edit_car(edit_vin_car: str, list_of_cars: list):
    car = search_cars(edit_vin_car, list_of_cars)
    if car is None:
        print("Нет такого автомобиля!")
    else:
        list_of_cars[car].model = input("Введите модель автомобиля: ")
        list_of_cars[car].year = int(input("Введите год выпуска автомобиля: "))
        list_of_cars[car].price = float(input("Введите цену автомобиля: "))
        list_of_cars[car].mileage = float(input("Введите пробег автомобиля: "))
        list_of_cars[car].vin = input("Введите VIN автомобиля: ")


def show_cars(list_of_cars: list):
    for i in range(len(list_of_cars)):
        print(str(list_of_cars[i]))


def get_cars_with_big_mileage(list_of_cars: list):
    for i in range(len(list_of_cars)):
        if list_of_cars[i].year == 2021:
            temp = list_of_cars[i].mileage
        else:
            temp = list_of_cars[i].mileage / (2021 - list_of_cars[i].year)
        if temp >= 17000:
            print(str(list_of_cars[i]))


def five_cars_with_small_price(list_of_cars: list):
    sorted_list_of_car = sorted(list_of_cars)
    if len(list_of_cars) >= 5:
        for i in range(0, 5):
            print(str(sorted_list_of_car[i]))
    else:
        for i in range(len(list_of_cars)):
            print(str(sorted_list_of_car[i]))


def five_cars_with_big_price(list_of_cars: list):
    sorted_list_of_car = sorted(list_of_cars, reverse=True)
    if len(list_of_cars) >= 5:
        for i in range(0, 5):
            print(str(sorted_list_of_car[i]))
    else:
        for i in range(len(list_of_cars)):
            print(str(sorted_list_of_car[i]))


cars_list = [
    BMW("M3", 2019, 20000, 90000, "12345678"),
    Audi("RS6", 2014, 45000, 35000, "14587665"),
    Bentley("Continental GT", 2015, 112000, 15000, "1157429889")
]

if __name__ == '__main__':
    while True:
        menu = "1 - Добавление автомобиля\n" \
               "2 - Удаление автомобиля\n" \
               "3 - Изменение автомобиля\n" \
               "4 - Просмотр всех автомобилей\n" \
               "5 - Посмотреть автомобили с большим пробегом\n" \
               "6 - Получить 5 автомобилей с самой большой/маленькой ценой\n" \
               "0 - Закрыть программу\n--> "
        controls_enter = input(menu)

        if controls_enter == "1":
            mark_input = input("Введите марку машины(BMW, Audi или Bentley): ")
            add_car(mark_input, cars_list)

        elif controls_enter == "2":
            input_vin = input("Введите vin машины: ")
            delete_car(input_vin, cars_list)

        elif controls_enter == "3":
            input_edit_vin_car = input("Введите VIN автомобиля: ")
            edit_car(input_edit_vin_car, cars_list)

        elif controls_enter == "4":
            show_cars(cars_list)

        elif controls_enter == "5":
            get_cars_with_big_mileage(cars_list)

        elif controls_enter == "6":
            print(f"Пять самых дешевых автомобилей:\n")
            print(f"{five_cars_with_small_price(cars_list)}")
            print(f"Пять самых дорогих автомобилей:\n")
            print(f"{five_cars_with_big_price(cars_list)}")

        elif controls_enter == "0":
            exit()
        else:
            print("Нет такого действия!")
            continue
