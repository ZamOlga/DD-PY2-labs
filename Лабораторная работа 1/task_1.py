# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Bottle:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бутылка
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> bottle = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем бутылки
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # занятый объем бутылки

    def is_full_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка полной

        :return: Является ли бутылка полной

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.is_full_bottle()
        """
    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.add_water_to_bottle(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")


class Dog:
    def __init__(self, name: str):
        """
        Создание и подготовка к работе объекта Собака
        :param name: Имя собаки
        :param tricks: список трюков, которым обучена собака
        Примеры:
        >>> dog = Dog('Бобик')  # инициализация экземпляра класса
        """
        self.name = name
        self.tricks = []    # создание пустого списка для каждой собаки

    def add_trick(self, trick: str) -> None:
        """
        Добавление трюков для собаки.
        :param trick: название трюка
        Примеры:
        >>> dog = Dog('Бобик')
        >>> dog.add_trick('Голос')
        """

    def check_trick(self, trick: str) -> bool:
        """
        Функция которая проверяет обучена ли собака трюку

        :return: Знает ли собака трюк

        Примеры:
        >>> dog = Dog('Бобик')
        >>> dog.check_trick('Голос')
        """


class Warehouse:
    def __init__(self, products: str, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бутылка
        :param products: вид продукции на складе
        :param capacity_volume: вместимость склада
        :param occupied_volume: количество продукции на складе
        Примеры:
        >>> warehouse = Warehouse('яблоки',500, 0)  # инициализация экземпляра класса
        """
        self.products = products    # вид продукции на складе
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Вместимость должна быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Вместимость должна быть положительным числом")
        self.capacity_volume = capacity_volume  # вместимость склада
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество продукции на складе должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество продукции на складе не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # количество продукции на складе

    def is_empty_warehouse(self) -> bool:
        """
        Функция которая проверяет является ли склад свободным

        :return: Является ли склад свободным

        Примеры:
        >>> warehouse = Warehouse('яблоки',500, 0)
        >>> warehouse.is_empty_warehouse()
        """
    def add_products_to_warehouse(self, new_product: str, volume: Union[int, float]) -> None:
        """
        Заполнение в склада.
        :param new_product: тип продукции

        :raise ValueError: Если количество добавляемой продукции превышает свободное место в бутылке, то вызываем ошибку
        :raise TypeError: Если новая продукция не совпадает с находящейся на складе

        Примеры:
        >>> warehouse = Warehouse('яблоки',500, 0)
        >>> warehouse.add_products_to_warehouse('яблоки', 200)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Количество добавляемой продукции должно быть типа int или float")
        if volume < 0:
            raise ValueError("Количество добавляемой продукции должно быть положительным числом")


if __name__ == "__main__":
    doctest.testmod()


