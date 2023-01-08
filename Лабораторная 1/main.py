import doctest


class Fridge:
    def __init__(self, max_volume: int, current_load: float, food_weight: float):
        """
        Создание и подготовка к работе объекта "Холодильник"
        :param max_volume: Максимальный объем холодильника в литрах
        :param current_load: Загрузка холодильника в литрах
        :param food_weight: Вес еды
        Примеры:
        >>> weight = Fridge(300, 150, 9.5)  # инициализация экземпляра класса
        """

        if not isinstance(max_volume, int):
            raise TypeError("Максимальный объем должен быть типа int")
        if max_volume <= 0:
            raise ValueError("Максимальный объем должен быть положительным числом")
        self.max_volume = max_volume

        if not isinstance(current_load, (int, float)):
            raise TypeError("Загрузка холодильника должна быть типа int или float")
        if current_load <= 0:
            raise ValueError("Загрузка холодильника должна быть положительным числом")
        self.current_load = current_load

        if not isinstance(food_weight, (int, float)):
            raise TypeError("Вес еды должен быть типа int или float")
        if food_weight < 0:
            raise ValueError("Вес еды не может быть отрицательным числом")
        self.food_weight = food_weight

    def can_it_be_fridge(self) -> bool:
        """
        Функция, которая проверяет, возможность наполнения холодильника
        :return: Возможно ли наполнение холодильника
        Примеры:
        >>> weight = Fridge(300, 150, 9.5)
        >>> weight.can_it_be_fridge()
        """
        ...

    def fridge_volume(self) -> float:
        """
        Функция для расчета оставшегося объема
        :return: Оставшийся объем
        Примеры:
        >>> weight = Fridge(300, 150, 9.5)
        >>> weight.fridge_volume()
        """
        ...


class Boiler:

    def __init__(self, water_volume: float, temperature: float):
        """
        Создание и подготовка к работе объекта "Котел"
        :param water_volume: Объём нагреваемой воды
        :param temperature: Необходимая температура воды
        Примеры:
        >>> water_heat = Boiler(20, 80)  # инициализация экземпляра класса
        """
        max_volume = 5
        desired_temperature = 40
        if not isinstance(water_volume, (float, int)):
            raise TypeError("Объём нагреваемой воды должен быть типа float или int")
        if water_volume < max_volume:
            raise ValueError("Объем воды должен быть не менее", max_volume, "литров")
        self.water_volume = water_volume

        if not isinstance(temperature, (float, int)):
            raise TypeError("Желаемая температура воды должна быть типа float или int")
        if temperature < desired_temperature:
            raise ValueError("Желаемая температура воды должна быть не менее", desired_temperature, "градусов")
        self.temperature = temperature

    def constant(self) -> None:
        """
        Поддержание температуры воды
        Примеры:
        >>> water_heat = Boiler(20, 80)
        >>> water_heat.constant()
        """
        ...

    def time(self, power_level: int) -> float:
        """
        Функция для расчета необходимого времени для нагрева
        :param power_level: уровень мощности котла
        :rise TypeError: уровень мощности нагрева должен быть типа int
        :rise ValueError: уровень мощности нагрева должен быть от 1 до 5
        :return: время, необходимое для нагрева объема воды
        Примеры:
        >>> water_heat = Boiler(20, 80)
        >>> water_heat.time(5)
        """
        min_level = 1
        max_level = 5
        if not isinstance(power_level, int):
            raise TypeError("уровень мощности нагрева должен быть типа int")
        if min_level < power_level < max_level:
            raise ValueError("уровень мощности нагрева должен быть от", min_level, "до", max_level)
        ...


class Pot:
    def __init__(self, wrap_status, liquid_status, liquid_capacity):
        """"
        Создание объекта класса "банка"
        :param wrap_status: статус банки (open или closed)
        :param liquid_status: текущее количество жидкости (литры) в банке
        :param liquid_capacity: вместимость банки (литры)
        Примеры:
        >>> my_pot = Pot(0, 0.5, 3) # инициализация экземпляра класса
        """

        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("банка должна быть открыта (0) или закрыта (1)")
        self.wrap_status = wrap_status
        if not isinstance(liquid_status, (int, float)):
            raise TypeError("переменная должна быть типа float или int")
        if not isinstance(liquid_capacity, (int, float)):
            raise TypeError("переменная должна быть типа float или int")
        if liquid_status > liquid_capacity:
            raise ValueError("Вместимость должна быть больше занятого объема")
        if liquid_status < 0:
            raise ValueError("Количество жидкости не должно быть меньше 0")
        if liquid_capacity < 0:
            raise ValueError("Количество жидкости не должно быть меньше 0")
        self.liquid_status = liquid_status
        self.liquid_capacity = liquid_capacity

    def open_pot(self):
        """"
        Функция открывает банку, если та была закрыта,
        в случае успеха выводится сообщение (банка открыта).
        :raise ValueError: вызывает ошибку, если банка была открыта при вызове метода
        Примеры:
        >>> my_pot = Pot(1, 0.5, 3)
        >>> my_pot.open_pot()
        """

    ...

    def close_pot(self):
        """"
        Функция закрывает банку, если та была открыта,
        в случае успеха выводится сообщение (банка закрыта).
        :raise ValueError: вызывает ошибку, если банка была закрыта при вызове метода
        Примеры:
        >>> my_pot = Pot(0, 0.5, 3)
        >>> my_pot.close_pot()
        """
        ...

    def add_liquid(self, liquid_input):
        """"
        Функция добавляет жидкость в банку, если банка открыта
        :raise TypeErroe: вызывает ошибку при попытке налить не целое и не вещественное число жидкости
        :raise ValueError: вызывает ошибку при попытке переполнить банку или налить отрицательные значения
        :return: новое число занятого объёма банки
        примеры:
        >>> my_pot = Pot(0, 0.5, 3)
        >>> my_pot.add_liquid(1)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
