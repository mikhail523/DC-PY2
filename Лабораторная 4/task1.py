class Motorbike:
    """Базовый класс"""

    def __init__(self, brand: str, model: str, year: int, max_speed: int):
        """
        Создание и подготовка к работе объекта "Мотоцикл"
        :param brand: Марка мотоцикла
        :param model: Модель мотоцикла
        :param year: Год выпуска
        :param max_speed: Максимальная скорость автомобиля в км/ч
        Пример:
        >>> my_motorbike = ('Honda', 'CBR', 2018, 120)
        """

        if not isinstance(brand, str):
            raise TypeError('Название марки вашего мотоцикла должно соответствовать типу str')
        self.brand = brand
        if not isinstance(model, str):
            raise TypeError('Модель вашего мотоцикла должно соответствовать типу str')
        self.model = model
        if not isinstance(year, int):
            raise TypeError('Год выпуска вашего мотоцикла дожен соответствовать типу int')
        self.year = year
        if not max_speed > 0:
            raise ValueError('Максимальная скорость мотоцикла должна быть положительным числом')
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}) in {self.max_speed} km/h"

    def __repr__(self) -> str:
        return f"Motorbike({self.brand!r}, {self.model!r}, {self.year!r}, {self.max_speed!r})"


class SportsBike(Motorbike):
    """ Дочерний класс """

    def __init__(self, brand: str, model: str, year: int, max_speed: int):
        """
        Создание и подготовка к работе дочернего класса "Спортивный мотоцикл"
        :param brand: Марка мотоцикла
        :param model: Модель мотоцикла
        :param year: Год выпуска
        :param max_speed: Максимальная скорость автомобиля в км/ч
        Пример:
        >>> motorbike = SportsBike('Yamaha', 'R1', 2020, 150)
        """
        super().__init__(brand, model, year, max_speed)
        self.max_speed = max_speed

    def __str__(self) -> str:
        return f"{super().__str__()} with a top speed of {self.max_speed} km/h"

    def __repr__(self) -> str:
        return f"SportsBike({self.brand!r}, {self.model!r}, {self.year!r}, {self.max_speed!r})"

    def accelerate(self):
        return "The sports bike is accelerating."

    def brake(self):
        return "The sports bike is braking."


if __name__ == "__main__":
    # Write your solution here
    pass
