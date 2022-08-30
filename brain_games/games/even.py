"""Логика игры 'Проверка на чётность'."""

from random import randint

# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0  # Минимальное значение числа
MAX_NUMBER = 1000  # Максимальное значение числа


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer


def is_even(number):
    """
    Чётное ли число?.

    Parameters:
        number :  integer : число.

    Returns:
        bool : булево : True - число чётное, False - число нечётное
    """
    return number % 2 == 0
