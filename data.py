from random import randint

class Person:
    user_name = 'Марина'
    email = f'marina_maleeva_46_123@mail.ru'
    password = f'12345Qwerty'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@mail.ru'
    password = f'{randint(1000, 9999)}Qwerty'