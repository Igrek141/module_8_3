class Car(Exception):
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
            if self.__is_valid_numbers(numbers):
                self.__numbers = numbers
                print(f'{self.model} успешно создан')

    def __is_valid_vin(self, vin_number):
        try:
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True

    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')