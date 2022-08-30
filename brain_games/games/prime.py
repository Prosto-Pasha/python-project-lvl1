"""Логика игры 'Простое ли число?'."""

import math
from random import randint

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1  # Минимальное значение числа
MAX_NUMBER = 1000  # Максимальное значение числа


def get_question_answer():
    """
    Получить вопрос и правильный ответ.

    Returns:
        tuple : кортеж с текстом вопроса и правильным ответом
    """
    question_number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question_number) else 'no'
    return question_number, correct_answer


def is_prime(number):
    """
    Проверить, простое ли число.

    Parameters:
        number : число, проверяемое число.

    Returns:
        bool : булево : True - число простое, False - в противном случае.
    """
    max_index = int(math.sqrt(number))
    index = 2
    while index <= max_index:
        if number % index == 0:
            return False
        index += 1
    return True
