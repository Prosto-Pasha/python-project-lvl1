"""Логика игры 'Наибольший общий делитель'."""

from random import randint

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1  # Минимальное значение числа
MAX_NUMBER = 150  # Максимальное значение числа


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question_text = '{0} {1}'.format(number1, number2)
    correct_answer = euqlid_gcd(number1, number2)
    return question_text, str(correct_answer)


def euqlid_gcd(number1, number2):
    """
    Определяем наибольший общий делитель чисел number1 и number2.

    Методом Евклида.

    Parameters:
        number1 : число, первый параметр.
        number2 : число, второй параметр.

    Returns:
        integer : число, наибольший общий делитель чисел number1 и number2
    """
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2
