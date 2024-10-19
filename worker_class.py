# Классы для программы составления графика работы водителей.


from typing import List


class Manager:
    cars: List['Car']
    drivers: List['Driver']

    def vacation(self, driver: 'Driver', start: int, end: int):
        return
# Класс водитель.
class Driver:
    car: 'Car'

    # Инициализируем атрибуты.
    def __init__(self, list_day_month: List[int], num: int) -> None:
        self.__last_name: str = input('Введите фамилию водителя: ').title()
        self.__work_schedule: List[int] = list_day_month[num::4]

    def work_schedule(self):
        return self.__work_schedule

    def __str__(self) -> str:
        return f'{self.__last_name}'


# Класс автомобиль.
class Car:
    drivers: List[Driver]

    def __init__(self) -> None:

        # Инициализируем атрибуты.
        self.__garage_number: str = input('Введите гаражный номер автомобиля: ')
        # Проверка, что бы номер был введен цифрами.
        while not self.__garage_number.isdigit():
            print('Пожалуйста, введите номер цифрами!')
            self.__garage_number: str = input('Гаражный номер автомобиля: ')

    def __str__(self) -> str:
        return f'{self.__garage_number}'
