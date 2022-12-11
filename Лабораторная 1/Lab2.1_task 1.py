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

        if not isinstance(max_volume, (int)):
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

        if not isinstance(water_volume, (float, int)):
            raise TypeError("Объём нагреваемой воды должен быть типа float или int")
        if water_volume < 5:
            raise ValueError("Объем воды должен быть не менее 5 литров")
        self.water_volume = water_volume

        if not isinstance(temperature, (float, int)):
            raise TypeError("Желаемая температура воды должна быть типа float или int")
        if temperature < 40:
            raise ValueError("Желаемая температура воды должна быть не менее 40 градусов")
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
        if not isinstance(power_level, int):
            raise TypeError("уровень мощности нагрева должен быть типа int")
        if 5 < power_level < 1:
            raise ValueError("уровень мощности нагрева должен быть от 1 до 5")
        ...


class House:
    def __init__(self, status_: int, roomers: float, rooms: float):
        """"
        Создание объекта класса "Дом"
        :param status_: открыт или закрыт дом
        :param roomers: количество жильцов
        :param rooms: количество комнат в доме
        Примеры:
        >>> my_House = House(0, 5, 4)
        """

        if (status_ != 0) and (status_ != 1):
            raise ValueError("Дом может быть открыт(1) или закрыт (0)")
        self.status_ = status_
        if not isinstance(roomers, (int, float)):
            raise TypeError("Введите количество жильцов в цифрах")
        if roomers < 0:
            raise ValueError("Количество жильцов не может быть отрицательным")
        self.roomers = roomers
        if rooms < 0:
            raise ValueError("Количество комнат не может быть отрицательны")
        if not isinstance(rooms, (int, float)):
            raise TypeError("Введите количество комнат в цифрах")
        self.rooms = rooms

    def open_House(self):
        """"
        Открывает дом, выводится сообщение (дом открыт).
        :raise ValueError: вызывает ошибку, если дом уже открыт при вызове метода
        Примеры:
        >>> my_House = House(0, 5, 4)
        >>> my_House.open_House()
        """

    def close_House(self):
        """"
        Закрывает дом, выводится сообщение (дом закрыт).
        :raise ValueError: вызывает ошибку, если дом уже закрыт при вызове метода
        Примеры:
        >>> my_House = House(1, 5, 4)
        >>> my_House.close_House()
        """

    def add_roomers(self, roomers_input):
        """
        :param roomers_input: количество заселяемых людей
        Добавляем жильцов, если дом открыт
        :raise TypeError: вызывает ошибку при попытке ввести не целое число жильцов
        :raise ValueError: вызывает ошибку при заселении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если дом закрыт
        :return: новое число жильцов
        примеры:
        >>> my_House = House(1, 5, 4)
        >>> my_House.add_roomers(5)
        """

    def eject_roomers(self, roomers_input):
        """
        Выселяем постояльцев, если дом открыт
        :param roomers_input: количество выселяемых людей
        :raise TypeError: вызывает ошибку при попытке ввести не целое число жильцов
        :raise ValueError: вызывает ошибку при выселении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если дом закрыт
        :return: новое число постояльцев
        Примеры:
        >>> my_House = House(1, 5, 4)
        >>> my_House.eject_roomers(2)
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
